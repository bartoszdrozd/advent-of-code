import re


file = "input.txt"
with open(file, "r") as f:
	input_list = f.readlines()
	guidelines_list= []
	for elem in input_list:
		guidelines_list.append(elem.strip('\n'))


horizontal_postion = 0
depth = 0
depth_second = 0
aim = 0
pattern = '([a-z]*) ([0-9]+)'
for elem in guidelines_list:
	match = re.search(pattern, elem)
	if match.group(1) == "forward":
		horizontal_postion += int(match.group(2))
		depth_second += aim * int(match.group(2))
	elif match.group(1) == "up":
		depth -= int(match.group(2))
		aim -= int(match.group(2))
	elif match.group(1) == "down":
		depth += int(match.group(2))
		aim  += int(match.group(2))

print(f"FIRST - Depth: {depth}, Horizontal: {horizontal_postion}, Answer: {depth*horizontal_postion}")
print(f"SECOND - Depth: {depth_second}, Horizontal: {horizontal_postion}, Answer: {depth_second*horizontal_postion}")