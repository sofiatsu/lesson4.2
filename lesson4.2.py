lst = [1, 2, 3, 6]

if lst:
    for num in lst:
        result = sum(lst[0::2]) * lst[-1]
else:
    result = 0

print(result)
