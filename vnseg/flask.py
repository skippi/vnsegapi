from typing import List

from flask import Flask, request, jsonify
from pyvi import ViTokenizer


def make_app(test_config=None) -> Flask:
    app = Flask(__name__)
    app.route('/')(_endpoint_tokenize_get)
    app.route('/<string:sentence>')(_endpoint_tokenize_get)
    return app


def _endpoint_tokenize_get(sentence: str = '') -> str:
    tokens = [] if not sentence else _tokenize(sentence)
    return jsonify({'tokens': tokens})


def _tokenize(sentence: str) -> List[str]:
    pyvi_str = ViTokenizer.tokenize(sentence)
    underscore_tokens = pyvi_str.split()
    return [t.replace('_', ' ') for t in underscore_tokens]
