# app.py - Une application simple de calculatrice
def add(a, b):
    """Additionner deux nombres"""
    return a + b


def subtract(a, b):
    """Soustraire deux nombres"""
    return a - b


def multiply(a, b):
    """Multiplier deux nombres"""
    return a * b


def divide(a, b):
    """Diviser deux nombres"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Fonction principale pour démontrer"""
    print("Bienvenue dans la calculatrice !")
    print(f"2 + 2 = {add(2, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"10 / 2 = {divide(10, 2)}")


if __name__ == "__main__":
    main()
