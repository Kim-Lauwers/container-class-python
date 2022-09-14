number_list = [10, 20, 33, 46, 55, 13, 15, 88, 99, 156, 321564, 32165, 798, 4987, 99496, 98789195]

result = list(filter(lambda x: (x % 5 == 0), number_list))

print(result)
