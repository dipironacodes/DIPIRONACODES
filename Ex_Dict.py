#1.
aluno = {
    'nome':"Jõao Matheus",
    'idade':22,
    'curso': 'Ciência de Dados'
}
print (f"Nome: {aluno['nome']}")
print (f"idade: {aluno['idade']}")
print (f"Curso: {aluno['curso']}")

#2.
produto = {
    'nome' : "Teclado Mecânico",
    'preço': 350.00,
    'estoque': 10
}
produto [ "marca"] = "HyperX"
print (produto)
produto ["preço"] = 320.00
print (produto)
produto ["estoque"] = 8
print (produto)
del produto ["marca"]
print (produto)

#3
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
for nome, nota in notas.items():
    print (f"{nome} {nota}")
soma_das_notas = sum (notas.values())
quantidade_de_alunos = len(notas)
media_das_notas = soma_das_notas / quantidade_de_alunos
print (media_das_notas)

#4
numeros = {
    "a":10,
    "b":20,
    "c":30,
    "d":40,
    "e":50
}
soma_dos_numeros = sum (numeros.values())
print (soma_dos_numeros)
#5
lista = ["teclado","mouse","fone","teclado","teclado","mouse"]
contagem_lista={}
for item in lista:
    if item in lista:
        contagem_lista[item] += 1
    else:
        contagem_lista[item] = 1
print (lista)
print(contagem_lista)


           
