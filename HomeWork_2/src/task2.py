import random

def randomNumbers():
    numbers = [
        random.randint(100, 1000),
        random.randint(100, 1000)
    ]

    print("Generated numbers:", numbers)

    if numbers[0] > numbers[1]:
        return f"{numbers[0]} > {numbers[1]}"
    elif numbers[0] < numbers[1]:
        return f"{numbers[1]} > {numbers[0]}"
    else:
        return "Both numbers are equal."