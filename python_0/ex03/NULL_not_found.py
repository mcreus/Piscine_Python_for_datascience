def NULL_not_found(obj: any) -> int:
	try:
		if obj is None:
			print("Nothing: None <class 'NoneType'>")
			return 0
	except:
		pass
	try:
		if obj != obj:
			print("Cheese: nan <class 'float'>")
			return 0
	except:
		pass
	try:
		if not obj and obj is False:
			print("Fake: False <class 'bool'>")
			return 0
	except:
		pass
	try:
		if obj + 1 == 1:
			print("Zero: 0 <class 'int'>")
			return 0
	except:
		pass
	try:
		if len(obj) == 0:
			print("Empty: <class 'str'>")
			return 0
	except:
		pass
	print("Type not Found")
	return 1