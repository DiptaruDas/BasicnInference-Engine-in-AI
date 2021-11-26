import itertools

class Sentence():
	def variables(self):
		return set()
	def value(self, model):
		raise Exception("Empty Sentence")
	def validate(sentence):
		if(isinstance(sentence, Sentence) is not True):
			raise TypeError("This is not a valid logical sentence")
	def __isBalanced(self, sentence):
		parenCnt = 0
		for ch in sentence:
			if(ch == '('): parenCnt+=1
			elif(ch == ')' and parenCnt<=0): return False
			else: parenCnt-=1
		return (parenCnt == 0)
	def __str__(self):
		return ""
	def parenthesize(sentence):
		if(len(sentence) in [0,1] or (sentence[0]=='(' and sentence[-1]==')')):
			return sentence
		return f"({sentence})"

class Variable(Sentence):
	def __init__(self, symbol):
		self.symbol = symbol
	def __eq__(self, sentence):
		return(isinstance(sentence, Variable) and self.symbol == sentence.symbol)
	def __str__(self):
		return self.symbol
	def __repr__(self):
		return  self.symbol
	def value(self, model):
		return bool(model[self.symbol])
	def variables(self):
		return {self.symbol}
class Not(Sentence):
	def __init__(self, operand):
		Sentence.validate(operand)
		self.operand = operand
	def __eq__(self, sentence):
		return (isinstance(sentence, Not) and self.operand == sentence.operand)
	def __repr__(self):
		return f"Not({self.operand})"
	def __str__(self):
		return "!"+Sentence.parenthesize(str(self.operand))
	def variables(self):
		return self.operand.variables()
	def value(self,model):
		return (not self.operand.value(model))
class And(Sentence):
	def __init__(self, *operand):
		self.operand = []
		for item in operand:
			Sentence.validate(item)
			self.operand.append(item)
	def __eq__(self, sentence):
		return (isinstance(sentence, And) and self.operand == sentence.operand)
	def __repr__(self):
		temp = ",".join([str(item)for item in self.operand])
		return "And("+temp+")"
	def __str__(self):
		if(len(self.operand) == 1):
			return str(self.operand[0])
		return "^".join([Sentence.parenthesize(str(item)) for item in self.operand])
	def add(self, operand):
		Sentence.validate(operand)
		self.operand.append(operand)
	def variables(self):
		return set.union(*[item.variables() for item in self.operand])
	def value(self, model):
		return all(item.value(model) for item in self.operand)

class Or(Sentence):
	def __init__(self, *operand):
		self.operand=[]
		for item in operand:
			Sentence.validate(item)
			self.operand.append(item)
	def __eq__(self, sentence):
		return (isinstance(sentence, Or) and self.operand == sentence.operand)
	def __repr__(self):
		temp = ",".join([Sentence.parenthesize(str(item)) for item in self.operand])
		return "Or("+temp+")"
	def __str__(self):
		if(len(self.operand) == 1):
			return str(self.operand[0])
		return "v".join([Sentence.parenthesize(str(item)) for item in self.operand])
	def add(self, operand):
		Sentence.validate(operand)
		self.operand.append(operand)
	def variables(self):
		return set.union(*[item.variables() for item in self.operand])
	def value(self, model):
		return any(item.value(model) for item in self.operand)

class Implication(Sentence):
	def __init__(self, antecedent, consequent):
		Sentence.validate(antecedent)
		Sentence.validate(consequent)
		self.antecedent = antecedent
		self.consequent = consequent
	def __eq__(self, operand):
		return ( isinstance(operand, Implication) and self.antecedent==operand.antecedent and self.consequent==operand.consequent)
	def __repr__(self):
		return f"Implication({self.antecedent}, {self.consequent})"
	def __str__(self):
		antecedent = Sentence.parenthesize(str(self.antecedent))
		consequent = Sentence.parenthesize(str(self.consequent))
		return f"{antecedent} -> {consequent}"
	def value(self, model):
		return (not self.antecedent.value(model) or self.consequent.value(model))
	def variables(self):
		return set.union(self.antecedent.variables(), self.consequent.variables())

class Bicondition(Sentence):
	def __init__(self, left, right):
		Sentence.validate(left)
		Sentence.validate(right)
		self.left = left
		self.right = right
	def __eq__(self, operand):
		return (isinstance(operand, Bicondition) and self.left==operand.left and self.right==operand.right)
	def __repr__(self):
		return f"Bicondition({self.left}, {self.right})"
	def __str__(self):
		left = Sentence.parenthesize(str(self.left))
		right = Sentence.parenthesize(str(self.right))
		return f"{left} <-> {right}"
	def value(self, model):
		leftval = self.left.value(model)
		rightval = self.right.value(model)
		return (not leftval or rightval) and (leftval or not rightval)
	def variables(self):
		return set.union(self.left.variables(), self.right.variables())
class Equivalent(Sentence):
	def __init__(self, left, right):
		Sentence.validate(left)
		Sentence.validate(right)
		self.left = left
		self.right = right
	def __eq__(self, operand):
		return (isinstance(operand, Equivalent) and self.left == operand.left and self.right == operand.right)
	def __repr__(self):
		return f"Equivalent({self.left}, {self.right})"
	def __str__(self):
		left = Sentence.parenthesize(str(self.left))
		right = Sentence.parenthesize(str(self.right))
		return f"{left} = {right}"
	def value(self, model):
		return self.left.value(model) == self.right.value(model)
	def variables(self):
		return set.union(self.left.variables(), self.right.variables())
