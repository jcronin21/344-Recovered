
# # Decorator Format:
# # https://realpython.com/primer-on-python-decorators/

# #########################################
# # Example 1: Functions can be arguments #
# #########################################
# # Say you have two greetings and you want a 
# # convenient way to use either:

# def greeting1(name):
#     return "Hello, {0}".format(name)

# def greeting2(name):
#     return "What up, {0}".format(name)

# def greet(greeter_func, name):
#     print(greeter_func(name))

# greet(greeting1, 'Bob')
# greet(greeting2, 'Maria')


# ###########################################
# # Example 2: Functions can be defined and # 
# # invoked inside of other functions.      #
# ###########################################
# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# parent()


# ###############################
# # Example 3: Functions can be # 
# # returned and invoked later. #
# ###############################
# def parent(num):
#     def first_child(name):
#         return "Hi, I am " + name

#     def second_child(name):
#         return "Call me " + name

#     if num == 1:
#         # returns a function
#         return first_child
#     else:
#         # returns a function
#         return second_child

# f1 = parent(1)
# f2 = parent(2)

# print(f1)
# print(f2)
# print(f1('Emma'))
# print(f2('Liam'))