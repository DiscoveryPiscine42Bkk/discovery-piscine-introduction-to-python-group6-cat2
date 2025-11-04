def main():
    print("Enter a number")
    try:
        number = int(input())
        for i in range(10):
            print(f"{i} x {number} = {i * number}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
