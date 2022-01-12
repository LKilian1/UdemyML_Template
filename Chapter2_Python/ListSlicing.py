list_a = [i for i in range(10)]

print(list_a)


# Methode 1 (zu viele Zeilen)
list_b = []

print("")

for i in range(3):
    list_b.append(list_a[i])

print(list_b)

# Methode 2 mit ListComprehension

list_c = [list_a[i] for i in range(3)]

print(list_c)


# Slicing
#                Start:Stop:Step
list_d = list_a[0:3:1]

print(list_d)
