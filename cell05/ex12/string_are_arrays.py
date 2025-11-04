import sys

def string_are_arrays():

    # [cite: 441, 444]
    if len(sys.argv) != 2:
        print("none")
        return

    input_string = sys.argv[1]
  
    z_count = 0
    for char in input_string:
        if char == 'z':
            z_count += 1
            
    if z_count == 0:
    
        print("none")
    else:
    
        print('z' * z_count)

if __name__ == "__main__":
    string_are_arrays()