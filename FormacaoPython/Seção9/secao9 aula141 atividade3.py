def print_digitado():
    try:
        txt = input('Digite um texto: ')
        return txt
    except KeyboardInterrupt:
        return None


print(print_digitado())