list1 = [0, 3, 4, 1, 2]
list1[1]=[8,9]
print(list1)


list1=["Go","Java","C","Python"]
print(max(list1))


list1 = [4, 4, 3, 1]
list1.pop(2)
print(list1)


testdict = {
  "brand": "apple",
  "ram": "3",
  "year": 2020,
  "year": 2021
}

print(testdict)


matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)
print(matrix2)
print(matrix2[0])


## This code gives and error NameError: name 'result' is not defined
# def multi_func():
#   result = int(input()) * 5
#   return result     

# print(result)


x = 'abcd'
for i in range(len(x)):
    print(i)


for x in [0, 2, 1, 3]:
    for y in [0, 4, 1, 2]:
            print('*')


## This code will print the number entered three times on the same line
# Num = input("Enter a Number: ") 
# print (Num * 3 )

## This code will multiplied the number entered times three 
# Num = int(input("Enter a Number: "))
# print (Num * 3 )


def myfunc():
  a = 20
  print(a)

myfunc()


def is_true(a): 
  return bool(a) 

result = is_true(3<6) 
print("The result is", result)


def my_function(names):
  for i in names:
    print(i, end=' ')

names = ["john", "mark", "emmy"]
my_function(names)


list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[2:4])


list1 = [0, 3, 4, 1, 2]
list1[2:5]=[8,9]
print(list1)


list1=[2,5,3,1]
print(list1[::-1])


countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in sublist if len(country) < 6]
print(countries2)


matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[1][2])


list1 = [10, 11, 12, 13, 14]
print(list1[::1])


x = 3
if ( x == 0 ):
  print("Am I here?")
elif ( x == 3 ):
  print("Or here?")
print("Or over here?")


def my_function(arg1, *argv): 
    print ("First argument:", arg1) 
    for arg in argv: 
        print("Next argument:", arg) 

my_function('Welcome', 'to', 'Python!')


x = 1
while ( x <= 5 ):
  x += 1
print(x)