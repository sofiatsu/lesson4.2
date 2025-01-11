lst = [0]

if lst:
    for num in lst:
        ind = sum(lst[0::2])
        result = ind * lst[-1]
else:
    result = 0

print(result)
