Introduction
============

.. image:: https://codecov.io/gl/AlexanderHagerman/circuitroomba/branch/master/graph/badge.svg
    :target: https://codecov.io/gl/AlexanderHagerman/circuitroomba
    :alt: Coverage Report

.. image:: https://readthedocs.org/projects/circuitroomba/badge/?version=latest
    :target: https://circuitroomba.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://gitlab.com/AlexanderHagerman/circuitroomba/badges/master/pipeline.svg
    :target: https://gitlab.com/AlexanderHagerman/circuitroomba/commits/master
    :alt: Build Status

CircuitRoomba is a CircuitPython library for interfacing with Roomba Open Interface devices.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------

.. code-block:: shell

    pip install circuitroomba


To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip install circuitroomba

Usage Example
=============

.. code-block:: python

    import board
    import digitalio
    from circuitroomba import series6

    brc = digitalio.DigitalInOut(board.A1)

    # Setup the interface
    roomba = series6.Roomba(board.TX, board.RX, brc)

    # Wake the roomba up
    roomba.wake_up()

    # Per the OI doc start must be the first command
    roomba.start()

    # Issue the rest of our commands
    roomba.safe()
    roomba.clean()
    roomba.power()
    roomba.stop()

Additional examples can be found in `examples`.


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/AlexHagerman/CircuitPython_circuitroomba/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.


Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
