def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    i = 0
    while i < len(my_list):
        if i != idx:
            new_list.append(my_list[i])
        i = i + 1
    my_list = new_list.copy()
    return my_list
