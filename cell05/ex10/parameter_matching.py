import sys

def parameter_matching():
   
    if len(sys.argv) != 2:
        print("none")
        return

    expected_parameter = sys.argv[1]
    
    try:
        user_input = input("What was the parameter? ")
    except EOFError:
     
        user_input = "" 

    if user_input == expected_parameter:
        print("Good job!")
    else:
    
        print("Nope, sorry...")

if __name__ == "__main__":
    parameter_matching()