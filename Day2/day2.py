file = "input2.txt"
import re

with open(file, "r") as f:
    new_list = f.readlines()
    print(new_list)
    for line in new_list:
        occurance = re.findall("[0-9]\-[0-9]*", line)
        lower_limit, upper_limit = occurance[0].split('-')
        letter = re.findall("([a-z]\:){1}", line)
        letter = letter[0].rstrip(":")
        print(letter)

