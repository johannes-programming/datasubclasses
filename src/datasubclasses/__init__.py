import functools
from dataclasses import dataclass
from typing import *

__all__ = ["decorator", "init", "tool"]


def decorator(args: Iterable, cls: type, /, **kwargs) -> type:
    cargo = dict()
    for x in args:
        cargo[x] = getattr(cls, x)
        delattr(cls, x)
    cls = dataclass(cls, **kwargs)
    print(cargo)
    cls = type(cls.__name__, (cls,), cargo)
    return cls


def init(**kwargs) -> type:
    return tool("__init__", **kwargs)


def tool(*args, **kwargs) -> type:
    return functools.partial(
        decorator,
        args,
        **kwargs,
    )
