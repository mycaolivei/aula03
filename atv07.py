tipo=input("Digite E para etanol e G para gasolina: ")
qtdlitros=float(input("Você vai querer quantos litros?: "))
vGas= 5.8
vEta= 4.9
if tipo == "G" or tipo == "g":
    valor = qtdlitros * vGas
elif tipo == "E" or tipo == "e":
    valor = qtdlitros * vEta
else:
    print("Tipo de combustivel invalido!")
print(f"Voce gastou R$ {valor:.2f}")


