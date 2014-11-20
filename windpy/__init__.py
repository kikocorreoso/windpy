"""
windpy library
~~~~~~~~~~~~~~

Windpy is a library to work with wind time series and basic wind energy 
related calculations.

Basic usage:
    
    >>> import windpy as w
    >>> wts = w.timeseries.Timeseries(DataFrame)
    >>> print(wts.summary())
    
:copyright: (c) 2014 by Kiko Correoso.
:license: MIT, see LICENSE for more details.
"""

__version__ = "0.0.1"
__author__ = "KikoCorreoso"
__license__ = "MIT"
__copyright__ = 'Copyright 2014 Kiko Correoso'

from . import timeseries
from . import site
from . import turbine
