import sys

def append_it():

    parameters = sys.argv[1:]
    num_parameters = len(parameters)

    if num_parameters == 0:
        print("none")
        return

    for param in parameters:
 
        if param.endswith("ism"):

            continue 
        else:

            print(param + "ism")

if __name__ == "__main__":
    append_it()