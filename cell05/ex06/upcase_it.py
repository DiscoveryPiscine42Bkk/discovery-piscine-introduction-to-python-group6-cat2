import sys

if len(sys.argv) == 2:

    input_string = sys.argv[1]
    
    uppercase_string = input_string.upper()

    print(uppercase_string)
else:
    print("none")