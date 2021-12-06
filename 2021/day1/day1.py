def sum_every_triple(input_list):
	i = 0
	triple_list = []
	for elem in range(len(input_list)-2):
		triple_list.append(input_list[i] + input_list[i+1] + input_list[i+2])
		i += 1
	return(triple_list)


file = "input1.txt"
with open(file, "r") as f:
	depth_list = f.readlines()
	depth_values = []
	for elem in depth_list:
		depth_values.append(int(elem.strip('\n')))

idx = 1
increase_counter = 0
for elem in depth_values[1:]: #counting starts from the second value
	if depth_values[idx] > depth_values[idx-1]:
		increase_counter += 1
	idx += 1
print(f"Task 1 answer: {increase_counter}")


triplet_list = sum_every_triple(depth_values)

test_index = 1
second_counter = 0
for elem in triplet_list[1:]: #counting starts from the second value
	if triplet_list[test_index] > triplet_list[test_index-1]:
		second_counter += 1
	test_index += 1
print(f"Task 2 answer: {second_counter}")




