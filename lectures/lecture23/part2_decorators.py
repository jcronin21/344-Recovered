from datetime import datetime
import json
from flask import Response, request


# ###################################
# # Example 4: Your First Decorator #
# ###################################
# '''
# * A decorator takes a function as an argument, 
#   and then wraps some functionality around it.
# * Useful for error checking and security
# '''
# def my_decorator(func):
#     def wrapper(name):
#         print("Something is happening before the function is called.")
#         func(name)
#         print("Something is happening after the function is called.")
#     return wrapper

# # Syntax 1:
# def say_hi(name):
#     print('Hi ' + name)

# def say_bye(name):
#     print('Bye ' + name)

# say_hi_plus_extras = my_decorator(say_hi)
# say_bye_plus_extras = my_decorator(say_bye)

# print(say_hi_plus_extras)
# print(say_bye_plus_extras)
# say_hi_plus_extras('Curly')
# say_bye_plus_extras('Moe')


# # Alternative syntax:
# @my_decorator
# def say_hi(name):
#     print('Hi ' + name)

# @my_decorator
# def say_bye(name):
#     print('Bye ' + name)

# say_hi('Curly')
# say_bye('Moe')


# ############################
# # Example 5: args & kwargs #
# ############################
# '''
# Sometimes you want to use a decorator but you don't know 
# how many arguments the inner function will have. If this
# is the case, you can use "args" and "kwargs".

# * args hold a list of any positional parameters
# * kwargs hold a dictionary of any keyword parameters.

# Using this strategy, you can apply your decorator to
# multiple functions with different function signatures. 
# '''
# def security(func):
#     def wrapper(username, *args, **kwargs):
#         if username == 'sjv':
#             # pass all of the arguments to the inner function
#             func(username, *args, **kwargs)
#         else:
#             print('Unauthorized')
#     return wrapper

# @security
# def query_users(username, limit=5, order_by='last_name'):
#     print('filter criteria:', username, limit, order_by)

# @security
# def query_posts(username, before_date=datetime.now()):
#     print('filter criteria:', username, before_date)

# print('\nquerying users table...')
# query_users('sjv', limit=10)

# print('\nquerying posts table...')
# query_posts('hjv4599')


# #######################################
# # Example 6: Flask + SQL Alchemy Demo #
# #######################################
# def id_is_integer_or_400_error(func):
#     def wrapper(self, id):
#         try:
#             int(id)
#             return func(self, id)
#         except:
#             return Response(
#                 json.dumps({'message': '{0} must be an integer.'.format(id)}), 
#                 mimetype="application/json", 
#                 status=400
#             )
#     return wrapper

# def handle_db_insert_error(func):
#     def wrapper(self):
#         try:
#             return func(self)
#         except:
#             import sys
#             db_message = str(sys.exc_info()[1]) # stores DB error message
#             print(db_message)                   # logs it to the console
#             message = 'Database Insert error. Make sure your post data is valid.'
#             post_data = request.get_json()
#             post_data['user_id'] = self.current_user.id
#             response_obj = {
#                 'message': message, 
#                 'db_message': db_message,
#                 'post_data': post_data
#             }
#             return Response(json.dumps(response_obj), mimetype="application/json", status=400)
#     return wrapper