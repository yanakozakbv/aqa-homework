"""
Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу
, що складається з числа, оператора (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).

Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
Якщо введені числа не можуть бути float спіймайте ValueError
Також ловіть помилку при діленні на 0
В кожній спійманій помилці друкуйте пояснення, що пішло не так
За допомогою циклів (while + counter) або (for + in range) надайте три спроби скористуватись калькулятором, якщо введені не вірні дані
Використати всі блоки try, except, else, finally. В finally можна надрукувати за скільки спроб виконавлась формула
Результат виконання формули - float число з двома знаками після крапки
"""


class WrongOperatorError(Exception):
    pass


class FormulaError(Exception):
    pass


counter = 0
success = False

while counter < 3:
    try:
        pr = input("Please enter your operation:")
        pr_split = pr.split()

        if len(pr_split) != 3:
            raise FormulaError('The number of entered elements should be 3')

        num1 = float(pr_split[0])
        num2 = float(pr_split[2])
        operations = ['*', '/', "+", "-"]

        result = 0
        if pr_split[1] in operations:
            if pr_split[1] == '+':
                result = num1 + num2
            elif pr_split[1] == '*':
                result = num1 * num2
            elif pr_split[1] == '/':
                result = num1 / num2
            elif pr_split[1] == '-':
                result = num1 - num2
        else:
            raise WrongOperatorError('Operator is not correct')

        print('{:.2f}'.format(result))
        success = True
        break
    except ZeroDivisionError as error:
        print('Division by 0 is prohibited')
    except FormulaError as error:
        print(error)
        print('Enter the right formula')
    except ValueError:
        print('You may entered not a number')
        print('Please enter a number')
    except WrongOperatorError as error:
        print(error)
        print('Enter the right operator')
    finally:
        counter += 1
print('Attempts count: ', counter) if success else print('Sorry, too many failed attempts')