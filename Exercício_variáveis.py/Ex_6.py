nome = str (input("Digite seu nome completo:"))
print (nome)
nome_maiusculas = nome.upper()
print (nome_maiusculas)
primeiro_nome = nome.split()[0]
print (primeiro_nome)
nome_sem_espacos = nome.replace(" ", "")
quantidade_letras = len(nome_sem_espacos)
print(quantidade_letras)
