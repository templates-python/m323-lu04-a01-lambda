add = lambda a, b: a + b  # Funktion zum Addieren zweier Zahlen

subtract = lambda a, b: a - b  # Funktion zum Subtrahieren zweier Zahlen

multiply = lambda a, b: a * b  # Funktion zum Multiplizieren zweier Zahlen

divide = (
    lambda a, b: a / b if b != 0 else 'Division durch Null ist nicht erlaubt!'
)  # Funktion zum Teilen zweier Zahlen


if __name__ == '__main__':

    # Testen Sie Ihre Funktionen hier
    print(add(5, 10))
    print(subtract(10, 5))
    print(multiply(3, 4))
    print(divide(15, 3))
