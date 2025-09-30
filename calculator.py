def get_number(prompt):
    """Функция для безопасного ввода числа"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите число!")

def get_operation():
    """Функция для ввода операции"""
    while True:
        operation = input("Введите операцию (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        print("Ошибка: доступные операции: +, -, *, /")

def calculate(num1, num2, operation):
    """Функция для выполнения вычислений"""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Деление на ноль невозможно!")
        return num1 / num2

def main():
    """Основная функция программы"""
    print("=== Простой калькулятор ===")
    print("Доступные операции: +, -, *, /")
    
    try:
        # Ввод данных
        num1 = get_number("Введите первое число: ")
        operation = get_operation()
        num2 = get_number("Введите второе число: ")
        
        # Вычисление
        result = calculate(num1, num2, operation)
        
        # Вывод результата
        print(f"Результат: {num1} {operation} {num2} = {result}")
        
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()