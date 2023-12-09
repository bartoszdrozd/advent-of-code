import time
import re

start_time = time.time()

file = "input.txt"
with open(file, "r") as f:
	data = list(f.readlines())

red_pattern = '(\d+) red'
blue_pattern = '(\d+) blue'
green_pattern = '(\d+) green'


def check_bags(data_list):
    bags_threshold = [12, 13, 14] #red, green, blue
    total_sum = 0
    second_answer = 0
    for row, line in enumerate(data_list):
        bags = [0, 0, 0]
        line_num = int(line.strip().split(':')[0].split()[1])
        # print(line_num)
        red = re.findall(red_pattern, line)
        red = [int(elem) for elem in red]
        green = re.findall(green_pattern, line)
        green = [int(elem) for elem in green]
        blue = re.findall(blue_pattern, line)
        blue = [int(elem) for elem in blue]
        bags = [max(red), max(green), max(blue)]
        second_answer += bags[0] * bags[1] * bags[2]
        if bags[0] <= bags_threshold[0] and bags[1] <= bags_threshold[1] and bags[2] <= bags_threshold[2]:
            total_sum += line_num
    print(f'Part One: {total_sum}')
    print(f'Part Two: {second_answer}')
    return total_sum, second_answer

check_bags(data)

end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')