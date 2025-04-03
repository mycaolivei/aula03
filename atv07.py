tipo=input("Digite E para etanol e G para gasolina: ")
qtdlitros=float(input("Você vai querer quantos litros?: "))
vGas= 5.8
vEta= 4.9
if tipo =="G":
    valor = qtdlitros * vGas
else:
    valor = qtdlitros * vEta
    print (f"Voce gastou R$ {valor:.2f}")


