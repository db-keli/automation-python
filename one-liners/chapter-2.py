# List Comprehension

# Native way of iterating through a dict
occupants = {'James': 700,
             'Bob': 789,
             'Joyce': 8983}

top_earners = []
# for key, val in occupants.items():
#     if val > 800:
#         top_earners.append((key, val))
[top_earners.append((key, val)) for key, val in occupants.items() if val > 800]
print(top_earners)

# Using list comprehensions

new_list = []
new_list.append([x*4 for x in range(5)])
print(new_list)

print([(x, y) for x in range(6) for y in range(7)])

print(([x % 2 for x in range(15) if x < 10]))

words = '''Mike comes home every time shit works on a silver kind of plater.
        Come lets do this fucking python'''
w = [[x for x in line.split() if len(x) > 4] for line in words.split('\n')]
print(w)

lines = []
with open('chapter-2.py') as f:
    for line in f:
        lines.append(line.strip().strip())
print(lines)


