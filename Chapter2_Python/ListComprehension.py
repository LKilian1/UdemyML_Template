# Methode 1
list_a = []

for i in range(100):
    list_a.append(5)

print("")

# Methode 2
list_b = [5 for i in range(100)]
print(list_b)

print("")

# oder
list_c = [i**2 for i in range(100)]
print(list_c)
