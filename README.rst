********
read_env
********

.. image:: https://badge.fury.io/py/read_env.svg
    :target: http://badge.fury.io/py/read_env
    :alt: Latest version

.. image:: https://travis-ci.org/sloria/read_env.svg?branch=master
    :target: https://travis-ci.org/sloria/read_env
    :alt: Travis-CI


read_env reads .env.

Install
-------
::

    pip install read_env

Usage
-----

Add variables to a ``.env`` file in your project.

.. code-block:: bash

    # myapp/.env
    DEBUG=true
    PORT=5000

Call ``read_env`` to add the variables to ``os.environ``.

.. code-block:: python

    # myapp/env.py
    import os
    from read_env import read_env

    read_env()

    assert os.environ['DEBUG'] == 'true'
    assert int(os.environ['PORT']) == 5000

Related Projects
----------------

Check out `environs <https://github.com/sloria/environs>`_ for parsing environment variables.

License
-------

MIT
