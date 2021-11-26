from propositional_logic import *
from check_kb import *
from parse import *
from consistency import *

try:
	knowledge_base = None
	while True:
		inp = input().strip()
		if len(inp)==0:
			knowledge_base = None
			continue
		if(inp[-1] == "?"):
			if knowledge_base is None:
				query = parse(inp[:-1])
				result = consistent(query)
				if result[0] == False:
					print ("Query is False. It's a Contradiction.")
				elif result[1]:
					print ("Query is True. It's a Tautology.")
				else:
					print ("Can't answer. Knowledge Base is EMPTY!")
			else:
				query = parse(inp[:-1])
				variables = set.union(knowledge_base.variables(), query.variables())
				values = dict()
				if check_kb(knowledge_base, query, variables, values):
					print ("Query is True")
				else:
					print ("Query is False")
		else:
			new_knowledge = parse(inp)
			if new_knowledge is not None:
				if consistent(new_knowledge)[0]:
					if knowledge_base is None:
						knowledge_base =And(new_knowledge)
					elif consistent(And(knowledge_base,new_knowledge))[0]:
						knowledge_base.add(new_knowledge)
					else:
						print ("Entered sentence is not consistent wrt Knowledge Base!")
				else:
					print ("Entered sentence is not consistent itself! It's a Contradiction.")
			#print(knowledge_base)
except KeyboardInterrupt:
	print ("Exiting...")
