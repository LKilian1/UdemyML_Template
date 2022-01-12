for i in range(1, 6):
    for j in range(1, 6):
        if(i == 1 or i == 5):
            print(j, end="")
        elif(j == 6 - i):
            print(6 - i, end="")
        else:
            print(" ", end="")
    print()
