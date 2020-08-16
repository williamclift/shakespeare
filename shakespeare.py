'''
	Shakespeare Machine Learning Algorithm

		@author William Clift
			- 16 August 2020

'''

def oneGram(str):
	return str.split(' ')

def nGram(tokens, n):
	newList = list()
	num = len(tokens)

	for i in range(num - n):
		concat = ''
		for j in range(n):
			concat += tokens[i+j] + ' '

		newList.append(concat.rstrip())

	return newList



#function to split text into word
tokens = oneGram("The quick brown fox jumps over the lazy dog")

for token in tokens:
	print(token)

for e in nGram(tokens, 3):
	print(e)




