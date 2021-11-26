from propositional_logic import *
from postfix import *

def parse(data):
	if data is None or not len(data):
		return None

	data = convertToPostfix(data)
	if data is None:
		return None
#	print(data)
#	print(type(data[0]))
	stack = []
	for item in data:
		if item == "!":
			variable = stack.pop()
#			print(type(variable))
			stack.append(Not(variable))
		elif item == "^":
			variable2 = stack.pop()
			variable1= stack.pop()
			stack.append(And(variable1, variable2))
		elif item == "v":
			variable2 = stack.pop()
			variable1 = stack.pop()
			stack.append(Or(variable1, variable2))
		elif item == "->":
			variable2 = stack.pop()
			variable1 = stack.pop()
			stack.append(Implication(variable1, variable2))
		elif item == "<->":
			variable2 = stack.pop()
			variable1 = stack.pop()
			stack.append(Bicondition(variable1, variable2))
		elif item == "=":
			variable2 = stack.pop()
			variable1 = stack.pop()
			stack.append(Equivalent(variable1, variable2))
		else:
			stack.append(Variable(item))
#	print (stack[0])
	return stack.pop()
