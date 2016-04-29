from read_env import read_env


def test_read_env_traversal():
    mock_environ = {}
    read_env(environ=mock_environ)
    assert mock_environ == {
        'FOO': 'bar',
        'BAZ': '42'
    }
