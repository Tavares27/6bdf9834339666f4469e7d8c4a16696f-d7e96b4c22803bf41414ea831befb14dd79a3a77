soma = 0
BN1 = []
H = [0]*3
O = [0]*4
BN2 = []
SB = [0]*12
try :
    N1 = int(input("Digite o primeiro número: "))
    N2 = int(input("Digite o segundo número: "))
    B = int(input("Digite a base desejada: "))
    if (N1 > 512 or N2 > 512) or (B!= 2 and B!= 8 and B!= 10 and B!=16):
        print("ERRO")
    else:
        a1 = N1
        a2 = N2
        while a1 >= 1:
            BN1.append(a1 % 2)
            a1 = a1//2
        while a2 >= 1:
            BN2.append(a2 % 2)
            a2 = a2//2
        while len(BN1) < 11:
            BN1.append(0)
        while len(BN2) < 11:
            BN2.append(0)
        for i in range(len(BN1)):
            if (BN1[i]+BN2[i])%2 == 0:
                SB[i] += 0
                if BN1[i]+BN2[i] > 0 :
                    SB[i+1] += 1
            if (BN1[i]+BN2[i])%2 == 1:
                SB[i] += 1
                if BN1[i]+BN2[i] > 1 :
                    SB[i+1] += 1
            if SB[i] == 2 :
                SB[i] = 0
                SB[i+1]= 1
            elif SB[i] == 3:
                SB[i] = 1
                SB[i+1] = 1
        if B == 2:
            SB.pop(0)
            SB.reverse()
            soma = ''.join([str(x)for x in SB])
            print("A soma dos números é :", soma)
        elif B == 10:
            for i in range(0, 11):
                soma = soma + (SB[i] * 2**i)
            print("A soma dos números é :", soma)
        elif B == 8 :
            for i in range(4):
                O[i] = (SB[i*3]*2**0)+(SB[(i*3)+1]*2**(1))+(SB[(i*3)+2]*2**(2))
            O.reverse()
            soma = ''.join([str(x) for x in O])
            print("A soma dos números é :", soma)
        elif B == 16 :
            for i in range(3):
                H[i] = (SB[i*4]*2**0)+(SB[(i*4)+1]*2**(1))+(SB[(i*4)+2]*2**(2)+(SB[(i*4)+3]*2**(3)))
                if H[i] == 10:
                    H[i] = "A"
                elif H[i] == 11:
                    H[i] = "B"
                elif H[i] == 12 :
                    H[i] = "C"
                elif H[i] == 13:
                    H[i] = "D"
                elif H[i] == 14:
                    H[i] = "E"
                elif H[i] == 15:
                    H[i] = "F"
            H.reverse()
            soma = ''.join([str(x) for x in H])
            print("A soma dos números é :", soma)
except ValueError:
    print("ERRO")