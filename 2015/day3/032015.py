import time
import re

start_time = time.time()

numbers_list = []
file = "data.txt"
with open(file, "r") as f:
	data_list = f.read()

test_data = "^v^v^v^v^v"

counter = 0
coordinates = [0, 0]
visited_houses = {}
for x in range(len(data_list)):
	if tuple(coordinates) in visited_houses:
		visited_houses[tuple(coordinates)] += 1
	else:
		visited_houses[tuple(coordinates)] = 1
		counter += 1
	if data_list[x] == 'v':
		coordinates[1] -= 1
	elif data_list[x] == '^':
		coordinates[1] += 1
	elif data_list[x] == '<':
		coordinates[0] -= 1
	elif data_list[x] == '>':
		coordinates[0] += 1



print(f'Part One: {counter}')
# print(f'Part Two: {total_ribbon}')

end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')
