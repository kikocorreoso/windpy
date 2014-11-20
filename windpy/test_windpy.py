import unittest
import warnings

import pandas as pd
import windpy as w
from windpy.utils import (check_duplicated_timestamps,
                          check_unsorted_timestamps)
from windpy.timeseries import _msg_timestamp, _msg_w

#####################################
# some data to be used in the tests #
#####################################
a_dict = {'c01': [1,2,3], 'c02': [1,2,3], 'c03': [1,2,3], 
          'c04': [1,2,3], 'c05': [1,2,3], 'c06': [1,2,3]}

df_base = pd.DataFrame(a_dict)

class TestTimeSeriesPy(unittest.TestCase):
    """tests for timeseries.py"""
    
    def setUp(self):
        pass
        
    def test_input(self):
        """test_in the input to timeseries.TimeSeries is accepted."""
        
        # test that a no dataframe is not accepted
        self.assertRaises(ValueError, w.timeseries.TimeSeries, a_dict)
        
        # test that if the dataframe doesn't have a timestamp column
        # then a warning will be show
        df = df_base.copy()
        df.columns = ['c01', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        with warnings.catch_warnings(record=True) as warn:
            w.timeseries.TimeSeries(df)
            assert len(warn) == 1
            assert issubclass(warn[-1].category, UserWarning)
            assert _msg_timestamp in str(warn[-1].message)
        
        # test that the timestamps are valid datetime64 dtype
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        df.timestamp = pd.date_range('20000101', '20000103')
        wts = w.timeseries.TimeSeries(df)
        self.assertEqual(wts._has_timestamp, True)
        
        # test wspd column available
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        wts = w.timeseries.TimeSeries(df)
        self.assertEqual(wts._has_wspd, True)
        
        # test exception if wspd column is not in df
        df = df_base.copy()
        df.columns = ['timestamp', 'c02', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        self.assertRaises(ValueError, w.timeseries.TimeSeries, df)
        
        # test wdir column available
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        wts = w.timeseries.TimeSeries(df)
        self.assertEqual(wts._has_wdir, True)
        
        # test warning if wdir column is not in df
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'c03', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        with warnings.catch_warnings(record=True) as warn:
            w.timeseries.TimeSeries(df)
            assert len(warn) == 1
            assert issubclass(warn[-1].category, UserWarning)
            assert _msg_w.format('wdir') in str(warn[-1].message)
        
        # test wspd_min column available
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        wts = w.timeseries.TimeSeries(df)
        self.assertEqual(wts._has_wspd_min, True)
        
        # test warning if wspd_min column is not in df
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wspd', 
                      'c04', 'wspd_max', 'wspd_std']
        with warnings.catch_warnings(record=True) as warn:
            w.timeseries.TimeSeries(df)
            assert len(warn) == 1
            assert issubclass(warn[-1].category, UserWarning)
            assert _msg_w.format('wspd_min') in str(warn[-1].message)
        
        # test wspd_max column available
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        wts = w.timeseries.TimeSeries(df)
        self.assertEqual(wts._has_wspd_max, True)
        
        # test warning if wspd_max column is not in df
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wspd', 
                      'wspd_min', 'c05', 'wspd_std']
        with warnings.catch_warnings(record=True) as warn:
            w.timeseries.TimeSeries(df)
            assert len(warn) == 1
            assert issubclass(warn[-1].category, UserWarning)
            assert _msg_w.format('wspd_max') in str(warn[-1].message)
        
        # test wspd_std column available
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        wts = w.timeseries.TimeSeries(df)
        self.assertEqual(wts._has_wspd_std, True)
        
        # test warning if wspd_std column is not in df
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wspd', 
                      'wspd_min', 'wspd_max', 'c06']
        with warnings.catch_warnings(record=True) as warn:
            w.timeseries.TimeSeries(df)
            assert len(warn) == 1
            assert issubclass(warn[-1].category, UserWarning)
            assert _msg_w.format('wspd_std') in str(warn[-1].message)

class TestSitePy(unittest.TestCase):
    
    def setUp(self):
        pass

class TestTurbinePy(unittest.TestCase):
    
    def setUp(self):
        pass

class TestUtilsPy(unittest.TestCase):
    """tests for utils.py"""
    
    def setUp(self):
        pass
        
    def test_check_duplicated_timestamps(self):
        """test for duplicated timestamps and raises an Exception"""
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        df.timestamp = pd.date_range('20000101', '20000103')
        df.timestamp[2] = pd.datetime(2000, 1, 2)
        self.assertRaises(Exception, check_duplicated_timestamps, df)
    
    def test_check_unsorted_timestamps(self):
        """test for duplicated timestamps and raises an Exception"""
        df = df_base.copy()
        df.columns = ['timestamp', 'wspd', 'wdir', 
                      'wspd_min', 'wspd_max', 'wspd_std']
        df.timestamp = pd.date_range('20000101', '20000103')
        df.timestamp[2] = pd.datetime(1999, 12, 31)
        self.assertRaises(Exception, check_unsorted_timestamps, df)

if __name__ == '__main__':
    unittest.main()
