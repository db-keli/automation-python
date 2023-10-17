# List Comprehension

# Native way of iterating through a dict
occupants = {'James': 700,
             'Bob': 789,
             'Joyce': 8983}

top_earners = []
for key, val in occupants.items():
    if val > 800:
        top_earners.append((key, val))

print(top_earners)

# Using list comprehensions

new_list = []
new_list.append([x*4 for x in range(5)])
print(new_list)

print([(x, y) for x in range(6) for y in range(7)])

print(([x % 2 for x in range(15) if x < 10]))
