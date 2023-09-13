str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
new_list = list(map(lambda x: int(x), str_list))

square_items = list(map(lambda x: x ** 2, new_list))

create_dict = dict(zip(new_list, square_items))
print(create_dict)
