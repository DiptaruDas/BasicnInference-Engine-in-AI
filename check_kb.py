def check_kb(kBase, query, variables, values):
	if(variables is None or len(variables) == 0):
		if(kBase.value(values) is True):
			return query.value(values)
		return True

	tempvars = variables.copy()
	nextvar = tempvars.pop()
	values1 = values.copy()
	values2 = values.copy()

	values1[nextvar] = True
	values2[nextvar] = False

	return (check_kb(kBase, query, tempvars, values1) and check_kb(kBase, query, tempvars, values2))
