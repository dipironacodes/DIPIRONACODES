#1.
faturamento = [
 {"dia": "segunda", "valor": 1200},
 {"dia": "terça", "valor": 1500},
 {"dia": "quarta", "valor": 900},
 {"dia": "quinta", "valor": 1800},
 {"dia": "sexta", "valor": 2400},
]
faturamento_total = 0
for dia_faturamento in faturamento:
    faturamento_total += dia_faturamento ["valor"]
    print (f"Faturamento total da semana:R${faturamento_total:.2f}")
