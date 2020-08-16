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

def readMatrix():
	file = open("matrix.txt","r") 

	matrix = list()
	for line in file:
		row = line.strip('\n').strip().split(' ')
		subframe = list()
		for i in row:
			subframe.append(int(i))
		matrix.append(subframe)

	return matrix

def writeMatrix(matrix):
	file = open("matrix.txt","w") 

	string = ''
	for row in matrix:
		rowString = ''
		for e in row:
			rowString += str(e) + ' '
		string += rowString + '\n'

	file.write(string)

def reduceCalc(matrix):
	vector = list()

	for j in range(len(matrix[0])):
		count = 0
		for i in range(len(matrix)):
			count += matrix[i][j]
		vector.append(count)

	return vector

def partition(matrix, n): #Assumes partition smaller than actual matrix
	initial_size = len(matrix)
	partition = list()
	sub = initial_size - n
	col_start = sub / 2
	row_start = col_start + (sub % 2)

	for i in range(row_start, row_start + n):
		subpartition = list()
		for j in range(col_start, col_start + n):
			subpartition.append(matrix[i][j])
		partition.append(subpartition)
	return partition

def weigh(matrix):
	shkspr = reduceCalc(partition(readMatrix(), len(matrix)))
	vector = reduceCalc(matrix)

	size = len(vector)

	result = list()
	for i in range(size):
		result.append(vector[i]-shkspr[i])
	return result

def sum(vector):
	sum = 0
	for i in vector:
		sum += i
	return sum


#function to split text into word
tokens = oneGram("I must be honest with you.")

result = list()
for i in range(len(tokens)):
	subframe = value(nGram(tokens, i))
	while len(subframe) < len(tokens):
		subframe.append(0)
	result.append(subframe)

print(sum(weigh(result)))




