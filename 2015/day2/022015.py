import time
import re

start_time = time.time()

numbers_list = []
file = "data.txt"
with open(file, "r") as f:
	for elem in f.readlines():
		elem = elem.strip('\n')
		numbers_list.append(elem)

test_data = ['3x11x24','13x5x19','1x9x27', '1x1x1', '2x2x3']

pattern = '\d+'
paper_counter = 0
total_wrapping_paper = 0
ribbon_counter = 0
total_ribbon = 0
for x in (numbers_list):
	result = re.findall(pattern, x)
	paper_counter = int(result[0]) * int(result[1]) * 2 + int(result[0]) * int(result[2]) * 2 + int(result[1]) * int(result[2]) * 2
	if int(result[0]) <= int(result [1]) and int(result[2]) <= int(result[1]):
		paper_counter += int(result[0]) * int(result[2])
		ribbon_counter = 2 * int(result[0]) + 2 * int(result[2])
	elif int(result[1]) <= int(result [2]) and int(result[0]) <= int(result[2]):
		paper_counter += int(result[0]) * int(result[1])
		ribbon_counter = 2 * int(result[0]) + 2 * int(result[1])
	else:
		paper_counter += int(result[1]) * int(result[2])
		ribbon_counter = 2 * int(result[1]) + 2 * int(result[2])
	total_wrapping_paper += paper_counter
	total_ribbon += ribbon_counter + (int(result[0]) * int(result[1]) * int(result[2]))

print(f'Part One: {total_wrapping_paper}')
print(f'Part Two: {total_ribbon}')

end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')
