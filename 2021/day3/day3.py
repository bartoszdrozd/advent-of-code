import numpy as np
import pandas 

numbers_list = []
file = 'input.txt'
with open(file, 'r') as f:
	for elem in f.readlines():
		elem = elem.strip('\n')
		numbers_list.append(elem)

b = [0 for i in range(12)]
for elem in numbers_list:
	idx = 0
	for item in elem:
		b[idx] += int(elem[idx])
		idx += 1
print(b)

output_string = ''
for elem in b:
	if elem > 500:
		output_string += '1'
	else:
		output_string += '0'

reverted_string = ''
for elem in output_string:
	if elem == "1":
		reverted_string += '0'
	else:
		reverted_string += '1'

print(f"Answer:{int(output_string,2) * int(reverted_string,2)}")

# ----------- part2 

""" def search_for_ones(binary_list):
	for elem in binary_list: """

""" zeros_counter = 0
ones_counter = 1
counter = 0 
second_task_list = numbers_list
i = 0
for i in range(12):
	for elem in second_task_list:
		counter += 1
		if counter == len(second_task_list):
			i += 1
		if elem[i] == '0':
			zeros_counter += 1
		elif elem[i] == '1':
			ones_counter += 1
	if ones_counter >= zeros_counter:
		for elem in second_task_list:
			if elem.startswith('0'):
				second_task_list.remove(elem)

print(second_task_list) """


def zero_or_one(input_list):
	for elem in input_list:
		if elem[0] == "1":
			counter += 1
		else:
			zeros_counter += 1

global zeros_counter, ones_counter
zeros_counter = 0
ones_counter = 0
counter = 0 
idx = 0
for i in range(12):
	zeros_counter = 0
	ones_counter = 0 
	#zero_or_one(numbers_list)
	for elem in numbers_list:
		if counter == len(numbers_list):
			idx += 1
		if elem[idx] == "1":
			ones_counter += 1
		else:
			zeros_counter += 1
		counter += 1
	if ones_counter >= zeros_counter:
		for elem in numbers_list:
			if elem[idx] == "0":
				numbers_list.remove(elem)
	elif zeros_counter > ones_counter:
		for elem in numbers_list:
			if elem[idx] == "1":
				numbers_list.remove(elem)
	print(numbers_list)