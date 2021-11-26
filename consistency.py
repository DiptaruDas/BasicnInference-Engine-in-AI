def consistent(knowledge):
	def check(knwoledge, variables, values):
		if(variables is None or len(variables)==0):
			val = knowledge.value(values)
			return [val, val]
		else:
			tempvars = variables.copy()
			nextvar = tempvars.pop()
			values1 = values.copy()
			values2 = values.copy()

			values1[nextvar] = True
			values2[nextvar] = False

			val1 = check(knowledge, tempvars, values1)
			val2 = check(knowledge, tempvars, values2)
			return [val1[0] or val2[0], val1[1] and val2[1]]

#	print (knowledge.variables())
	return check(knowledge, knowledge.variables(), dict())
