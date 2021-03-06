import dataclasses
from pathlib import Path
from unittest.mock import patch

import pytest

from pdoc import extract
from pdoc.doc import Module, Class, Variable
from pdoc.doc_types import empty

here = Path(__file__).parent


def test_repr_tb(monkeypatch):
    m = Module(dataclasses)
    with patch("pdoc.doc._docstr", side_effect=ValueError):
        with pytest.raises(RuntimeError, match="Error in dataclasses's repr!"):
            repr(m)


def test_order():
    m = Module(dataclasses)
    m2 = Module(pytest)
    assert m < m2


def test_attrs():
    mod = extract.load_module(extract.parse_spec(here / "snapshots" / "demo_long.py"))

    m = Module(mod)
    assert m.variables
    assert m.classes
    assert m.functions

    c = m.members["Foo"]
    assert isinstance(c, Class)
    assert c.class_variables
    assert c.instance_variables
    assert c.classmethods
    assert c.staticmethods
    assert c.methods


def test_var_with_raising_repr():
    class Raising:
        def __repr__(self):
            raise RuntimeError

    v = Variable("module", "var", "", ("module", "var"), empty, Raising())
    assert v.default_value_str == " = <unable to get value representation>"
