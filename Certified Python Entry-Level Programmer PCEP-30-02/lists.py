################### Lists ##################

# list1 = [10, 11, 12, 13, 14]
# print(list1[::3])

# list1=[2,5,3,1]
# a = list1[2:4]
# print(a)

# a = list1[::2]
# print(a)

# a = list1[::-1]
# print(a)

# a = list1[::1]
# print(a)

# numbers = [1, 2, 3, 4, 5]
# numbers[4] = 6
# print(numbers[4])

# list1 = [1, 2, 3, 4, 5]
# print(list1[4])


################### Lists Methods ##################

# list1=['UK','India','Canada']
# list1.insert(1,8)
# print(list1)

# list1 = [4, 4, 3, 1]
# list1.pop(2)
# print(list1)

# list1 = [10, 20, 30, 40, 50]
# list1.append(60)
# print(list1)

# ages = [56, 72, 24, 46]
# ages.sort()
# print(ages)

# list1=["Go","Java","C","Python"]
# print(max(list1))

# list1=["Go","Java","C","Rust"]
# print(min(list1))

# list1=['h', 'e', 'l', 'l', 'o']
# print(len(list1))

# num = [4, 4, 3, 1]
# num.sort()
# print(num)


################### Iterating Lists ##################

# for x in [0, 1, 1, 3]:
#     for y in [0, 2, 1, 2]:
#             print('*')


# for letter in 'KodeKloud':
#     if letter == 'u':
#         continue
#     print('Letter : ' + letter)


# sum = 0
# values = [2,9,1,7]
# for number in values:
#     sum = sum + number

# print(sum)


# sum = 0
# values = [2,9,1,7]
# for number in values:
#     sum += number

# print(sum)


# for letter in 'KodeKloud':
#     if letter == 'e':
#         continue
#     print('Letter : ' + letter)


# for x in [0, 2, 1, 3]:
#     for y in [0, 4, 1, 2]:
#             print('*')


################### Understanding Lists ##################

# list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
# for i in list1:
#       if len(i)==4:
#         print(i)


# list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
# for i in list1:
#       if len(i)==3:
#         print(i)


# list1 = [10, 11, 12, 13, 14]
# print(list1[::1])
# print(list1[::2])
# print(list1[::3])


# list1 = [1, 2, 3, 4]
# for i, j in enumerate(list1):
#      print(i, j)


# list1=[4,0,7,1]
# print(list1[::-1])


# list1 = [1, 2, 3, 4]
# for index, j in enumerate(list1):
#      print(index, j)


# list1 = [10, 11, 12, 13, 14]
# list1.append(15)
# print(list1)


# letters = ["A", "B", "C", "D", "E"]
# print(letters[1:])


################### Slicing Lists ##################

# my_list = [0, 1, 2, 3, 4]
# print(my_list[::-1])


# my_list = [0, 1, 2, 3, 4]
# print(my_list[::2])


# list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
# print(list1[0:4])


# list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
# print(list1[2:4])


# my_list = [0, 1, 2, 3, 4]
# my_list.append("python")
# b = my_list[1:]
# print(b)


# my_list = [0, 1, 2, 3, 4]
# my_list.append("python")
# print(my_list[2:])


# my_list = [0, 1, 2, 3, 4]
# print(my_list[::3])


# my_list = [0, 1, 2, 3, 4]
# print(my_list[2:4])


################### Finding in  Lists ##################

# list1 = [0, 3, 4, 1, 2]
# list1[1]=[8,9]
# print(list1)


# list1 = [0, 3, 4, 1, 2]
# list1[2:4]=[1,2]
# print(list1)


# Li = ['A','C','b', 1, 3, 4]
# print('A' in Li)


# list1=[3,4,6,1,2]
# list2=list1
# list1[1]=9
# print(list2)


# my_list = [0, 1, 2, 3, 4]
# print(my_list.index(2))


# print((4, 6) not in [(4, 7), (5, 6), "hello"])


# list1 = [0, 3, 4, 1, 2]
# list1[2:5]=[8,9]
# print(list1)


# countries = ["USA", "Canada", "India"]
# countries[0], countries[1] = countries[1], countries[0]
# print(countries)


# list1=[3,4,6,1,2]
# list2=list1
# list1[0]=9
# print(list2)


################### Nested Lists 2D ##################

# matrix = [[j for j in range(3)] for i in range(3)] 
# print(matrix)
# print(matrix[1][2])


# a = []
# for i in range(5):
#     a.append([])
#     for j in range(5):
#         a[i].append(j)
# print(a)
# print(a[2][3])


# countries = [['Egypt', 'USA', 'India'],
#        ['Dubai', 'America', 'Spain'], 
#        ['London', 'England', 'France']]
# countries2  = [country for sublist in countries for country in 
#                        sublist if len(country) < 6]
# print(countries2)


# countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
# countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
# print(countries2)


# matrix = [[j for j in range(4)] for i in range(4)] 
# print(matrix)
# print(matrix[3][1])


# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)
# print(matrix2)
# print(matrix2[2])


# matrix = [[j for j in range(3)] for i in range(3)] 
# print(matrix)
# print(matrix[2][1])


# a = []
# for i in range(5):
#     a.append([])
#     for j in range(5):
#         a[i].append(j)
# print(a)
# print(a[3][3])


# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# matrix2 = []

# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)
# print(matrix2)
# print(matrix2[0])


# a = []
# for i in range(2):
#     a.append([])
#     for j in range(2):
#         a[i].append(j)

# print(a)


################### Nested Lists – 3D ##################

matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)
print(matrix2)
print(matrix2[2])


Colors= [ [['Blue','Green','White','Black']], [['Green','Blue','White','Yellow']] , [['White','Blue','Red','Green']] ]
print(Colors[2][0][2])


matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix)
print(matrix[1][2])


matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
print(matrix[0][0][0])


matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)
print(matrix2)
print(matrix2[2][0])


matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix)
print(matrix[2][1])


Colors = [ ['Red', 'Green', 'White', 'Black'], ['Green', 'Blue', 'White', 'Yellow'] ,['White', 'Blue', 'Green', 'Red'] ]
print(Colors[1][2])


matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2][2])


matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix)
print(matrix[0][0][1])


matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[1][1][1])
