years_list = []
new_list = []
file = "expanses.txt"
with open(file, "r") as f:
    years_list = f.readlines()
    idx = 0
    for elem in years_list:
        years_list[idx] = int(elem.rstrip("\n"))
        idx += 1
        new_list.append(2020 - int(elem))

    answer = []
    for item in new_list:
        if item in years_list:
            answer.append(item)

    print(f"Answer = {answer[0] * answer[1]}")


def find_triplet(A, sum):
    arr_size = len(A)
    for i in range(0, arr_size - 2):
        for j in range(i + 1, arr_size - 1):
            for k in range(j + 1, arr_size):
                if A[i] + A[j] + A[k] == sum:
                    print(f"Three numbers that sum to {sum} are: {A[i]} ,  {A[j]} , {A[k]}")
                    print(f"The answer to second task is =  {A[i] * A[j] * A[k]}")
                    return True
    return False


find_triplet(years_list, 2020)