# name = input("Enter please name: ")

# salary_input = input("Enter your monthly salary in dollars: ")
# salary_input = salary_input.replace(" ", "")   
# monthly_salary = float(salary_input)

# annual_salary = monthly_salary * 12 / 1000

# print(f"Annual salary {name} comprises {annual_salary:.0f} thousand dollars.")

value = input("Enter an integer between 100 and 999 to check if it is even: ")

if value.isdigit():
    number = int(value)
    if 100 <= number <= 999 and number % 2 == 0:
        print("The number is even and within the required range:", True)
    else:
        print("The number is either odd or outside the 100–999 range:", False)
else:
    print("Invalid input format. Please enter an integer.")