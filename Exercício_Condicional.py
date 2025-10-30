# 1. Par ou Ímpar:
num = int( input("Insira um Número"))
if num % 2 == 0:
      print("Esse Número é Par")
else:
      print("Esse Número é Ímpar")

# 2. Aprovado ou Reprovado: 
ap1 = float (input( "Digite sua nota da AP1"))
ap2 = float (input ( "Digite sua nota da AP2"))
ac = float ( input ( "Digite sua nota da AC"))
media = 0.4 * ap1 + 0.4 * ap2 + 0.2 * ac 
if media >= 7:                        
    print ("Aprovado")
else:
         print ("Reprovado") 

# 3. Cálculo de Desconto:
valor = float (input ("Digite o Valor da sua compra"))
if valor > 100:
    desconto = valor * 0.1 
    preço_final = valor - desconto 
    print ("Sua compra deu:"(preço_final))
else:
      preço_final = valor 
      print ("Sua compra deu:"(preço_final))  

# 4. Conversão de Temperatura: 
c = float (input ("Digite a temperatura em Celsius:"))
f = (c*9/5) + 32
print (f"A temperatura em fahrenheit é:{f}") 

# 5. Maior número (Dois valores):
num_1 = int ( input ("Digite o primeiro número:"))
num_2 = int ( input ("Digite o segundo número:"))
if num_1 > num_2:
      print ("O primeiro número é maior.")
if num_2 > num_1:
      print ("O segundo número é maior.")
if num_1 == num_2:
      print ("Os números são iguais.") 

# 6. Maior número (Três valores):
num1 = int (input ("Digite o primeiro número:"))
num2 = int (input("Digite o segundo número:"))
num3 = int (input("Digite o terceiro número:"))
if num1 > num2 and num1 > num3:
      print ("O primeiro número é o maior.")
if num2 > num1 and num2 > num3:
      print("O segundo número é o maior.")
if num3 > num1 and num3 > num2:
      print ("O terceiro número é o maior.")
if num1 == num2 == num3:
      print ("Os números são iguais")

# 7. Calculadora Simples: 
num1 = float (input ("Digite o primeiro número:"))
num2 = float (input ("Digite o segundo número"))
op = str (input ("Digite a operação desejada:"))
if op == "+":
      print (f"A soma é:{num1 + num2}")
elif  op == "-":
      print (f"A subtração é:{num1 - num2}")
elif op == "*":
      print (f"A multiplicação é:{num1 * num2}")
elif op == "/":
      if num2 == 0:
            print ("Erro: Divisão por 0 é indeterminada.")
      else:
           print (f"A divisão é:{ num1 / num2 }")      
elif op != "+" or "-" or "*" or "/":      
      print ("Digite um operação válida")
      


#9. Ano Bissexto:
ano = int (input ("Digite o ano:"))
if ano % 4 == 0:
    print("É um ano Bissexto")
else:
      print (" Não é um ano bissexto")

#10. Intervalo de idade:
idade = int (input("Digite sua idade:"))
if idade >= 18 and idade <= 65:
      print("Dentro da faixa permitida")
else:
      print("Fora da faixa permitida")

# 11. Acesso ao sistema:
user = input("Digite o usuário:")
password = input ("Digite a senha:")
if user == "Fred" and password == "1234":
      print("Acesso Permitido")
else:
      print ("Acesso negado")

# 12. Voto Obrigatório:
idade = int (input("Digite sua idade:"))
if idade <= 16:
      print("Não vota")
if idade >= 18 and idade <= 70:
    print ("Voto Obrigatório")
else:
      print ("Voto facultativo")

# 13. Número fora de intervalo:
numero = int (input("Digite um número inteiro:"))
if numero >= 10 and numero <= 50:
      print("Dentro do intervalo")
else: 
      print("Fora do intervalo")

# 14. Aluno Aprovado com Recuperação:
media_final = float (input("Digite a sua média:"))
if media_final >= 7:
      print("Aprovado")
elif media_final >= 5 and media_final < 7:
        print (f"Recuperação")
else: print ("Reprovado")



    
