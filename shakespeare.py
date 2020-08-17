'''
	Shakespeare Machine Learning Algorithm

		@author William Clift
			- 16 August 2020

'''
import numpy as np


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

	return np.asarray(matrix)


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
	for j in range(len(matrix)):
		count = 0
		for i in range(len(matrix)):
			count += matrix[i][j]
		vector.append(count)

	return np.asarray(vector)


def position(size, n):
	sub = size - n
	col_start = sub / 2
	row_start = col_start + (sub % 2)
	return [row_start, col_start]


def partition(matrix, n): 			#Assumes partition smaller than actual matrix
	starting_position = position(len(matrix), n)
	row_start = starting_position[0]
	col_start = starting_position[1]

	partition = list()
	for i in range(row_start, row_start + n):
		subpartition = list()
		for j in range(col_start, col_start + n):
			subpartition.append(matrix[i][j])
		partition.append(subpartition)
	return np.asarray(partition)


def weigh(vector):
	shkspr = reduceCalc(partition(readMatrix(), len(vector)))

	size = len(vector)

	result = list()
	for i in range(size):
		result.append(vector[i]-shkspr[i])
	return np.asarray(result)


def sum(vector):
	sum = 0
	for i in vector:
		sum += i
	return sum


def process(str):
	tokens = str.split(' ')
	result = list()
	for i in range(len(tokens)):
		subframe = value(nGram(tokens, i))
		while len(subframe) < len(tokens):
			subframe.append(0)
		result.append(subframe)
	return np.asarray(result)


def diff(new, old):
	value = old
	delta = old - new
	perc = 0

	if delta < 0:
		perc = new / old
	elif delta > 0:
		perc = (-1 * new) / old
	value += ((delta * perc) /10)

	return value


def backPropogate(result):
	matrix = readMatrix()
	offset = position(len(matrix), len(result))
	u = offset[0]
	v = offset[1]
	adj = list()
	for i in range(len(result)):
		subframe = list()
		for j in range(len(result[0])):
			subframe.append(diff(result[i, j], matrix[i + u, j + v]))
		adj.append(subframe)

	writeMatrix(np.asarray(adj))


def resetMatrix(n):
	reset = list()
	for i in range(n):
		subframe = list()
		for j in range(n):
			if j > n - i - 1:
				subframe.append(0)
			else:
				subframe.append(1)
		reset.append(subframe)

	writeMatrix(np.asarray(reset))


def runTest(string):

	result = process(string)
	reduced = reduceCalc(result)
	weighted = weigh(reduced)
	backPropogate(result)
	print(readMatrix())


'''
	RUN ALGORITHM
'''

runTest("It is great to meet you.")





