import functools

# Usage of decorators with args:
# * provide user permissions
# * insert elements into db (if they match)
def decorator_w_args(number):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("The decorator starts!")
            if number==56:
                print("Not running the function!")
            else:
                print("The number is not 56")
                print("Running the function")
                func(*args, **kwargs)
            print("The decorator ends!")
        return wrapper
    return my_decorator


@decorator_w_args(32)
def my_function_too(x, y):
    print("Hello!")
    print(f"The sum is: {x+y}")

my_function_too(57, 67)


# version 1
# import functools
#
# def my_decorator(func):
#     @functools.wraps(func)
#     def wrapper():
#         print("In the decorator!")
#         func()
#         print("After the decorator")
#     return wrapper
#
# @my_decorator
# def my_function():
#     print("I'm the function")
#
#
# my_function()
