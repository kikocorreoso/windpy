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
