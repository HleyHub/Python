# def sum(a,b):
#     return a+b

# print(sum(2,3))


# def my_function(arg1, *argv): 
#     print ("First argument:", arg1) 
#     for arg in argv: 
#         print("Next argument:", arg) 

# my_function('Welcome', 'to', 'Python!')


# def division(a,b):
#     return a/b

# division(8,2)


## This code throws the following error: cannot access local variable 'result' where it is not associated with a value
# def sum(*args):
#     for arg in args:
#         result += arg
#     return result 

# print(sum(2,3,1))


def my_function(*argv):  
    for arg in argv:  
        print(arg) 

my_function('Hello', 'World!')


def my_function(*argv):
  print(argv)

my_function('Hello', 'World!')


def my_function(*argv):
  print(argv[0])

my_function('Hello', 'World!')


def my_function(*ages):
  print("The older friend is " + ages[0] + " years")

my_function("13", "12", "11")