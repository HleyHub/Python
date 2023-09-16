for num in range(0, 11):
	if num % 2 != 0:
	    print(num)
		

matrix = [[j for j in range(4)] for i in range(4)] 
print(matrix)
print(matrix[3][1])


def get_odd_func(numbers):
    odd_numbers = [num for num in numbers if num % 2]
    return odd_numbers

print(get_odd_func([7, 4, 5, 6, 9, 8, 12]))


x = 30
def my_function():
  def my_inner_function():
    x = 20
  print(x)
  my_inner_function()

my_function()


## This code produces an error because the tuple cannot be modified
# tuple1 = (1,2,3,4,5)
# print(tuple1.append(6))


list1 = [1, 2, 3, 4, 5]
list1[0] = 10
print(list1)


def input_num():
    return int(input (num) )


## This code gives an error TypeError: 'int' object is not iterable
# x = tuple(3)
# print(x)


a = 0
def add_three(a):
	return a+3

result = add_three(a)
print(result)


print((4, 6) not in [(4, 7), (5, 6), "hello"])

## This code gives an error AttributeError: 'list' object has no attribute 'upper'
# list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
# print(list1.upper())


i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1


def my_function(*ages):
  print("The older friend is " + ages[1] + " years")

my_function("13", "12", "11")


list1 = ['h', 'e', 'l', 'l', 'o']
print(len(list1))


list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
      if len(i)==3:
        print(i)


matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2)
print(matrix2[2])


print(6. // 4)
