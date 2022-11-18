def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def percentage(x, y):
  return (x * y) / 100.0


print("Selecione a operação.")
print("1.+")
print("2.-")
print("3.*")
print("4./")
print("5.^")
print("6.%")

while True:
    # take input from the user
    choice = input("Escolha (1/2/3/4/5/6): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6'):
        num1 = float(input("Primeiro Número: "))
        num2 = float(input("Segundo Número: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(pow(num1,num2))

        elif choice == '6':
            print(num1, "%", num2, "=", percentage(num1, num2))

        next_calculation = input("Repetir? (s/n): ")
        if next_calculation == "n":
            break

    else:
        print("Inválido")
