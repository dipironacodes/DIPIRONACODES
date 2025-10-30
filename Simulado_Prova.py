#1.
preço_produtos = [27,90,100,53,39,47,12,50]
valor_da_compra = sum(preço_produtos)
print (f"{valor_da_compra}")

#2.
estoque = {"notebook":5,"mouse":12,"teclado":8}
estoque["monitor"] = 3
print (estoque)

#3.
nota_final = float(input(print("Digite a sua nota final:")))
if nota_final >= 7:
    print("Aprovado")
elif nota_final>=5 and nota_final<=6.9:
    print("Recuperação")
else:
    print ("Reprovado")

#4.
cidades = ["São Paulo","Nova York","Rio de Janeiro","Chicago","Brasília","Los Angeles"]
contador_brasil = 0 
cidades_brasil = "São Paulo", "Rio de Janeiro", "Brasília"
for cidade in cidades:
    if cidade in cidades_brasil:
        contador_brasil += 1
print (cidades)
print (contador_brasil)


#5.
avaliacoes = {
    "Norte":[7,8,6,5,9],
    "Sul":[8,9,7,10,6],
    "Sudeste":[9,8,9,10,9]
}
for regiao, notas in avaliacoes.items():
    soma_notas = sum(notas)
    quantidade_avaliacoes = len(notas)
    media = soma_notas / quantidade_avaliacoes
    print (f"Média da região {regiao}:{media:.2f}")


