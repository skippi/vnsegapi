"""This module implements functions for parsing Vietnamese."""

import re
from typing import List

from pyvi import ViTokenizer


def tokenize(string: str) -> List[str]:
    """Converts a Vietnamese string into its respective tokens."""

    if not string:
        return []

    if not re.search(r"\s|\W", string):
        return [string]

    underscore_tokens = ViTokenizer.tokenize(string).split()
    return [token.replace("_", " ") for token in underscore_tokens]
