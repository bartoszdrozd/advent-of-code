import time
import re

start_time = time.time()

file = "test_input2.txt"
with open(file, "r") as f:
	data_list = f.readlines()
characters_list = []
characters_locations = []

# data_list = ['........','.24..4..','......*.']


def getCharactersLocations(data_list):
    line_number = 1
    for lines in data_list:
        for elem in lines:
            if elem.isalnum() == False and elem != '.' and elem != '\n':
                characters_locations.append((line_number, lines.index(elem)))
                # if elem not in characters_list:
                #     characters_list.append(elem)
                # characters_locations.append((line_number, lines.index(elem)))
        line_number += 1
    # print(characters_list)
    print(characters_locations)
    return characters_locations

match_list = []

def getNumbers(data_list):
    print(f'length of data_list: {len(data_list)}')
    line_number = 1
    for lines in data_list:
        matches = re.finditer(r'\d+', lines)
        for match in matches:
            match_list.append([line_number, match.start(), match.end() - match.start(), match.group()])
        line_number += 1
    return match_list

def getAdjacentData(matches, char_loc):
    adjacent_sum = 0
    for elem in char_loc:
        for location in matches:
            if elem[0] == 1 or location[0] == 1:
                if elem[0] == location[0] or elem[0] == location[0] + 1:
                    if elem[1] == location[1] - 1 or elem[1] == location[1] or elem[1] == location[1] + location[2] - 2 or elem[1] == location[1] + location[2] - 1 or elem[1] == location[1] + location[2]:
                        adjacent_sum += int(location[3])
                        print(f'elem: {elem}, location: {location}')
            elif elem[0] == len(data_list) or location[0] == len(data_list):
                if elem[0] == location[0] or elem[0] == location[0] - 1:
                    if elem[1] == location[1] - 1 or elem[1] == location[1] or elem[1] == location[1] + location[2] - 2 or elem[1] == location[1] + location[2] - 1 or elem[1] == location[1] + location[2]:
                        adjacent_sum += int(location[3])
                        print(f'elem: {elem}, location: {location}')
            elif elem[0] == location[0] or elem[0] == location[0] + 1 or elem[0] == location[0] - 1:
                if elem[1] == location[1] - 1 or elem[1] == location[1] or elem[1] == location[1] + location[2] - 2 or elem[1] == location[1] + location[2] - 1 or elem[1] == location[1] + location[2]:
                    adjacent_sum += int(location[3])
                    print(f'elem: {elem}, location: {location}')
    return(adjacent_sum)


# print(f'Part One: {getsum(data_list)}')
# print(f'Part Two: {second_answer}')

print(getCharactersLocations(data_list))
print(getNumbers(data_list))
print(getAdjacentData(match_list, characters_locations))


end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')