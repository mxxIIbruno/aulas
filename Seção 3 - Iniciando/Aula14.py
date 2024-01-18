from datetime import datetime

# Obtendo a data atual
current_date = datetime.now()

# Exemplo básico
print(f"Atualmente é {current_date}")

# Formatando a data de maneira específica
print(f"Data formatada: {current_date:%Y-%m-%d %H:%M:%S}")

# Extraindo componentes individuais da data
print(f"Ano: {current_date.year}, Mês: {current_date.month}, Dia: {current_date.day}")

# Calculando a diferença entre duas datas
other_date = datetime(2020, 1, 1)
difference = current_date - other_date
print(f"Diferença entre as datas: {difference}")
