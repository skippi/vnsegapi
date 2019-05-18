import json
from urllib.parse import quote

import pytest
from vnseg.flask import make_app


_test_app = make_app()
_test_app.testing = True


@pytest.fixture
def client():
    return _test_app.test_client()


def test_tokenize_get_given_empty_sentence(client):
    res = client.get('/')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == []


def test_tokenize_get_given_one_word_sentence(client):
    res = client.get(f'/{quote("táo")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['táo']


def test_tokenize_get_given_two_words_each_as_tokens(client):
    res = client.get(f'/{quote("táo cao")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['táo', 'cao']


def test_tokenize_get_given_many_words_three_tokens(client):
    res = client.get(f'/{quote("Đây là từ điển")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['Đây', 'là', 'từ điển']


def test_tokenize_get_handles_periods(client):
    res = client.get(f'/{quote("Chào mẹ.")}')
    get_result = json.loads(res.data)
    assert get_result['tokens'] == ['Chào', 'mẹ', '.']
