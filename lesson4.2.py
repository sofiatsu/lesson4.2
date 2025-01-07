lst_a = [2, 4, 5, 9, 1]

for lst_b in lst_a:
    if lst_a:
        ind = sum(lst_a[0::2])
        result = ind * lst_a[-1]
    else:
        result = 0
print(result)