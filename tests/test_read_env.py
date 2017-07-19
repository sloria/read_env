# -*- coding: utf-8 -*-
from read_env import parse_env, read_env

content = '''
ignorethis
# just a comment
FOO=bar
BAZ='qux'
WOO=42
WAT=wher,wen,wy
'''

def test_parse_env():
    assert parse_env(content) == {
        'FOO': 'bar',
        'WOO': '42',
        'WAT': 'wher,wen,wy',
        'BAZ': 'qux'
    }

def test_read_env():
    mock_environ = {}
    read_env(environ=mock_environ)
    assert mock_environ == {
        'FOO': 'bar',
        'BAZ': '42',
        'POO': '💩'
    }
