import time
import re
import num2words

start_time = time.time()

file = "input.txt"
with open(file, "r") as f:
	data_list = f.readlines()

literal_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numbers = {
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
	for x in data_list:
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


pattern = '(\D+)'
total_count = 0
counter = 0
for elem in data_list:
	test_list = []
	elem = elem.rstrip('\n')
	letter_index = 0
	elem_list = list(elem)
	for numb in elem_list:
		if numb.isdigit():
			elem_list[letter_index] = num2words.num2words(numb)
		letter_index += 1
	elem = ''.join(elem_list)
	words = re.findall(pattern, elem)
	test_dict = {}
	for word in words:
		for literal in literal_list:
			start = 0
			while word.find(literal, start) != -1:
				index = word.find(literal, start)
				test_dict[index] = numbers[literal]
				start = index + 1
	sorted_dict = dict(sorted(test_dict.items()))
	dict_list = []
	for key in sorted_dict:
		dict_list.append(int(sorted_dict[key]))
	value = int((str(dict_list[0]) + str(dict_list[-1])))
	total_count += value


print(f'Part One: {getsum(data_list)}')
print(f'Part Two: {total_count}')

end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')