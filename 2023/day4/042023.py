import time
import re

start_time = time.time()

file = "input.txt"
with open(file, "r") as f:
	data = list(f.readlines())

count_dict = {k:1 for k in range(1,len(data)+1)} 

# print(count_dict)
# points_arr = []

# for row, line in enumerate(data):
#     line_num = int(line.strip().split(':')[0].split()[1])
#     print(line_num)
#     num_of_instances = count_dict[line_num]
#     winning_nums = line.strip().split(':')[1].split('|')[0].split() 
#     print(winning_nums)
#     my_nums = line.strip().split(':')[1].split('|')[1].split() 
#     print(my_nums)
#     common_nums = [x for x in winning_nums if x in my_nums] 
#     num_added_line = len(common_nums) 
#     for i in range(line_num + 1,line_num + num_added_line + 1): 
#         count_dict[i] += num_of_instances*1 
#     points = 2**(len(common_nums) - 1) if len(common_nums)>0 else 0 

#     points_arr.append(points) 
#     print(sum(points_arr))
#     print(sum(count_dict.values()))

pattern = '[:]( +\d+.+)*[|] (\d+.+)*' 
"""line 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def getIntersection(data_list):
    # sum = 0
    points_arr = []
    for row, line in enumerate(data_list):
        line_num = int(line.strip().split(':')[0].split()[1])
        num_of_instances = count_dict[line_num]
        winning_nums = line.strip().split(':')[1].split('|')[0].split() 
        my_nums = line.strip().split(':')[1].split('|')[1].split() 
        common_nums = [x for x in winning_nums if x in my_nums] 
        num_added_line = len(common_nums) 
        for i in range(line_num + 1,line_num + num_added_line + 1): 
            count_dict[i] += num_of_instances*1 
        points = 2**(len(common_nums) - 1) if len(common_nums)>0 else 0 
        points_arr.append(points) 
        print(sum(points_arr))
        print(sum(count_dict.values()))
    return(sum(points_arr))
    # total_sum = 0
    # points_arr = []
    # for row, line in enumerate(data_list):
    #     winning_numbers_list = line.strip().split(':')[1].split('|')[0].split()
    #     my_numbers_list = line.strip().split(':')[1].split('|')[1].split()
    #     common_nums = [x for x in winning_numbers_list if x in my_numbers_list]
    #     points = 2**(len(common_nums) - 1) if len(common_nums) > 0 else 0
    #     total_sum += points
    # return(total_sum)


print(f'Part One: {getIntersection(data)}')
print(f'Part Two: {second_answer}')

# print(getCharactersLocations(data_list))
# print(getNumbers(data_list))
# print(getAdjacentData(match_list, characters_locations))

end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')