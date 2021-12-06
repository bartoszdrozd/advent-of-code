file = 'input6.txt'

with open(file, 'r') as f:
    new_list = f.readlines()
    quick_dict = {}
    sum_count = 0
    line_counter = 0
    sum_count_two = 0
    for line in new_list:
        line = line.strip('\n')
        if line == '':
            sum_count += len(quick_dict)
            for item in quick_dict.values():
                if item == line_counter:
                    sum_count_two += 1
            quick_dict.clear()
            line_counter = 0
        else:
            line_counter += 1
            for letter in line:
                if letter not in quick_dict:
                    quick_dict[letter] = 1
                else:
                    quick_dict[letter] += 1
    print(f"What is the sum of those counts? \nAnswer = {sum_count}")
    print(f"Second task answer = {sum_count_two}")