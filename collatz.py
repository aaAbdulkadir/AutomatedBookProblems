"""
collatz - If number is even:
                print number // 2

          If number is odd:
                print  3 * number + 1
"""

while True:
    try:
        number = int(input("number: "))

        while number > 1:
            if number % 2 == 0:
                number = number // 2
                print(number)
            elif number % 2 == 1:
                number = 3 * number + 1
                print(number)

    except ValueError:
        print("Number only")