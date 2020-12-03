file = 'input3.txt'
first_opening = True

f1 = open(file, 'r')
f2 = open('testfile.txt', 'w')

for line in f1:
    f2.write(line.rstrip('\n') * 1000 + '\n')

f1.close()
f2.close()

line_counter = 0
place_counter = 0
place_counter_two = 0
place_counter_three = 0
place_counter_four = 0
place_counter_five = 0
hash_counter = 0
hash_counter_two = 0
hash_counter_three = 0
hash_counter_four = 0
hash_counter_five = 0


f2 = open('testfile.txt', 'r')


for line in f2:
    #Right 3, down 1. (This is the slope you already checked.)
    if line[place_counter] == '#':
        hash_counter += 1
    place_counter += 3
    #Right 1, down 1.
    if line[place_counter_two] == '#':
        hash_counter_two += 1
    place_counter_two += 1
    # Right 5, down 1
    if line[place_counter_three] == '#':
        hash_counter_three += 1
    place_counter_three += 5
    #Right 7, down 1.
    if line[place_counter_four] == '#':
        hash_counter_four += 1
    place_counter_four += 7
    # Right 1, down 2.
    if line_counter % 2 == 0:
        if line[place_counter_five] == '#':
            hash_counter_five += 1
        place_counter_five += 1
    line_counter += 1

hash_counters = hash_counter * hash_counter_two * hash_counter_three * hash_counter_four * hash_counter_five
print(f"Answer to the first task is {hash_counter}")
print(f"Answer to the second task is {hash_counters}")

f2.close()
