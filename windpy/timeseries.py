import warnings
warnings.simplefilter('always', UserWarning)

import pandas as pd
import numpy as np

from .utils import (check_duplicated_timestamps,
                    check_unsorted_timestamps,
                    get_frequency)

_msg_timestamp = """
'timestamp' column is not available or not understood. Some operations 
related with time operations could not be performed.
"""

_msg_w = """
'{0}' column is not available. Operations that requires {0}
could not be performed and an Exception will be raised.
"""

class TimeSeries:
    def __init__(self, data, height = 10):
        self.data = data            
        self._has_timestamp = False
        self._has_wspd = False
        self._has_wdir = False
        self._has_wspd_min = False
        self._has_wspd_max = False
        self._has_wspd_std = False
        self._check_input_data()
        self.height = height
        
        
    def _check_input_data(self):
        try:
            _cols = self.data.columns
        except:
            raise ValueError('Only Pandas DataFrames are accepted')
        
        if 'wspd' in _cols:
            self._has_wspd = True
        else:
            raise ValueError("""No 'wspd' column available.""")
        
        if 'timestamp' in _cols:
            if self.data.timestamp.dtype == "datetime64[ns]":
                check_duplicated_timestamps(self.data)
                check_unsorted_timestamps(self.data)
                self._has_timestamp = True
                self.freq = get_frequency(self.data)
                self.date_start = self.data.timestamp.min()
                self.date_end = self.data.timestamp.max()
                rango = pd.Timedelta(self.date_end - self.date_start)
                self.possible_values = rango / self.freq + 1
            else:
                warnings.warn(_msg_timestamp, UserWarning)
        else:
            warnings.warn(_msg_timestamp, UserWarning)

        if 'wdir' in _cols:
            self._has_wdir = True
        else:
            warnings.warn(_msg_w.format('wdir'), UserWarning)
            
        if 'wspd_min' in _cols:
            self._has_wspd_min = True
        else:
            warnings.warn(_msg_w.format('wspd_min'), UserWarning)
        
        if 'wspd_max' in _cols:
            self._has_wspd_max = True
        else:
            warnings.warn(_msg_w.format('wspd_max'), UserWarning)
        
        if 'wspd_std' in _cols:
            self._has_wspd_std = True
        else:
            warnings.warn(_msg_w.format('wspd_std'), UserWarning)
        
    def mean_wspd(self):
        return self.data.wspd.mean()
    
    def weibull_params(self, method = "MLE", date_start = None, date_end = None):
        pass
    
