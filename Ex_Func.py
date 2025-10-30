#1:
potencia = lambda x: x**2
potencia(4)
#2:
func2 = lambda x: 5*x - 3
func2 (2)
#3:
func3 = lambda x: x**2 + 2*x + 1
func3 (-1)
func3 (0)
func3 (1)
#4:
func4 = lambda x,y: x**2 + 2*x*y + y**2
func4(x=2, y=4)
#5:
func5 = lambda x,y,z: x**y + z
func5 (x=3,y=2,z=10)
#6:
def lucro(receita,custo):
    lucro = receita - custo 
    return lucro 
receita = 10000 
custo = 7500
lucro(receita, custo)
#7:
def margem_lucro (receita,custo):
    margem_lucro = (receita - custo /receita)* 100
    return margem_lucro
receita = 20000
custo = 15000
margem_lucro (receita,custo)
#8:
def qe (custo_fixo,preco,custo_variavel):
    qe = custo_fixo / (preco - custo_variavel)
    return qe 
custo_fixo = 5000
custo_variavel = 30
preco = 50
qe (custo_fixo,preco,custo_variavel)
#9:
def folha(funcionarios):
    folha_salarial = 0
    for funcionario in funcionarios:
        salario = funcionario['salario']
        folha_salarial += salario
    return folha_salarial
        
    
folha([{'nome': 'Ana', 'salario': 3000}, {'nome': 'Carlos', 'salario': 4500}])

