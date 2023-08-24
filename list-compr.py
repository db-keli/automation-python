Names = ['Mike', 'Richard', 'Joyce']

my_names = [n for n in Names]
print(my_names)

values = [1, 2, 3, 4]

my_digits = [i for i in values]
print(my_digits)

x = 1 if my_digits else 3
print(x)


def print_names(*args, **kwargs):
    for arg in args:
        print(f"My name is {arg}")
    for key, val in kwargs.items():
        print(f"{key} ---> {val}")


# def print_bio(**kwargs):
#     for key, val in kwargs.items():
#         print(f"{key} --> {val}")


print_names('Kofi', 'Mike', 'Peggy', 'Loyal', home="Obuasi", place="st. james")
