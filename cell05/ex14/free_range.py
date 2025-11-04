import sys

def free_range():

    if len(sys.argv) != 3:
      
        print("none")
        return

    try:

        start = int(sys.argv[1])
        end = int(sys.argv[2])

        result_array = list(range(start, end + 1))

        print(result_array)

    except ValueError:

        print("none")

if __name__ == "__main__":
    free_range()