nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# The List comprehension way!
my_list = [n*n for n in nums]
print(my_list)

my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# The List Comprehension way!
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

Names = ['Mike', 'Owuraku', 'Peggy', 'Jennifer']
my_names = [n for n in Names]
print(my_names)
