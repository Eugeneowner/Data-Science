import random
#Task 1
# name = input("Enter please name: ")

# salary_input = input("Enter your monthly salary in dollars: ")
# salary_input = salary_input.replace(" ", "")   
# monthly_salary = float(salary_input)

# annual_salary = monthly_salary * 12 / 1000

# print(f"Annual salary {name} comprises {annual_salary:.0f} thousand dollars.")


#Task 2
# value = input("Enter an integer between 100 and 999 to check if it is even: ")

# if value.isdigit():
#     number = int(value)
#     if 100 <= number <= 999 and number % 2 == 0:
#         print("The number is even and within the required range:", True)
#     else:
#         print("The number is either odd or outside the 100–999 range:", False)
# else:
#     print("Invalid input format. Please enter an integer.")

    #Task 3
# value = input("Please enter an integer between 101 and 999 (the last digit should not be 0): ")
# if value.isdigit():
#     number = int(value)
#     if 101 <= number <= 999 and number % 10 != 0:
#         reversed_number = int(value[::-1])
#         print("In reverse number:", reversed_number)
#     else:
#         print("Error: the number must be between 101 and 999 and not end with 0.")
# else:
#     print("Error: the value entered is not an integer.")

#Task 3_1
# while True:
#     number = random.randint(101, 999)
  
#     if number % 10 != 0:
#         break

# print("Random number:", number)

# reversed_number = int(str(number)[::-1])

# print("In reverse number:", reversed_number)


   #Task 4
# valuesFirst = int(input("Enter the first integer: "))
# valuesSecond = int(input("Enter the second integer: "))

# print("Sum:", valuesFirst + valuesSecond)
# print("Difference:", valuesFirst - valuesSecond)
# print("Multiplication:", valuesFirst * valuesSecond)
# print("Division:", valuesFirst / valuesSecond)
# print("Remainder:", valuesFirst % valuesSecond)
# print("valuesFirst >= valuesSecond:", valuesFirst >= valuesSecond)
   

# #Task 4_1
valuesFirst = input("Enter the first integer: ")
valuesSecond = input("Enter the second integer: ")


if valuesFirst.isdigit() and valuesSecond.isdigit():
    a = int(valuesFirst)
    b = int(valuesSecond)

    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Sum:", a + b)
        print("Difference:", a - b)
        print("Multiplication:", a * b)
        print("Division:", a / b)
        print("Remainder:", a % b)
        print("a >= b:", a >= b)

else:
    print("Invalid input: both values must be integers.")