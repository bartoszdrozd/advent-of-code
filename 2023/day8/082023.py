import time
import re
import math

start_time = time.time()

result_dict = {}
file = "input.txt"
# file = "test_input_part_two.txt"
with open(file, "r") as file:
    for line in file:
        key, value = line.strip().split(' = ')
        value = value.strip().strip('()')
        value = tuple(value.split(', '))
        result_dict[key] = value

test_directions = 'RL'
test_directions2 = 'LLR'
directions = 'LLLLRLRLRRLRRRLRRLRLRRLRLLRRRLRRLRRRLRLLLRLRRLRLLRRRLRRLRLRRLLRRRLRRRLRLRRLRRRLRRLRRLLRRRLLLLRRLRRLRRLRRRLLLRLRLRLRRLRRRLRLRRRLRLRRRLRRLRRLLRRLLRLRRRLRLRRRLLLRLRRRLRLRRRLRRLRLRRLRRRLRRRLRRLLLRRRLRRLRRLRRLRRRLLLRRLRLRRRLLLLRRRLRRLRRRLLRLRLRRLLRRRLLRLRLRLRRLRRLRRRLRRLLRLRRLRRLLLLRRLRLRRLLRRLLRRLRRLRRRLLLRRRR'
test_directions_part_two = 'LR'

def find_last_elements(input_dict, element):
    starting_points = []
    for key, value in input_dict.items():
        if key[-1] == element:
            starting_points.append(key)
    return starting_points

def find_waypoints(nav_dict, test_directions):
    i = 0
    current_waypoint = 'AAA'
    step_count = 0
    while current_waypoint != 'ZZZ':
        if i >= len(test_directions):
            i = 0
        elif test_directions[i] == "R":
            current_waypoint = nav_dict[current_waypoint][1]
            i += 1
            step_count += 1
        elif test_directions[i] == "L":
            current_waypoint = nav_dict[current_waypoint][0]
            i += 1
            step_count += 1
    print(f'Part One: {step_count}')
    return

def find_ghost_route(nav_dict, test_directions, starting_points):
    i = 0
    z_encounters = []
    for elem in starting_points:
        step_count = 0
        while elem[-1] != 'Z':
            if i >= len(test_directions):
                i = 0
            elif test_directions[i] == "R":
                elem = nav_dict[elem][1]
                i += 1
                step_count += 1
            elif test_directions[i] == "L":
                elem = nav_dict[elem][0]
                i += 1
                step_count += 1
        z_encounters.append(step_count)

    print(f'Part Two: {math.lcm(*z_encounters)} ')
    return z_encounters

find_waypoints(result_dict, directions)
find_ghost_route(result_dict, directions, find_last_elements(result_dict, 'A'))


end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')