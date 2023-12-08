import time

start_time = time.time()

file = "input.txt"
with open(file, "r") as f:
	data_list = f.read()

# test_data = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"""

numbers = {
	'zero': 0,
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9
}

def getsum(data_list):
	counter = 0
	for x in data_list.splitlines():
		first_number = 0
		last_number = 0
		first_number_set = False
		last_number_set = False
		for elem in x:
			if elem.isdigit() and first_number_set == False:
				first_nubmer = elem
				last_number = elem
				first_number_set = True
			elif elem.isdigit() and last_number:
				last_number = elem
		counter += int(str(first_nubmer) + str(last_number))
	return counter

def get_sum_literals(data_list):
	counter = 0
	for x in data_list.splitlines():
		first_number = 0
		last_number = 0
		first_number_set = False
		last_number_set = False
		for elem in x:
			if elem.isdigit() and first_number_set == False:
				first_nubmer = elem
				last_number = elem
				first_number_set = True
			elif elem.isdigit() and last_number:
				last_number = elem
		counter += int(str(first_nubmer) + str(last_number))
	return counter



print(f'Part One: {getsum(data_list)}')
# print(f'Part Two: {second_answer}')

end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')