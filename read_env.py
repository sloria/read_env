# -*- coding: utf-8 -*-
import re
import shlex
import os
import inspect

__version__ = '1.0.0'

try:
    FileNotFoundError
except NameError:  # Python 2
    FileNotFoundError = IOError

ENV = '.env'

def read_env(path=None, environ=None):
    """Reads a .env file into ``environ`` (which defaults to ``os.environ``).
    If .env is not found in the directory from which this function is called, recurse
    up the directory tree until a .env file is found.
    """
    environ = environ if environ is not None else os.environ

    if path is None:
        frame = inspect.currentframe().f_back
        caller_dir = os.path.dirname(frame.f_code.co_filename)
        path = current = os.path.join(os.path.abspath(caller_dir), ENV)

        pardir = os.path.abspath(os.path.join(current, os.pardir))
        while current != pardir:
            target = os.path.join(current, ENV)
            if os.path.exists(target):
                path = os.path.abspath(target)
                break
            else:
                current = os.path.abspath(os.path.join(current, os.pardir))
                pardir = os.path.abspath(os.path.join(current, os.pardir))
        if not path:
            raise FileNotFoundError('Could not find a .env file')

    with open(path, 'r') as fp:
        content = fp.read()
    parsed = parse_env(content)
    for key, value in parsed.items():
        environ.setdefault(key, value)

_ITEM_RE = re.compile(r'[A-Za-z_][A-Za-z_0-9]*')
# From Honcho. See NOTICE file for license details.
def parse_env(content):
    """Parse the content of a .env file (a line-delimited KEY=value format) into a
    dictionary mapping keys to values.
    """
    values = {}
    for line in content.splitlines():
        lexer = shlex.shlex(line, posix=True)
        tokens = list(lexer)

        # parses the assignment statement
        if len(tokens) < 3:
            continue

        name, op = tokens[:2]
        value = ''.join(tokens[2:])

        if op != '=':
            continue
        if not _ITEM_RE.match(name):
            continue

        value = value.replace(r'\n', '\n')
        value = value.replace(r'\t', '\t')
        values[name] = value
    return values
