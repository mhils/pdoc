from __future__ import annotations

from typing import Optional

import forwardrefs
from forwardrefs import TurtleAlias1
from forwardrefs import TurtleAlias1 as MoreAlias


def foo(a: forwardrefs.TurtleAlias1):
    """Turtles from another module"""


def bar(a: forwardrefs.TurtleAlias1):
    """More turtles."""


def baz(a: Optional[forwardrefs.TurtleAlias1]):
    """Even more turtles."""


def qux(a: TurtleAlias1):
    """Even more turtles."""


def quux(a: MoreAlias):
    """Even more turtles."""
