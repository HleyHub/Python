def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result 

print(sum(2,3,1))


Colors = [ ['Red', 'Green', 'White', 'Black'], ['Green', 'Blue', 'White', 'Yellow'] ,['White', 'Blue', 'Green', 'Red'] ]
print(Colors[1][2])


a = 0
def add_one(a):
	return a+1

result = add_one(a)
print(result)


my_list = [0, 1, 2, 3, 4]
print(my_list[-1])


sum = 0
values = [2,9,1,7]
for number in values:
    sum = sum + number

print(sum)


list1=[3,4,6,1,2]
list2=list1
list1[0]=9
print(list2)


x = 'abcd'
for i in range(len(x)):
    y = x[i].upper()
    print(y)
print(x)


a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a)
print(a[2][3])


list1 = [0, 3, 4, 1, 2]
list1[2:4]=[1,2]
print(list1)


x = 0o11
y = 0x12b
z = 6
print(x, y, z)


x = 0
while (x < 50):
  x+=2

print(x)


## This code gives an error TypeError: 'int' object is not callable
# list1=[7,8,1,3,9]
# list1.remove(3)
# print(sum(list1))


def return_greeting():
  return "Hello, World"

print(return_greeting())


## This code gives an error NameError: name 'a' is not defined
# def myfunc():
#   a = 20

# myfunc()
# print(a)


## This code gives an error SyntaxError: invalid syntax
# y = 20
# x = y += 3
# print(x)


def double_list(numbers):
  return 2 * numbers

numbers = [1, 2, 3]
print(double_list(numbers))


## This code gives an error TypeError: can only concatenate str (not "int") to str
# print('My age is ' + 25)


inputString = input('Enter a string: ')
print(inputString*2)