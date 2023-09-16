def my_function():
  x = 20
  def my_inner_function():
    print(x)
  my_inner_function()
my_function()


matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
print(matrix[0][0][0])


numbers = [1, 2, 3, 4, 5]
print(numbers[4:])


list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[0:4])


if 4 + 5 == 10:
    print("TRUE")
else:
    print("FALSE")
print("TRUE")


i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1


x = 'abcd'
for i in x:
    print(i.upper())


list1 = [1, 2, 3, 4]
for i, j in enumerate(list1):
    print(i, j)


list1 = [1, 2, 3, 4, 5]
list1[4] = 10
list1.append(11)
print(list1)


tuple1 = (0,1,2,3,4,5)
print(tuple1[0:4])


my_list = [0, 1, 2, 3, 4]
print(my_list.index(2))


def my_function(*friends):
  print("The tallest student is " + friends[1])

my_function("john", "Ella", "mark")


matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix)
print(matrix[1][1][1])


print(type(100_25))


for letter in 'KodeKloud':
    if letter == 'e':
        continue
    print('Letter : ' + letter)


matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2)
print(matrix2[2])


print(2 * 3 ** 3 * 4)


def mean_func(list1):
    return sum(list1) / len(list1)

print(mean_func([5, 2, 2, 4]))


ages = [56, 72, 24, 46]
ages.sort()
print(ages)