i = 5
while True:
    if i%0o11 == 0:     # This is octal base: 1*8^1 + 1*8^0 = 9
        break
    print(i)
    i += 1
print(0o11)


my_list = [0, 1, 2, 3, 4]
my_list.append("python")
print(my_list[2:])


list1 = [1, 2, 3, 4, 5]
for i in list1:
    if i==5:
        print(i)


matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2][2])


testdict = {'brand': 'oppo', 'ram': '3', 'Os': 'Android', 'year': 2020}
del testdict['brand']
print(testdict)


def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    return even_numbers

print(get_even_func([1, 2, 3, 4, 5, 6]))


list1=['UK','India','Canada']

list1.insert(1,8)

print(list1)


name = "Sally"# employee name
 
data = "#123" 
print (name+data)


a = 20//5
print(a)


x = 0
a = 6
b = 6
if a > 0:
    if b < 0: 
        x = x + 6 
    elif a > 6:
        x = x + 5
    else:
        x = x + 4
else:
    x = x + 3

print(x)


matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)
print(matrix[1][2])


i = 1
x = 3
sum = 0
while ( i <= x ):
 sum += i
 i += 1
print(sum)


x = 20
def my_function():
  x = 30
  print(x, end=' ')

my_function()
print(x, end=' ')


for num in range(5, 9):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break