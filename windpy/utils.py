"""
utils.py module to help with some operations
"""

def check_duplicated_timestamps(data):
    """Check if a dataframe with a 'timestamp' column have duplicated timestamps"""
    res = data.timestamp[data.timestamp.duplicated()]
    if res.shape[0] > 0:
        raise Exception("""
There are duplicated timestamps. This could lead to ambiguous results.
Please, check your input.
Duplicated values:
        """ + res.__repr__())
        
def check_unsorted_timestamps(data):
    """Chack if the timestamps are not ordered"""
    if not any(data.sort('timestamp').timestamp == data.timestamp):
        raise Exception("""
The timestamps are not sorted. This could lead to ambiguous results.
Please, check your input.
        """)
