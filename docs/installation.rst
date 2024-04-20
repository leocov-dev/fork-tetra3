Installation
============

Getting Python
--------------
tetra3 is written for Python 3.7 or later (and therefore runs on almost any platform) and should
work with most modern Python 3 installations. There are many ways to get Python on your system.
Most easily, by going to `the python webiste <https://www.python.org/>`_ and selecting your
platform. On many operating systems Python is installed by default, but this can be a very old
version (often 2.7). Check if you have something installed by running ``python --version`` in a
command prompt or terminal window. You can also check ``python3 --version`` as it is sometimes
installed under this name. In the latter case, use ``python3`` and ``pip3`` in place of ``python``
and ``pip`` in these instructions.

Getting tetra3
--------------
tetra3 is available on PyPI (the Python Package Index).
Install into your project like::

    pip install tetra3



You can test that it works by running the example provided in the GitHub repo.

Manually download source code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to `the GitHub repository <https://github.com/esa/tetra3>`_, click `Clone or Download` and
`Download ZIP` and extract the tetra3 directory to where you want to use it. You can put this
directly in your Python project as a module and use, or see below for how to install it.

Installing from source
^^^^^^^^^^^^^^^^^^^^^^
To install the package from source, open a command prompt or terminal in the tetra3 directory and
run::

    pip install .
    
This will install all dependencies and make the tetra3 module accessible from anywhere. You can
test that it works by running the example::

    cd examples
    python test_tetra3.py
    
which should print out the solutions for the included test images.

Using tetra3 as a module in your repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A specific branch named `no_big_files` is available for practical inclusion as a git submodule
in your own repository. This does not include the default database and example images, making
it less than 1 MB. For a specific application you probably want a custom database anyway.

If problems arise
-----------------
Please get in touch by `filing an issue <https://github.com/esa/tetra3/issues>`_.