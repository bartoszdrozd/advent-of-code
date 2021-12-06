file = "input2.txt"
import re


with open(file, "r") as f:
    new_list = f.readlines()
    total_counter = 0
    second_counter = 0
    for line in new_list:
        test_string = re.match("([0-9]*\-[0-9]*)\s([a-z]\:{1})\s([a-z]{2,})", line)
        lower_limit, upper_limit = test_string.group(1).split('-')
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)
        letter = test_string.group(2).rstrip(':')
        sequence = test_string.group(3).strip('\n')
        if sequence[lower_limit - 1] == letter and sequence[upper_limit - 1] == letter:
            pass
        elif sequence[lower_limit - 1] == letter or sequence[upper_limit - 1] == letter:
            second_counter += 1
        else:
            pass
        letter_counter = 0
        for elem in sequence:
            if elem == letter:
                letter_counter += 1
        if lower_limit <= letter_counter <= upper_limit:
            total_counter += 1
    print(f"Passwords valid in first task: {total_counter}")
    print(f"Passwords valid in second task: {second_counter}")

