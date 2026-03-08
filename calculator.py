def get_numbers():
    raw = input("Enter numbers separated by spaces: ").strip()
    parts = raw.split()

    if len(parts) < 2:
        print("Please enter at least two numbers.")
        return None

    try:
        return [float(p) for p in parts]
    except ValueError:
        print("Invalid number input. Please try again.")
        return None


while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        continue

    numbers = get_numbers()
    if numbers is None:
        continue

    if choice == "1":
        result = sum(numbers)
        symbol = "+"
    elif choice == "2":
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        symbol = "-"
    elif choice == "3":
        result = 1
        for n in numbers:
            result *= n
        symbol = "*"
    else:
        result = numbers[0]
        valid = True
        for n in numbers[1:]:
            if n == 0:
                print("Cannot divide by zero.")
                valid = False
                break
            result /= n
        if not valid:
            continue
        symbol = "/"

    expression = f" {symbol} ".join(str(n) for n in numbers)
    print(f"Result: {expression} = {result}")