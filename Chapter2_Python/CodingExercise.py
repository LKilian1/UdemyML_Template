import matplotlib.pyplot as plt
import numpy as np


def e_function(my_list):
    my_result = []

    for val in my_list:
        my_result.append(np.exp(val))

    return my_result


my_list = [1, 2, 3, 4, 5, 6]
e_list = e_function(my_list)

plt.plot(my_list, e_list, color="red")
plt.xlabel("x")
plt.ylabel("e(x)")
plt.show()
