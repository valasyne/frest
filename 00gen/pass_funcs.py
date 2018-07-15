def methodception(another_func):
    return another_func()

def add_two_nums():
    return 23+57

# print(methodception(add_two_nums))

# print(methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 49, 484]
print(list(filter(lambda x: x>50, my_list)))

def over50(x):
    return x>50

print(list(filter(over50, my_list)))

print([x for x in my_list if x>50])

# print((lamdba x: x*3)(5))
#
# def f(x):
#     return x*3
#
# print(f(5))
