import json
from random import randrange
from urllib.parse import quote

import pytest
from hypothesis import given
from hypothesis.strategies import text
from vnsegapi import parse, server


_test_app = server.make_app()
_test_app.testing = True


@pytest.fixture
def client():
    return _test_app.test_client()


@given(string=text(max_size=250))
def test_tokens_identical_with_tokenize(client, string):
    res = client.get(f"/api/tokens?str={quote(string)}")
    tokens = json.loads(res.data)
    assert tokens == parse.tokenize(string)


def test_tokens_returns_status_400_given_no_str(client):
    res = client.get(f"/api/tokens")
    assert res.status_code == 400


def test_tokens_rejects_more_than_250_chars(client):
    res = client.get(f"/api/tokens?str={'a' * randrange(251, 20000)}")
    assert res.status_code == 400
