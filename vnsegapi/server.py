"""This module provides the primary vnsegapi server."""

from flask import Flask, abort, jsonify, request
from vnsegapi import parse


def make_app() -> Flask:
    """Returns a new vnsegapi server."""

    app = Flask(__name__)
    app.route("/api/tokens")(_api_tokens)
    return app


def _api_tokens() -> str:
    string = request.args["str"]
    if len(string) > 250:
        abort(400)

    return jsonify(parse.tokenize(string))
