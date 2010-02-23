# encoding: utf-8

"""Exceptions that can be raised by the dependancy graph generator."""


__all__ = ['CyclicDependancyError']


class CyclicDependancyError(Exception):
    """Cyclic dependancy error."""
    pass
