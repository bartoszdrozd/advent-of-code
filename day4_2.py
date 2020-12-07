import re

checklist = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
file = 'inut.txt'
with open(file, 'r') as f:
    new_list = f.readlines()
    print(new_list)
    counter_first = 0
    quick_dict = {}
    for line in new_list:
        if line != "\n":
            elements = re.search("([a-z]{3}:\#?[a-z0-9]*)", line)
            print(elements)
            for elem in elements:
                elem.split(':')
                quick_dict[elem[0]] = elem[1]
        else:
            overlapping_counter = 0
            for elem in quick_dict.keys():
                if elem in checklist:
                    overlapping_counter += 1
            if overlapping_counter == 7:
                counter_first += 1
            quick_dict.clear()
    print(f"Answer to the first task: {counter_first}")
