from __future__ import annotations

import typing
from typing import TYPE_CHECKING

if typing.TYPE_CHECKING:
    from collections import Counter

if TYPE_CHECKING:
    from collections import ChainMap


def foo(a: Counter[str], b: ChainMap[str, str]):
    pass
