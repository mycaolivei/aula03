time1=input("Digite o time de futebol: ")
time2=input("Digite outro time de futebol: ")
gol1=int(input(f"Digite o número de gols do {time1}"))
gol2=int(input(f"Digite o número de gols do {time2}"))
if gol1 == gol2:
    print("bola na trava não altera o placar!")
else:
    if gol1>gol2:
     print(f"O {time1} ganhou")
    else:
        print(f"O {time2} ganhou")

