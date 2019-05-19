from typing import List

from flask import Flask, request, jsonify
from pyvi import ViTokenizer


def make_app(test_config=None) -> Flask:
    app = Flask(__name__)
    app.route('/api/tokens')(_api_tokens)
    return app


def _api_tokens() -> str:
    string = request.args['str']
    tokens = [] if not string else _tokenize(string)
    return jsonify({'tokens': tokens})


def _tokenize(sentence: str) -> List[str]:
    pyvi_str = ViTokenizer.tokenize(sentence)
    underscore_tokens = pyvi_str.split()
    return [t.replace('_', ' ') for t in underscore_tokens]
