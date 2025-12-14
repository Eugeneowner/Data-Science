def sevenBoom():
    for number in range(1, 101):
        if number % 7 == 0 or '7' in str(number):
            print("BOOM")
        else:
            print(number)