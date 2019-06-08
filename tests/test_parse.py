import re

from hypothesis import given, example
from hypothesis.strategies import characters, text
from vnsegapi.parse import tokenize


def test_tokenize_returns_empty_list_given_empty_string():
    assert tokenize("") == []


@given(
    string=text(
        alphabet=characters(whitelist_categories=["Lu", "Ll", "Lm"]), min_size=1
    )
)
def test_tokenize_returns_same_word_given_one_word(string: str):
    assert tokenize(string) == [string]


def test_tokenize_returns_two_tokens_given_two_words():
    assert tokenize("táo cao") == ["táo", "cao"]


def test_tokenize_returns_one_token_given_two_words():
    assert tokenize("từ điển") == ["từ điển"]


def test_tokenize_can_tokenize_complex_sentences():
    assert tokenize("Đây là từ điển") == ["Đây", "là", "từ điển"]


@given(string=text())
def test_tokenize_splits_periods(string: str):
    period_separated = re.split(r"(\.)", string)
    tokens = [token for splits in period_separated for token in tokenize(splits)]
    assert tokenize(string) == tokens


@given(string=text())
def test_tokenize_ignores_extra_whitespace(string: str):
    assert tokenize(string) == tokenize(string.strip())
