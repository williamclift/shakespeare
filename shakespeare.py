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
		for j in range(n+1):
			concat += tokens[i+j] + ' '

		newList.append(concat.rstrip())

	return newList

def value(tokens):
	vector = list()

	for i in tokens:
		count = 0
		arr = list(i)
		for j in arr:
			count += ord(j)
		vector.append(count)

	return vector

#function to split text into word
tokens = oneGram("Hello Sir, How are you today?")

result = list()
for i in range(len(tokens)):
	subframe = value(nGram(tokens, i))
	while len(subframe) < len(tokens):
		subframe.append(0)
	result.append(subframe)

print(result)

#print(result[0])
#for i in range(len(result)):
#	print(result[i])




