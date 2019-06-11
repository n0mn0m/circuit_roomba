.. role:: bash(code)
   :language: bash

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

Installing from PyPI for blinka boards
--------------------------------------

.. code-block:: shell

    pip install circuitroomba

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip install circuitroomba

For CircuitPython  boards that don't support :bash:`blinka` copy :bash:`/circuitroomba` from :bash:`/src` to
:bash:`/lib` on the CircuitPython board. :bash:`make install` has been setup as a helper, but you may need
to update the :bash:`/Volume` path for your system and board name.

.. code-block:: shell

    make install

Usage Example
=============

.. code-block:: python

    import board
    import digitalio
    import time
    from circuitroomba.series6 import roomba

    __repo__ = "https://github.com/AlexanderHagerman/circuitroomba.git"

    # initialize roomba
    bot = roomba.Commands(board.TX, board.RX, digitalio.DigitalInOut(board.A1))

    # wake roomba from sleep mode
    bot.wake_up()

    # CircuitPython loop
    while True:
        # send commands
        bot.start()
        bot.safe()
        bot.clean()

        time.sleep(2)

        bot.power()
        bot.stop()

        break

More examples are available in :bash:`/examples`.


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

This will output the documentation to :bash:`docs/_build/html`. Open the ``index.html`` in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.

Images
======

.. image:: https://drive.google.com/open?id=1KtG_M6wwwOtODZrK1ZTnyX92WZUBcyOU
   :target: https://drive.google.com/open?id=1KtG_M6wwwOtODZrK1ZTnyX92WZUBcyOU
   :alt: circuit roomba high level

.. image:: https://drive.google.com/open?id=1GCv2tUK9gy0zGXF1X7UAJXt-FR0cVhlm
   :target: https://drive.google.com/open?id=1GCv2tUK9gy0zGXF1X7UAJXt-FR0cVhlm
   :alt: circuit roomba running video

.. image:: https://drive.google.com/open?id=1Um1UUVvmV5FkCiyP8SBmEOifm1huh9Bm
   :target: https://drive.google.com/open?id=1Um1UUVvmV5FkCiyP8SBmEOifm1huh9Bm
   :alt: roomba open interface connections

.. image:: https://drive.google.com/open?id=1goaZUGYlUYxY0_c_kZM8E3LHNcuu2lPR
   :target: https://drive.google.com/open?id=1goaZUGYlUYxY0_c_kZM8E3LHNcuu2lPR
   :alt: circuit playground connections

.. image:: https://drive.google.com/open?id=1YYps3UBBO7gMA1RfhlnACCx4bNVq-io_
   :target: https://drive.google.com/open?id=1YYps3UBBO7gMA1RfhlnACCx4bNVq-io_
   :alt: circuit playground connected to roomba
