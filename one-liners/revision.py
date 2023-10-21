dictionary = {
    'James' : 500,
    'John' : 700,
    'Adiza' : 900
}

top_earners = []

[top_earners.append((key, value)) for key, value in dictionary.items() if value > 600]
print(top_earners)


[print(f'{key} is available with an amount of {value}') for key, value in dictionary.items() if key is not None]