def tipo_param(*args):
    for item in args:
        print(type(item))


tipo_param('ac', 1, 1.2, True)
