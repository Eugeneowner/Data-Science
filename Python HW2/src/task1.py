def enterNumber(number: int):
    if number % 3 == 0 and number % 5 == 0:
        return "ham"
    elif number % 3 == 0:
        return "foo"
    elif number % 5 == 0:
        return "bar"
    else:
        return None