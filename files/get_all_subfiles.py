"""
"""
def function(directory):
	"""
	"""
	all_subfiles = []
	import os
	for root, subfolders, files in os.walk(directory):
		for file in files:
			file_path = os.path.join(root, file)
			all_subfiles += [file_path]
		for subfolder in subfolders:
			all_subfiles += function(subfolder)
	return all_subfiles