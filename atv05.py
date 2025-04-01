n1=float(input("Digite uma nota: "))
n2=float(input("Digite uma segunnda nota: "))
n3=float(input("Digite uma terceira nota: "))
media=(n1 + n2 + n3)/3
if media >= 7:
    print(f"Aluno aprovado com media {media}")
else:
    print(f"Aluno reprovado com media {media}")


