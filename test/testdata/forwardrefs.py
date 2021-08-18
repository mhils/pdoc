from __future__ import annotations

import typing

if typing.TYPE_CHECKING:
    import turtle
    from turtle import Turtle


def fun(arg: turtle.Turtle, arg2: Turtle) -> None:
    """turtles all the way down"""
    local_var: typing.Optional[turtle.TurtleScreen] = None


TurtleAlias1: typing.TypeAlias = "Turtle"
"""An alias for turtles"""

TurtleAlias2 = "turtle.Turtle"
"""Another alias for turtles"""


def alias1(x: TurtleAlias1):
    """A function with the first alias."""


def alias2(x: TurtleAlias2):
    """A function with the second alias."""
