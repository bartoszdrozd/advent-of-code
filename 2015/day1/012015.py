import time

start_time = time.time()

file = "data.txt"
with open(file, "r") as f:
	data_list = f.read()

test_data = ")())())"
counter = 0
transition_counter = 0
for x in range(len(data_list)):
	if data_list[x] == '(':
		counter += 1
	else:
		counter -=1
	if counter == -1 and transition_counter == 0:
		transition_counter += 1
		second_answer = x + 1
print(f'Part One: {counter}')
print(f'Part Two: {second_answer}')

end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')
