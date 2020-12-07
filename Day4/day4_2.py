import re

checklist = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
file = 'inut.txt'


def check_dict_elements(test_dict):
    global valid_counter
    valid_elements_counter = 0
    hcl_counter = 0
    eyes_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hcl_valid_list = list('0123456789abcdef')
    if len(test_dict['byr']) == 4 and 1920 <= int(test_dict['byr']) <= 2002:
        valid_elements_counter += 1
    if len(test_dict['iyr']) == 4 and 2010 <= int(test_dict['iyr']) <= 2020:
        valid_elements_counter += 1
    if len(test_dict['eyr']) == 4 and 2020 <= int(test_dict['eyr']) <= 2030:
        valid_elements_counter += 1
    if test_dict['hgt']:
        if test_dict['hgt'].endswith('cm'):
            if 150 <= int(test_dict['hgt'].rstrip('cm')) <= 193:
                valid_elements_counter += 1
        elif test_dict['hgt'].endswith('in'):
            if 59 <= int(test_dict['hgt'].rstrip('in')) <= 76:
                valid_elements_counter += 1
    if len(test_dict['hcl'].lstrip('#')) == 6:
        for character in test_dict['hcl'].lstrip('#'):
            if character not in hcl_valid_list:
                break
            else:
                hcl_counter += 1
        if hcl_counter == 6:
            valid_elements_counter += 1
    if test_dict['ecl'] in eyes_colors:
        valid_elements_counter += 1
    if len(test_dict['pid']) == 9:
        if test_dict['pid'].isnumeric():
            valid_elements_counter += 1
    valid_counter = valid_elements_counter


with open(file, 'r') as f:
    new_list = f.readlines()
    counter_first = 0
    counter_second = 0
    quick_dict = {}
    for line in new_list:
        if line != '\n':
            line = line.rstrip('\n')
            elements = re.findall("([a-z]{3}:\#?[a-z0-9]*)", line)
            for elem in elements:
                elem = elem.split(':')
                quick_dict[elem[0]] = elem[1]
        else:
            overlapping_counter = 0
            for key in quick_dict:
                if key in checklist:
                    overlapping_counter += 1
            if overlapping_counter == 7:
                counter_first += 1
                check_dict_elements(quick_dict)
                if valid_counter == 7:
                    counter_second += 1
            quick_dict.clear()
    print(f"Answer to the first task: {counter_first}")
    print(f"Answer to the second task: {counter_second - 1}") #last line fo the file included incorrectly