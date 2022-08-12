from __future__ import annotations

import types
import typing
from typing import TypeAlias, Text
import numpy.typing as npt
from pdoc import doc
from pdoc.doc import Module

DocumentedAlias: TypeAlias = int | str
"""An int or a str."""

UndocumentedAlias = int | str


class Foo:
    pass


def foo(
    obj: Foo,
    explicit_alias: DocumentedAlias,
    stdlib_alias: Text,
    stdlib_explicit: typing.Text,
    numpy_monster: npt.ArrayLike,
    numpy_monster2: npt.ArrayLike | None,
    pdoc_ref: doc.Class,
    pdoc_ref2: Module,
    parametrized: doc.Doc[types.ModuleType],
    implicit_alias: UndocumentedAlias,
    mix: DocumentedAlias | UndocumentedAlias,
    simple: str | int,
    simpler: bool,
    literal: typing.Literal["str", "int"],
    new_style_union_with_typing: int | str | typing.Iterable[int | str]
):
    pass
