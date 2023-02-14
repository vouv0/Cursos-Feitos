def converte(str1, str2):
    try:
        num1 = float(str1)
        num2 = float(str2)
        print(num1 + num2)
    except:
        raise Exception('Falha nos valores')
    finally:
        print('Fim!')

converte('1', '2')
