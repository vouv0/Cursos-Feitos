import pandas as pd

data = pd.DataFrame({
    'Sede': ['Nova Iorque', 'São Paulo', 'Nova Iorque', 'Londres', 'Londres'],
    'Piloto': ['Mike Ross', 'Sebastian Thomas', 'Glen Are','Michael Schum', 'Luiz da Silva'],
    'Mundiais': [10, 11, 0, 3, 44],
    'Vitórias': [321, 229, 12, 44, 1023]
}, index=['X Racing', 'Equatorial', 'Typo', 'Blue Race', 'Capa Racing'])

data.at['X Racing', ['Sede', 'Vitórias']] = ('São Paulo', 322)

print(data)
