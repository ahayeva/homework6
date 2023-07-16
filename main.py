if __name__ == "__main__":
    # ВПРАВА 1

    numberOne = input("Введіть перше число")
    numberTwo = input("Введіть друге число")
    numberThree = input("Введіть третє число")
    число = int(numberOne + numberTwo + numberThree)
    print("створене число", число)
   # ВПРАВА 2
    number = int(input("введіть чотиризначне число: "))
    product = 1
    while number > 0:
     digit = number % 10
    product *= digit
    number //= 10
    print("добуток цифр:", product)
   # EXERcISE 3
    meters = float(input("Введіть кількість метрів: "))
    sm = meters * 100
    decimeters = meters * 10
    milimitr = meters * 1000
    miles = meters/ 1609
    print("У сантиметрах:", sm)
    print("У дециметрах:", decimeters)
    print("У міліметрах:", milimitr)
    print("У милях:", miles)
    # ВПРАВА 4

    size = float(input("Введіть розмір основи трикутника: "))
    height = float(input("Введіть розмір висоти трикутника: "))
    площа = 0, 5 * розмір * висота
    # print("Площа трикутника:", area)
    # EXERSISE 5
    number = int(input("Введіть чотиризначне число: "))
    reverse_number = int(str(number)[::-1])
    print("Resultat:", reverse_number)