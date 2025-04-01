nome=input("Digite o seu nome: ")
idade=int(input("Dgite a  sua idade: "))
salario=float(input("Qual  é o valor do seu salario: "))
aumento=float(input("Quantos porcentos de aumento você  obteve no seu salario? "))
valoreal=salario*aumento / 100
novosalario = salario + valoreal
print(f"Olá {nome}, você tem {idade} anos e seu salario é {salario}, esse mês voce recebeu {valoreal} seu salario final é de {novosalario}")