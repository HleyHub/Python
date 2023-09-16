# def my_function():
#   def my_inner_function():
#     x = 20
#     print(x)
#   my_inner_function()

# my_function()


# def my_function():
#   global x
#   x = 30

# my_function()
# print(x)


# def myfunc():
#   a = 20
#   print(a)

# myfunc()


## This will throw an error because a is not defined globally
# def myfunc():
#   a = 20

# myfunc()
# print(a)


# x = 20
# def my_function():
#   x = 30
#   print(x, end=' ')

# my_function()
# print(x, end=' ')


## This will throw an error because x is not defined globally
# def my_function():
#   def my_inner_function():
#     x = 20
#   print(x)
#   my_inner_function()

# my_function()


# x = 30
# def my_function():
#   global x
#   x = 20

# my_function()
# print(x)


# x = 20
# def my_function():
#   print(x, end=' ')

# my_function()
# print(x, end=' ')


def my_function():
  x = 20
  def my_inner_function():
    print(x)
  my_inner_function()
my_function()


x = 20
def my_function():
  x = 30
  print(x, end=' ')

my_function()
print(x, end=' ')