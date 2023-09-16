def fullname_func(fname):
  print(fname + " Mark")

fullname_func("John")


a = 0
def add_three(a):
	return a+3

result = add_three(a)
print(result)


def add_func(num1,num2):
    return num1 + num2 
		
print ( add_func(5 , 5) )


a = 0
def add_three(a):
	return a+3

result = add_three(3)
print(result)


nums= [7,4,1]
def change_third_item(list):
	list[2] = 5

change_third_item(nums)
print(nums)


def fullname_func(fname, lname):
  print(fname + " " + lname)

fullname_func("John", "Mark")


def print_name_age(name, age=19):
    print(name, age)

print_name_age('john', 18)


def my_function(*friends):
  print("The tallest student is " + friends[0])

my_function("john", "Ella", "mark")