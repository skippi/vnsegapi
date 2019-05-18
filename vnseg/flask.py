from flask import Flask, request, jsonify


def make_app(test_config=None) -> Flask:
    app = Flask(__name__)
    app.route('/tokenize/')(_tokenize_get)
    app.route('/tokenize/<string:sentence>')(_tokenize_get)
    return app


def _tokenize_get(sentence: str = '') -> str:
    tokens = [] if not sentence else [sentence]
    return jsonify({'tokens': tokens})
