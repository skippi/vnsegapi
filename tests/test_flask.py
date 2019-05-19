import json
from urllib.parse import quote

import pytest
from vnseg.flask import make_app


_test_app = make_app()
_test_app.testing = True


@pytest.fixture
def client():
    return _test_app.test_client()


def test_tokens_given_empty_sentence(client):
    res = client.get('/api/tokens?str=')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == []


def test_tokens_given_one_word_sentence(client):
    res = client.get(f'/api/tokens?str={quote("táo")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['táo']


def test_tokens_given_two_words_each_as_tokens(client):
    res = client.get(f'/api/tokens?str={quote("táo cao")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['táo', 'cao']


def test_tokens_given_many_words_three_tokens(client):
    res = client.get(f'/api/tokens?str={quote("Đây là từ điển")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['Đây', 'là', 'từ điển']


def test_tokens_handles_periods(client):
    res = client.get(f'/api/tokens?str={quote("Chào mẹ.")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['Chào', 'mẹ', '.']


def test_tokens_returns_status_400_given_no_str(client):
    res = client.get(f'/api/tokens')
    assert res.status_code == 400
