list_a = [100, 200, -10]
list_b = [False, False, True]

for i in range(len(list_a)):
    print(i, list_a[i], list_b[i])

print("")


# values for multiple iterables
for val_a, val_b in zip(list_a, list_b):
    print(val_a, val_b)

print("")

# index and value
for i, val in enumerate(list_a):
    print(i, val)

print("")

# index and values for multiple iterables
for i, (val_a, val_b) in enumerate(zip(list_a, list_b)):
    print(i, val_a, val_b)
