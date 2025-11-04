import sys

def aff_rev_params():
   
    if len(sys.argv) <= 2:
        print("none")
    else:
       
        for param in parameters[::-1]:
            print(param)

if __name__ == "__main__":
    aff_rev_params()