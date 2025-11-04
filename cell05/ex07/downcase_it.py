import sys

if len(sys.argv) != 2:

    print("none")
else:
    input_string = sys.argv[1]
    
    lowercase_string = input_string.lower()
    
    print(lowercase_string)