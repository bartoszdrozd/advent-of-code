import time

start_time = time.time()

test_data = [(7, 9), (15, 40), (30, 200)]
data = [(49, 298), (78, 1185), (79, 1066), (80, 1181)]
test_data_two = [(71530, 940200)]
data_two = [(49787980, 298118510661181)]

def optimise_road(test_data):
    speed = 0
    time = 0
    max_distance = 0
    total_counter = 1
    for elem in test_data:
        counter = 0
        max_distance = elem[1]
        for i in range(1, elem[0] + 1):
            speed = i
            time = elem[0]
            distance = speed * (time - i)
            if distance > max_distance:
                counter += 1
        if counter > 0:
            total_counter *= counter

    return total_counter

print(f'Part One: {optimise_road(data)}')
print(f'Part Two: {optimise_road(data_two)}')

end_time = time.time()

print(f'Execution time: {(end_time - start_time) * 1000} miliseconds')