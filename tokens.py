def tokens(data):
	datalist = []
	index = 0
	i = 0
	while i<len(data):
		if data[i] == "(":
			datalist.append("(")
			index = i+1
		elif data[i] == ")":
			item = data[index:i]
			if len(item)>0:
				datalist.append(item)
			datalist.append(")")
			index = i+1
		elif data[i] == "=":
			item = data[index:i]
			if len(item)>0:
				datalist.append(item)
			datalist.append("=")
			index = i+1
		elif data[i] == "!":
			datalist.append("!")
			index = i+1
		elif data[i] in ["^", "v"]:
			item = data[index:i]
			if len(item)>0:
				datalist.append(item)
			datalist.append(str(data[i]))
			index = i+1
		elif data[i:i+2] == "->":
			item = data[index:i]
			if len(item)>0:
				datalist.append(item)
			datalist.append(data[i:i+2])
			index = i+2
			i+=1
		elif data[i:i+3] == "<->":
			item = data[index:i]
			if len(item)>0:
				datalist.append(item)
			datalist.append(data[i:i+3])
			index = i+3
			i+=2
		i+=1
	item = data[index:i]
	if len(item)>0:datalist.append(item)
	return datalist
