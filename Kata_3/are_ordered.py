def are_ordered(list_of_values):

    if list_of_values == []:
        return False
    
    for i in range(len(list_of_values)-1):
        if list_of_values[i] > list_of_values[i+1]:
            return False

    return True