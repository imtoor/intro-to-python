# data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

# data_transpose = [] # replace with your code
# for i in range(len(data)):
#     for item in data[i]:
#         data_transpose.append(item)

# temp = data_transpose
# data_transpose = []
# start = 0
# end = 4
# for x in range(0, 3):
#     data_transpose.append(temp[start:end])
#     start = end
#     end += 4

# print(data_transpose)

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)