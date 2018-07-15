def my_method(arg1, arg2):
    return arg1+arg2

# print(my_method(5, 6))

def my_long_method(arg1, arg2, arg3, arg4):
    return arg1 + arg2 + arg3 + arg4


def my_list_add(list_arg):
    return sum(list_arg)

# my_long_method(3,5,7,2)
# my_list_add([3,5,7,2])

def addition_simplified(*args):
    return sum(args)

# addition_simplified(3,5,2,4,9)
def what_are_kwargs(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

what_are_kwargs(12, 34, 56, name="Vassily", place="Minsk")
