test_data = [16,1,2,0,4,2,7,1,2,14]
#Answer1: 37, Answer2: ____

# with open("input.txt") as f:
#     data = list(map(int, f.read().split(",")))
#     print(data)
test_data.sort()
fuel_consumption = []
for elem in range(len(test_data)):
    print(elem)
    consumption = abs(elem - test_data[elem])
    fuel_consumption.append(consumption)
    #print(consumption)
print(fuel_consumption)
