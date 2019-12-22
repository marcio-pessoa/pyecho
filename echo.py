"""
---
name: echo.py
description: Echo package
levels:
    0 Quiet (no messages)
    1 Errors
    2 Warnings
    3 Info (all messages)
    4 Device code running
copyright: 2017-2019 Marcio Pessoa
people:
  developers:
  - name: Marcio Pessoa
    email: marcio.pessoa@gmail.com
change-log: Check README.md file.
"""

import sys
from termcolor import cprint

INDENT_WIDTH = 4


class Echo:
    """
    description:
    """

    _version = 0.3
    __header = False
    __level = 1

    @classmethod
    def level(cls, verbosity=None):
        """
        description:
        """
        if verbosity is None:
            return int(cls.__level)
        cls.__level = verbosity
        return False

    @classmethod
    def header(cls, state=None):
        """
        description:
        """
        if state is None:
            return cls.__header
        cls.__header = state
        return False

    @classmethod
    def echo(cls, string, verbosity, indent=0):
        """
        description:
        """
        preffix = ''
        for _ in range(indent * INDENT_WIDTH):
            preffix += ' '
        cls.__print(preffix + string, verbosity, '')

    @classmethod
    def echoln(cls, string, verbosity, indent=0):
        """
        description:
        """
        preffix = ''
        for _ in range(indent * INDENT_WIDTH):
            preffix += ' '
        cls.__print(preffix + string, verbosity, '\n')

    @classmethod
    def __print(cls, string, verbosity, trailer):
        """
        description:
        """
        if int(verbosity) <= int(cls.__level):
            print(string, end=trailer)
            sys.stdout.flush()


def header(state=None):
    """
    description:
    """
    return Echo.header(state)


def level(verbosity=None):
    """
    description:
    """
    return Echo.level(verbosity)


def echo(string, indent=0):
    """
    description:
    """
    Echo.echo(string, 0, indent)


def echoln(string, indent=0):
    """
    description:
    """
    Echo.echoln(string, 0, indent)


def erro(string, indent=0):
    """
    description:
    """
    if Echo.header():
        string = 'Error: ' + string
    Echo.echo(string, 1, indent)


def erroln(string, indent=0):
    """
    description:
    """
    if Echo.header():
        string = 'Error: ' + string
    Echo.echoln(string, 1, indent)


def warn(string, indent=0):
    """
    description:
    """
    if Echo.header():
        string = 'Warning: ' + string
    Echo.echo(string, 2, indent)


def warnln(string, indent=0):
    """
    description:
    """
    if Echo.header():
        string = 'Warning: ' + string
    Echo.echoln(string, 2, indent)


def info(string, indent=0):
    """
    description:
    """
    Echo.echo(string, 3, indent)


def infoln(string, indent=0):
    """
    description:
    """
    Echo.echoln(string, 3, indent)


def debug(string, indent=0):
    """
    description:
    """
    Echo.echo(string, 4, indent)


def debugln(string, indent=0):
    """
    description:
    """
    Echo.echoln(string, 4, indent)


def code(string, color=None, attrs=None):
    """
    description:
    """
    if level() < 4:
        return False
    if color is None:
        color = 'blue'
    if attrs is None:
        attrs = []
    cprint(string, color, attrs=attrs, end='')
    sys.stdout.flush()
    return False


def codeln(string, color=None, attrs=None):
    """
    description:
    """
    code(string + '\n', color, attrs)
