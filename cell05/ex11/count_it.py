import sys

def count_it():

    parameters = sys.argv[1:]
    num_parameters = len(parameters)

    if num_parameters == 0:
        print("none")
        return

    print(f"parameters: {num_parameters}")
   
    for param in parameters:
        param_length = len(param)
        print(f"{param}: {param_length}")

if __name__ == "__main__":
    count_it()