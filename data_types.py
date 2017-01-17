def data_type(data):
	if type(data) == None:
		return "No value"
	elif type(data) == str:
		return len(data)
	elif type(data) == bool:
		return data
	elif type(data) == int:
		if data == 100:
			return "Equal to 100"
		elif data < 100:
			return "Less than 100"
		else:
			return "More than 100"
	elif type(data) == list:
		if len(data)< 3:
			return None
		else:
			return data[2]






	