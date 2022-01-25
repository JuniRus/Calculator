# Запуск цикла
while True:
    # Выбор операции и возможность выйти из цикла.
    print("Введите в любой стороке 'exit' для выхода из калькулятора.")
    operation = input("Выберите одну из операций ('+', '-', '*', '/'): ")
    
    if operation == 'exit':
        break
    # Ввод чисел. Если в одной из сточек будет введено 'exit', то 
    #  произойдёт выход из цикла.
    # Если в одном чисел будет введён текст, то выведется ошибка.
    try:
        first_number = int(input("Введите первое число: "))
    except ValueError:
        print("Произошла ошибка: вы ввели текст вместо числа.")
        print('\n')
        continue
    if first_number == 'exit':
        break
    
    try:
        second_number = int(input("Введите второе число: "))
    except ValueError:
        print("Произошла ошибка: вы ввели текст вместо числа.")
        print('\n')
        continue
    if second_number == 'exit':
        break
    
    # Выполнение арифметический действий с числами:
    if operation == '+':
        answear = first_number + second_number
        print(f"Ответ: {answear}")
    elif operation == '-':
        answear = first_number - second_number
        print(f"Ответ: {answear}")
    elif operation == '*':
        answear = first_number * second_number
        print(f"Ответ: {answear}")
    elif operation == '/':
        # Предотвращение ошибки при делении на ноль:
        try:
            answear = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("Делить на ноль нельзя!")
        else:
            print(f"Ответ: {answear}")
    else:
        print("Произошла ошибка: выбрана неверная операция!")
    print('\n')