def findNumbers():
    while True:
        a = input("Enter the first number: ")
        if a.isdigit():
            a = int(a)
            break
        else:
            print("Invalid input. Please enter an integer.")

    # Ввод второго числа
    while True:
        b = input("Enter the second number: ")
        if b.isdigit():
            b = int(b)
            break
        else:
            print("Invalid input. Please enter an integer.")

    while True:
        c = input("Enter the third number: ")
        if c.isdigit():
            c = int(c)
            break
        else:
            print("Invalid input. Please enter an integer.")

  
    minimum = min(a, b, c)
    maximum = max(a, b, c)
    middle = a + b + c - minimum - maximum

    return minimum, middle, maximum