def sum_digits(input):

    if input is None:
        return None  

    return sum(int(digit) for digit in str(input) if digit.isdigit())