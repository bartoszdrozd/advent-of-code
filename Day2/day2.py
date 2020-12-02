file = "input2.txt"
import re

with open(file, "r") as f:
    new_list = f.readlines()
    total_counter = 0
    for line in new_list:
        occurance = re.findall("[0-9]\-[0-9]*", line)
        lower_limit, upper_limit = occurance[0].split('-')
        lower_limit = int(lower_limit)
        upper_limit = int(upper_limit)
        letter = re.findall("([a-z]\:){1}", line)
        letter = letter[0].rstrip(":")
        sequence = re.findall("[a-z]{2,}", line)
        sequence = sequence[0].strip("\n")
        for elem in sequence:
            letter_counter = 0
            if elem == letter:
                letter_counter += 1
        if lower_limit <= letter_counter and letter_counter <= upper_limit:
            total_counter += 1
    print(total_counter)

