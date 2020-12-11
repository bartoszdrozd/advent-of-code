import re
target = ["shiny gold"]
bag_counter = 0
loop_counter = 0
previous_bag_counter = 0
with open('input7.txt', 'r') as f:
    new_list = f.readlines()
    while loop_counter < 7:
        for line in new_list:
            for elem in target:
                if elem in line:
                    container = re.search("([a-z]*\ [a-z]*\ bags?\ contain)", line)
                    new_bag = container[1].removesuffix(' bags contain')
                    if new_bag not in target:
                        bag_counter += 1
                        target.append(new_bag)
                        break
        loop_counter += 1
    print(bag_counter) #119 is too low
