import re

checklist = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
file = 'inut.txt'
with open(file, 'r') as f:
    new_list = f.readlines()
    control_list = []
    counter_first = 0
    for line in new_list:
        if line != "\n":
            for elem in line:
                #elements = re.search("([a-z]{3}:)", line)
                elements = re.findall("([a-z]{3}:\#?[a-z0-9]*)", line)
                print(elements)
            for elem in elements:
                control_list.append(elem)
        else:
            overlapping_counter = 0
            for elem in control_list:
                if elem in checklist:
                    overlapping_counter += 1
            if overlapping_counter == 7:
                counter_first += 1


            control_list.clear()
    print(f"Answer to the first task: {counter_first}")
