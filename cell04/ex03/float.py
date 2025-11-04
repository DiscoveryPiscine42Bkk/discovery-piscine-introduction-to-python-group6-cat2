def main():
    num_str = input("Give me a number: ")
    try:
        num = float(num_str)
    
        if num.is_integer():
            print("This number is an integer.")
        else:
            print("This number is a decimal.")
    except ValueError:
        print("That’s not a valid number!")

if __name__ == "__main__":
    main()
