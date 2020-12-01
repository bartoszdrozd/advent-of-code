years_list = []
new_list = []
file = "expanses.txt"
with open(file, "r") as f:
    for line in f:
        year = int(f.readline())
        years_list.append(year)
        new_list.append(2020 - year)

    answer = []
    for item in new_list:
        if (item) in years_list:
            answer.append(item)
    print(len(years_list))
    print(len(new_list))
    print(f"Answer = {answer[0] * answer[1]}")

#
# def find3Numbers(A, arr_size, sum):
#     for i in range(0, arr_size - 2):
#         for j in range(i + 1, arr_size - 1):
#             for k in range(j + 1, arr_size):
#                 if A[i] + A[j] + A[k] == sum:
#                     print("Triplet is", A[i],
#                           ", ", A[j], ", ", A[k])
#                     return True
#     return False
#
#
# # Driver program to test above function
# A = years_list
# A.sort()
# print(A)
# print(len(A))
# sum = 2020
# arr_size = len(A)
# find3Numbers(A, arr_size, sum)