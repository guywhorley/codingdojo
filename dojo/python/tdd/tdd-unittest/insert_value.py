def insert_value_at(index, my_list, value):
    if index < 0:
        return False
    elif not my_list:
        return False
    elif (index < 0) or (index > len(my_list)):
        return False
    else:
        my_list.insert(index, value)
        return my_list
