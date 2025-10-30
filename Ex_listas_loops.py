# 1. Lista de Frutas:
frutas = ["maçã", "banana","Laranja","uva"]
# 2. 1 e último elemento:
print (f"O primeiro item é {frutas[0]}")
print (f"O último item é {frutas [-1]}")
# 3. add "Manga"
frutas.append ("manga")
# 4. remove banana
frutas.remove ("banana")
#5.substitua "laranja" por "abacaxi"
indice = frutas.index ("laranja")
frutas[2] = "Abacaxi"
#6. Lista Números 1 a 10
numeros = [1,2,3,4,5,6,7,8,9,10]
print (numeros)
#7. calc e print soma de todos
soma = sum(numeros)
print (soma)
#8. Encontre e imprima o maior e o menor número da lista
max(numeros)
min(numeros)
#9. Inverta a ordem dos elementos na lista e imprima a lista invertida
numeros.reverse()
print (numeros)
#10. Crie uma lista cidades contendo as seguintes cidades: "São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba".
cidades = ["São Paulo","Rio de Janeiro","Belo Horizonte","Curitiba"]
#11. Ordene a lista cidades em ordem alfabética.
sorted(cidades)
#12.Adicione a cidade "Porto Alegre" ao final da lista.
cidades.append ("Porto Alegre")
#13.Encontre o índice da cidade "Curitiba" na lista.
cidades.index("Curitiba")
#14.Remova a cidade "Rio de Janeiro" da lista.
numeros.remove ("Rio de Janeiro")
#15.Crie duas listas lista1 e lista2, onde lista1 contém os números [1, 2, 3] e lista2 contém os números [4, 5, 6].
lista1 = [1,2,3]
lista2 = [4,5,6]
#16.Concatene lista1 e lista2 em uma nova lista lista3.
lista3 = lista1 + lista2
#17 Imprima Lista 3
print (lista3)
#18.Crie duas listas animais_domesticos e animais_selvagens, onde animais_domesticos contém ["cachorro", "gato", "coelho"] e animais_selvagens contém ["leão", "tigre", "urso"].
animais_domesticos = ["Cachorro","Gato","Coelho"]
animais_selvagens = ["Leão", "Tigre", "Urso"]
#19.Concatene as duas listas em uma nova lista todos_animais.
todos_animais = animais_domesticos + animais_selvagens
#20. Imprima todos_animais.
print(todos_animais)
#21.Crie uma lista nomes contendo os nomes: "Ana", "Pedro", "Maria", "João".
nomes = ["Ana", "Pedro","Maria","João"]
#22.Utilize um loop for para imprimir cada nome da lista
for nome in nomes:
    print(nome)
#23.Crie uma nova lista nomes_maiusculos contendo os nomes da lista nomes em letras maiúsculas. Utilize um loop for para isso.
nomes_maiusculos = [nome.upper() for nome in nomes]
#24.Crie uma lista numeros contendo os números de 1 a 20. Utilize um loop for para imprimir apenas os números pares
num = list(range(1,21))
for numero in num:
    if numero % 2 == 0:
        print (numero)
#25.Usando a lista numeros, utilize um loop for para criar uma nova lista quadrados contendo o quadrado de cada número.               
quadrados = []                                                                                                                              
for numero in num:
    quadrados.append(numero ** 2)
print(quadrados)



