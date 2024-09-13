#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if not (isinstance(num1, int) or isinstance(num1, float)):
                raise TypeError("wrong type")
            if not (isinstance(num2, int) or isinstance(num2, float)):
                raise TypeError("wrong type")
            result.append(num1 / num2)
        except IndexError:
            result.append(0)
            print("out of range")
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except TypeError:
            result.append(0)
            print("wrong type")
        finally:
            pass
    return result
