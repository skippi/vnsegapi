import json
from urllib.parse import quote

import pytest
from vnseg.flask import make_app


_test_app = make_app()
_test_app.testing = True


@pytest.fixture
def client():
    return _test_app.test_client()


def test_tokenize_given_empty_sentence(client):
    res = client.get('/api/tokenize?str=')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == []


def test_tokenize_given_one_word_sentence(client):
    res = client.get(f'/api/tokenize?str={quote("táo")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['táo']


def test_tokenize_given_two_words_each_as_tokens(client):
    res = client.get(f'/api/tokenize?str={quote("táo cao")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['táo', 'cao']


def test_tokenize_given_many_words_three_tokens(client):
    res = client.get(f'/api/tokenize?str={quote("Đây là từ điển")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['Đây', 'là', 'từ điển']


def test_tokenize_handles_periods(client):
    res = client.get(f'/api/tokenize?str={quote("Chào mẹ.")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['Chào', 'mẹ', '.']


def test_tokenize_returns_status_400_given_no_str(client):
    res = client.get(f'/api/tokenize')
    assert res.status_code == 400
