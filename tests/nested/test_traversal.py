# -*- coding: utf-8 -*-
import os

import pytest

from read_env import read_env

try:
    FileNotFoundError
except NameError:  # Python 2
    FileNotFoundError = IOError

HERE = os.path.abspath(os.path.dirname(__file__))

def test_read_env_traversal():
    mock_environ = {}
    read_env(environ=mock_environ)
    assert mock_environ == {
        'FOO': 'bar',
        'BAZ': '42'
    }

def test_recurse_with_directory_passed():
    mock_environ = {}
    read_env(path=HERE, environ=mock_environ, recurse=True)
    assert mock_environ == {
        'FOO': 'bar',
        'BAZ': '42'
    }

def test_recurse_with_filepath_passed_and_file_doesnt_exist():
    mock_environ = {}
    path = os.path.join(HERE, '.env')
    read_env(path=path, environ=mock_environ, recurse=True)
    assert mock_environ == {
        'FOO': 'bar',
        'BAZ': '42'
    }

def test_recurse_with_filepath_passed_and_file_exists():
    mock_environ = {}
    path = os.path.join(HERE, os.pardir, '.env')
    read_env(path=path, environ=mock_environ, recurse=True)
    assert mock_environ == {
        'FOO': 'bar',
        'BAZ': '42'
    }

def test_recurse_false():
    with pytest.raises(FileNotFoundError):
        read_env(recurse=False)
