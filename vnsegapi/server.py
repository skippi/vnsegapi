"""This module provides the primary vnsegapi server."""

from typing import List

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

    tokens = [] if not string else parse.tokenize(string)
    return jsonify(tokens)
