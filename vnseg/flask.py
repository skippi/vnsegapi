from flask import Flask, request, jsonify


def make_app(test_config=None) -> Flask:
    app = Flask(__name__)
    app.route('/')(_tokenize_get)
    app.route('/<string:sentence>')(_tokenize_get)
    return app


def _tokenize_get(sentence: str = '') -> str:
    tokens = [] if not sentence else sentence.split()
    return jsonify({'tokens': tokens})
