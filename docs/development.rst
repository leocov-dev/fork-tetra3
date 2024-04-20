Development
===========

Getting the source code
-----------------------

Clone the source code from the `Github repository <https://github.com/esa/tetra3.git>`_::

    cd ~/src
    git clone https://github.com/esa/tetra3.git
    cd tetra3

Installing Dependencies
-----------------------

Create a local development virtual environment with the utility of your choice.

For example from within the ``tetra3`` directory::

    pyenv local 3.7
    python -m venv .venv
    source .venv/bin/activate

Install the project and development dependencies::

    pip install -e ".[dev]"

If you wish to be able to build the documentation please include that optional group::

    pip install -e ".[dev,docs]"


Running Tests
-------------

Tests are written with the ``pytest`` testing framework.

Run unit tests::

    pytest

Building Documentation
----------------------

Documentation is configured and generated using Sphynx.

From the repository root run::

    cd docs && make html && cd ..

This will create a directory ``docs/_build/`` with the generated files.
