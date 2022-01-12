def list_max(input_list):
    max_value = input_list[0]

    for i in range(1, len(input_list)):
        if input_list[i] > max_value:
            max_value = input_list[i]

    print(max_value)


list_1 = [123, -13, 31, -32, 12]
list_max(list_1)
list_2 = [32, -123, 45, 46, 39]
list_max(list_2)
