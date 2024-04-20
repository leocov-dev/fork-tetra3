Development
===========

Getting the source code
-----------------------
To be able to easily download and contribute updates to tetra3 you should install Git. Follow the
instructions for your platform `over here <https://git-scm.com/downloads>`_.

Clone the source code from the `Github repository <https://github.com/esa/tetra3.git>`_::

    git clone https://github.com/esa/tetra3.git

You should see the tetra3 directory created for you with all necessary files. Check the status of
your repository by typing::

    cd tetra3
    git status

which should tell you that you are on the branch "master" and are up to date with the origin (which
is the GitHub version of tetra3). If a new update has come to GitHub you can update yourself by
typing::

    git pull

If you wish to contribute (please do!) and are not familiar with Git and GitHub, start by creating
a user on GitHub and setting you username and email::

    git config --global user.name "your_username_here"
    git config --global user.email "email@domain.com"

You will now also be able to push proposed changes to the software. There are many good resources
for learning about Git, `the documentation <https://git-scm.com/doc>`_ which includes the reference,
a free book on Git, and introductory videos is a good place to start.

Installing Dependencies
-----------------------

Create a local development virtual environment with the utility of your choice.

For example if using pythons "virtual environments" module first switch to this projects repository
root directory::

    cd tetra3

Create a virtual environment directory named `.venv` and activate it::

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
