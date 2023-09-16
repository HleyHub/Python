# try:
#       print("my_string"[1/0])
# except IndexError:
#       print("index error")
# except ZeroDivisionError:
#       print("zero error")
# except:
#       print("other error")


# # This code will throw index error
# list1 = [1, 2, 3, 4]
# list1[4]


# x = 5
# y = "Sally"
# print(str(x) + y)


# try:
#       x = y + 1
# except NameError:
#     print("y is not defined") 

# try:
#       x = 'seasalt'[7]
# except IndexError:
#       print("No character found in that index")

# try:
#       x = 'y' + 1
# except ValueError:
#       print("y is not a number value")


# flowers = ['roses', 'daisies', 'dahlias', 'camellias']
# i = 0
# while True:
#     try:
#         print(flowers[i])
#         i += 1
#     except IndexError:
#         break


# a = input("Enter a number: ")
# try:
#     float(a) / 0
# except (TypeError, ZeroDivisionError):
#     print("Please enter valid numbers, besides zero.")


# try:
#     y = 5 / 0
# except ZeroDivisionError:
#     print("Can't divide with zero.")

# try:
#     y = 5 / 0
# except BaseException:
#     print("Can't divide with zero.")


try:
    z = 3 // 0
except ZeroDivisionError:
    print("Zero won't work!")
except ArithmeticError:
    print("We have a problem!")












