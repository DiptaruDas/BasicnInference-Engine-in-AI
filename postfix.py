from tokens import *

def convertToPostfix(data):
	def priority(symbol):
		if symbol == "=":return 0
		if symbol == "<->":return 1
		if symbol == "->":return 2
		if symbol == "v":return 3
		if symbol == "^":return 4
		if symbol == "!":return 5
		else:return None

	tokenlist = tokens(data)
#	print("Token list:" +str(tokenlist))
	postlist = []
	stack = []
	for token in tokenlist:
		if token == "(":
			stack.append(token)
		elif token == ")":
			item = stack.pop()
			while item != "(" :
				postlist.append(item)
				item = stack.pop()
		elif token in ["!", "^", "v", "->", "<->", "="]:
			while len(stack)>0 and stack[-1]!="(" and priority(stack[-1])>=priority(token):
				postlist.append(stack.pop())
			stack.append(token)
		else:
			postlist.append(token)
	while len(stack)!=0:
		postlist.append(stack.pop())
#	print("Inside postfix", type(postlist[0]))
	return postlist
