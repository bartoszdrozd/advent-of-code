file = 'input5.txt'
with open(file, 'r') as f:
    new_list = f.readlines()
    check_dict = {}
    for elem in new_list:
        elem.rstrip('\n')
        test_string = ''
        for letter in elem:
            if letter == 'B' or letter == 'R':
                test_string += '1'
            elif letter == 'F' or letter == 'L':
                test_string += '0'
        row = test_string[:-3]
        seat = test_string[-3:]
        seat_id = int(row, 2) * 8 + int(seat, 2)
        check_dict[elem.rstrip('\n')] = seat_id
        a = sorted(check_dict.items(), key=lambda x: x[1])
        b = sorted(check_dict.values())
        check_elem = min(b)
        counter = 0
    for elem in b:
        if elem - 1 == check_elem and counter != 0:
            check_elem = elem
            counter += 1
            print(f"it's here {elem}")
        else:
            print(elem)
    print(b)
    print(f"Highest seat ID is {a[-1]}")
