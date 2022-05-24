import shelve as sh

file_name = "Cur_params"


def bin_first_in(*args):
    
    with sh.open(file_name, "n") as data:
        data["start_value"] = args[0]
        data["accuracy"] = args[1]
        data["function"] = args[2]
    
    
def bin_first_out():
    try:
        with sh.open(file_name, "r") as data:
           data_ = [data["start_value"], data["accuracy"], data["function"]]
        return data_
    except:
        return[0, 0.0, ""]
   

'''
def bin_second_in(*args):
    with sh.open(file_name_, "n") as data:
        data["start_value"] = args[0]
        data["value"] = args[1]
        data["step"] = args[2]
        data["flag for lb"] = args[3]
        data["color"] = args[4]


def bin_second_out():
    with sh.open(file_name_, "r") as data:
        data_ = [data["start_value"], data["value"], data["step"], data["flag for lb"], data["color"]]
    return data_
'''