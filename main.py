if __name__ == "__main__":
    #EXERCISE 1
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    num3 = float(input("Введіть третє число: "))
    operation = input("Виберіть операцію (сума або добуток): ")
    if operation == "сума":
        result = num1 + num2 + num3
        print("Сума чисел:", result)
    elif operation == "добуток":
        result = num1 * num2 * num3
        print("Добуток чисел:", result)
    else:
        print("Невірнo")
        #EXERCISE 2
        num1 = float(input("vvedit pershe chyslo: "))
        num2 = float(input("vvedit druhe cheslo: "))
        num3 = float(input("vvedit trete chyclo: "))
        operation = input("Виберіть операцію (максимум, мінімум або середнє): ")
        if operation == "максимум":
            result = max(num1, num2, num3)
            print("Максимум:", result)
        elif operation == "мінімум":
            result = min(num1, num2, num3)
            print("minimum:", result)
        elif operation == "середнє":
            result = (num1 + num2 + num3) / 3
            print("Середнє:", result)
        else:
            print("Невірна операція")
            #EXERCISE 3
            meters = float(input("Введіть кількість метрів: "))
            unit = input("Виберіть одиницю вимірювання (милі, дюйми або ярди): ")
            if unit == "милі":
                result = meters / 1609.34
                print("Милі:", result)
            elif unit == "дюйми":
                result = meters * 39.37
                print("Дюйми:", result)
            elif unit == "ярди":
                result = meters * 1.09361
                print("рди:", result)
            else:
                print("Невірна одиниця вимірювання")