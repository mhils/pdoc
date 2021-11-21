import abc
from functools import lru_cache
from typing import Generic
from typing import TypeVar

from pdoc._compat import cached_property


# https://github.com/mitmproxy/pdoc/issues/226


class Descriptor:
    def __init__(self, func):
        self.__doc__ = func.__doc__

    def __get__(self, instance, owner):
        return self if instance is None else getattr(instance, "_x", 0)

    def __set__(self, instance, value):
        instance._x = value


class Issue226:
    @Descriptor
    def size(self):
        """This is the size"""


# Testing function and object default values


def default_func():
    pass


default_obj = object()

var_with_default_obj = default_obj
"""this shouldn't render the object address"""
var_with_default_func = default_func
"""this just render like a normal function"""


def func_with_defaults(a=default_obj, b=default_func):
    """this shouldn't render object or function addresses"""
    pass


# Testing classmethod links in code
class ClassmethodLink:
    """
    You can either do

    >>> ClassmethodLink.bar()
    42

    or

    ```python
    ClassmethodLink.bar()
    ```

    neither will be linked.
    """

    @classmethod
    def bar(cls):
        return 42


# Testing generic bases

T = TypeVar("T")


class GenericParent(Generic[T]):
    pass


class NonGenericChild(GenericParent[str]):
    pass


# Testing docstring inheritance


class Base:
    def __init__(self):
        """init"""
        super().__init__()

    def foo(self):
        """foo"""
        pass

    @classmethod
    def bar(cls):
        """bar"""
        pass

    @staticmethod
    def baz():
        """baz"""
        pass

    @property
    def qux(self):
        """qux"""
        return

    # This is not supported by inspect.getdoc yet.
    @cached_property
    def quux(self):
        """quux"""
        return

    quuux: int = 42
    """quuux"""


class Child(Base):
    def __init__(self):
        super().__init__()

    def foo(self):
        pass

    @classmethod
    def bar(cls):
        pass

    @staticmethod
    def baz():
        pass

    @property
    def qux(self):
        return

    @cached_property
    def quux(self):
        return

    quuux: int = 42


# Testing that an attribute that is only annotated does not trigger a "submodule not found" warning.

only_annotated: int


# Testing that Exceptions render properly


class CustomException(RuntimeError):
    """custom exception type"""


# Testing that a private class in __all__ is displayed


class _Private:
    """private class"""

    pass

    def _do(self):
        """private method"""


# Testing a class attribute that is a lambda (which generates quirky sources)


class LambdaAttr:
    # not really supported, but also shouldn't crash.
    attr = lambda x: 42  # noqa


# Testing different docstring annotations
# fmt: off


def foo():
    """no indents"""


def bar():
    """no
indents"""


def baz():
    """one
    indent"""


def qux():
    """
    two
    indents
    """


class Indented:
    def foo(self):
        """no indents"""

    def bar(self):
        """no
indents"""

    def baz(self):
        """one
        indent"""

    def qux(self):
        """
        two
        indents
        """

    @lru_cache()
    def foo_decorated(self):
        """no indents"""

    @lru_cache()
    # comment
    def foo_commented(self):
        """no indents"""

    @lru_cache()
    def bar_decorated(self):
        """no
indents"""

    @lru_cache()
    def baz_decorated(self):
        """one
        indent"""

    @lru_cache()
    def qux_decorated(self):
        """
        two
        indents
        """

    @lru_cache(
        maxsize=42
    )
    def quux_decorated(self):
        """multi-line decorator, https://github.com/mitmproxy/pdoc/issues/246"""


def _protected_decorator(f):
    return f


@_protected_decorator
def fun_with_protected_decorator():
    """This function has a protected decorator (name starting with a single `_`)."""


class UnhashableDataDescriptor:
    def __get__(self):
        pass
    __hash__ = None  # type: ignore


unhashable = UnhashableDataDescriptor()


class AbstractClass(metaclass=abc.ABCMeta):
    """This class shouldn't show a constructor as it's abstract."""
    @abc.abstractmethod
    def foo(self):
        pass


__all__ = [  # noqa
    "Issue226",
    "var_with_default_obj",
    "var_with_default_func",
    "func_with_defaults",
    "ClassmethodLink",
    "GenericParent",
    "NonGenericChild",
    "Child",
    "only_annotated",
    "CustomException",
    "_Private",
    "LambdaAttr",
    "foo",
    "bar",
    "baz",
    "qux",
    "Indented",
    "fun_with_protected_decorator",
    "unhashable",
    "AbstractClass",
]
