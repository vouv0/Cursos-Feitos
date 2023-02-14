from math import sqrt, pow

def bhaskara():
    a = int(input('Insira o valor de a: '))
    b = int(input('Insira o valor de b: '))
    c = int(input('Insira o valor de c: '))
    delta = pow(b, 2) - (4 * a * c)
    x1 = ((-b) + sqrt(delta)) / (2 * a)
    x2 = ((-b) - sqrt(delta)) / (2 * a)
    print(f"x' = {round(x1, 3)}")
    print(f"x'' = {round(x2, 3)}")


bhaskara()

