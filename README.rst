Synapse SNAPpy library for HX711 Load Cell Amplifier/ADC
========================================================

``snappy-hx711`` is a SNAPpy library that reads values from the
HX711 24-bit ADC with amplifier designed to measure load cells.

Installation
------------

For use in Portal
~~~~~~~~~~~~~~~~~

Download and extract the latest release zip file to Portal’s
``snappyImages`` directory. By default, this is located at
``...\Documents\Portal\snappyImages`` on Windows.

For use with SNAPbuild/SNAPtoolbelt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The easiest way to install ``snappy-hx711`` for use with SNAPbuild
or SNAPtoolbelt is using `pip`_::

    pip install snappy-hx711

Alternatively you can download the source, extract it, and install it::

    python setup.py install

Usage
-----

To use the ``snappy-hx711`` library functions, first import the
library and call `hx711_begin()` with the pin numbers connected to the
HX711. Then you can start taking measurements:

.. code:: python

    from snappy_hx711 import *

    CLOCK_PIN = 6
    DATA_PIN = 7

    @setHook(HOOK_INIT)
    def init():
        # Must be called before making measurements:
        hx711_begin(CLOCK_PIN, DATA_PIN)

    def take_a_measurement():
        # Returns a 3-byte string:
        return hx711_read()


.. _pip: https://pip.pypa.io/en/latest/installing.html