file = 'input6.txt'

with open(file, 'r') as f:
    new_list = f.readlines()
    quick_dict = {}
    sum_count = 0
    for line in new_list:
        line = line.strip('\n')
        if line == '':
            sum_count += len(quick_dict)
            quick_dict.clear()
        else:
            for letter in line:
                quick_dict[letter] = 1
    print(f"What is the sum of those counts? \nAnswer = {sum_count}")