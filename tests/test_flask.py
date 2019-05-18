import json

import pytest
from vnseg.flask import make_app


_test_app = make_app()
_test_app.testing = True


@pytest.fixture
def client():
    return _test_app.test_client()


def test_tokenize_get_given_empty_sentence(client):
    res = client.get('/tokenize/')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == []
