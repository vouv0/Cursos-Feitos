import re

texto = '999 - 142'

info = re.search("^ *(\d+ *(-|\+) *\d+) *$", texto)

if info != None:
    print(f'Expressão "{texto}" é válida.')

else:
    print(f'"{texto}" não é uma expressão válida.')
