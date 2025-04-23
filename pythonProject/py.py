print("Cadastro do Aluno:")
truepass = "Kaka143"
trueRM = "564211"
nome = input("Nome:\n")
rm = input("RM do Aluno:\n")
senha = input("Senha:\n")
contTent = 2
while senha != truepass or rm != trueRM:
    rm = input("Digite seu RM novamente:\n")
    senha = input("Digite sua senha novamente:\n")
    continue
print("Entrada Permitida no Boletim:")
if senha == truepass and rm == trueRM:
    print("Boletim do Aluno")
    senha = input("Redigite sua senha:\n")
    if senha != truepass:
        for tent in range(1, 3):
            print(f"Você tem {contTent} chances!")
            senha = input("Redigite novamente:\n")
            contTent -= 1
            if tent == 3:
                print("Conta Bloqueada! Tente novamente mais tarde")
                break
    else:
        cp1 = float(input("Digite a sua primeira nota:\n"))
        cp2 = float(input("Digite a sua segunda nota:\n"))
        cp3 = float(input("Digite a sua terceira nota:\n"))
        while 0 > cp1 > 10 and 0 > cp2 > 10 and 0 > cp3 > 10:
            cp1 = float(input("Digite novamente a sua primeira nota:\n"))
            cp2 = float(input("Digite novamente a sua segunda nota:\n"))
            cp3 = float(input("Digite novamente a sua terceira nota:\n"))
        if cp1 < cp2 and cp1 < cp3:
            media1 = (cp2 + cp3)/2
        elif cp2 < cp1 and cp2 < cp3:
            media1 = (cp3 + cp1)/2
        else:
            media1 = (cp2 + cp1)/2
        sprint1 = float(input("Digite a nota do primeiro sprint:\n"))
        sprint2 = float(input("Digite a nota do segundo sprint:\n"))
        media2 = (sprint1+sprint2)/2
        mediatotal = (((media1 + media2)/2)*40)/100
        notaGs = 6 - mediatotal
        totalGs = (notaGs * 100) / 60
        print(f"Você precisa de: {totalGs:.2f} na global solution")

