#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    '''This function divides one list by another list'''
    list_3 = []

    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:  # if the current index isn't an int or float
            print("wrong type")
            result = 0
        except ZeroDivisionError:  # if my_list_2[i] == 0
            print("division by 0")
            result = 0
        except IndexError:  # if one of the list is smaller than the other one
            print("out of range")
            result = 0
        finally:
            list_3.append(result)
    return (list_3)
