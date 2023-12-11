import time
import re

start_time = time.time()

file = "input.txt"
with open(file, "r") as f:
	data_list = f.readlines()
characters_list = []
characters_locations = []

def get_indices_of_char(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def get_characters_locations(data_list):
    line_number = 1
    for lines in data_list:
        for elem in lines:
            if elem.isalnum() == False and elem != '.' and elem != '\n':
                indices = get_indices_of_char(lines, elem)
                for index in indices:
                    if (line_number, index) not in characters_locations:
                        characters_locations.append((line_number, index))
                    
        line_number += 1
    return characters_locations

def get_numbers(data_list):
    match_list = []
    line_number = 1
    for lines in data_list:
        matches = re.finditer(r'\d+', lines)
        for match in matches:
            match_list.append([line_number, match.start(), match.end() - match.start(), match.group()])
        line_number += 1
    return match_list

def get_adjacent(matches, char_loc):
    adjacent_sum = 0
    for elem in char_loc:
        for location in matches:
            if elem[0] == location[0] or elem[0] == location[0] + 1 or elem[0] == location[0] - 1:
                if elem[1] == location[1] - 1 or elem[1] == location[1] or elem[1] == location[1] + location[2] - 2 or elem[1] == location[1] + location[2] - 1 or elem[1] == location[1] + location[2]:
                    adjacent_sum += int(location[3])
    return(adjacent_sum)

def gear_ratio_calc():
    return 0


get_characters_locations(data_list)
get_numbers(data_list)
# print(get_adjacent(get_numbers(data_list), characters_locations))
print(f'Part One: {get_adjacent(get_numbers(data_list), characters_locations)}')
# print(f'Part Two: {second_answer}')


end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')