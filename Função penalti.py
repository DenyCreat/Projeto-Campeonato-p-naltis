import random
print('--------------------RODADA 2--------------------')
print('partida 7')
print('--casa--: time 1')
print('--visitante--: time 8')
L1 = ['penalty 1 T1:', 'penalty 2 T1:', 'penalty 3 T1:', 'penalty 4 T1:', 'penalty 5 T1:', 'penalty 6 T1:', 'penalty 7 T1:', 'penalty 8 T1:', 'penalty 9 T1:', 'penalty 10 T1:', 'penalty 11 T1:', 'penalty 12 T1:', 'penalty 13 T1:', 'penalty 14 T1:', 'penalty 15 T1:']
L2 = ['penalty 1 T2:', 'penalty 2 T2:', 'penalty 3 T2:', 'penalty 4 T2:', 'penalty 5 T2:', 'penalty 6 T2:', 'penalty 7 T2:', 'penalty 8 T2:', 'penalty 9 T2:', 'penalty 10 T2:', 'penalty 11 T2:', 'penalty 12 T2:', 'penalty 13 T2:', 'penalty 14 T2:', 'penalty 15 T2:']
L3 = ['penalty 1 T3:', 'penalty 2 T3:', 'penalty 3 T3:', 'penalty 4 T3:', 'penalty 5 T3:', 'penalty 6 T3:', 'penalty 7 T3:', 'penalty 8 T3:', 'penalty 9 T3:', 'penalty 10 T3:', 'penalty 11 T3:', 'penalty 12 T3:', 'penalty 13 T3:', 'penalty 14 T3:', 'penalty 15 T3:']
L4 = ['penalty 1 T4:', 'penalty 2 T4:', 'penalty 3 T4:', 'penalty 4 T4:', 'penalty 5 T4:', 'penalty 6 T4:', 'penalty 7 T4:', 'penalty 8 T4:', 'penalty 9 T4:', 'penalty 10 T4:', 'penalty 11 T4:', 'penalty 12 T4:', 'penalty 13 T4:', 'penalty 14 T4:', 'penalty 15 T4:']
L5 = ['penalty 1 T5:', 'penalty 2 T5:', 'penalty 3 T5:', 'penalty 4 T5:', 'penalty 5 T5:', 'penalty 6 T5:', 'penalty 7 T5:', 'penalty 8 T5:', 'penalty 9 T5:', 'penalty 10 T5:', 'penalty 11 T5:', 'penalty 12 T5:', 'penalty 13 T5:', 'penalty 14 T5:', 'penalty 15 T5:']
L6 = ['penalty 1 T6:', 'penalty 2 T6:', 'penalty 3 T6:', 'penalty 4 T6:', 'penalty 5 T6:', 'penalty 6 T6:', 'penalty 7 T6:', 'penalty 8 T6:', 'penalty 9 T6:', 'penalty 10 T6:', 'penalty 11 T6:', 'penalty 12 T6:', 'penalty 13 T6:', 'penalty 14 T6:', 'penalty 15 T6:']
L7 = ['penalty 1 T7:', 'penalty 2 T7:', 'penalty 3 T7:', 'penalty 4 T7:', 'penalty 5 T7:', 'penalty 6 T7:', 'penalty 7 T7:', 'penalty 8 T7:', 'penalty 9 T7:', 'penalty 10 T7:', 'penalty 11 T7:', 'penalty 12 T7:', 'penalty 13 T7:', 'penalty 14 T7:', 'penalty 15 T7:']
L8 = ['penalty 1 T8:', 'penalty 2 T8:', 'penalty 3 T8:', 'penalty 4 T8:', 'penalty 5 T8:', 'penalty 6 T8:', 'penalty 7 T8:', 'penalty 8 T8:', 'penalty 9 T8:', 'penalty 10 T8:', 'penalty 11 T8:', 'penalty 12 T8:', 'penalty 13 T8:', 'penalty 14 T8:', 'penalty 15 T8:']
Q = ['o placar dos penaltis T1 é:', 'o placar dos penaltis T2 é:', 'o placar dos penaltis T3 é:', 'o placar dos penaltis T4 é:', 'o placar dos penaltis T5 é:', 'o placar dos penaltis T6 é:', 'o placar dos penaltis T7 é:', 'o placar dos penaltis T8 é:']
R = ['time 1 ganhou o jogo, +3pts', 'time 2 ganhou o jogo, +3pts', 'time 3 ganhou o jogo, +3pts', 'time 4 ganhou o jogo, +3pts', 'time 5 ganhou o jogo, +3pts', 'time 6 ganhou o jogo, +3pts', 'time 7 ganhou o jogo, +3pts', 'time 8 ganhou o jogo, +3pts']
S = ['----------pontuacão atual do time 1 é:', '----------pontuacão atual do time 2 é:', '----------pontuacão atual do time 3 é:', '----------pontuacão atual do time 4 é:', '----------pontuacão atual do time 5 é:', '----------pontuacão atual do time 6 é:', '----------pontuacão atual do time 7 é:', '----------pontuacão atual do time 8 é:']
pt1 = 0
pt2 = 0
pt3 = 0
pt4 = 0
pt5 = 0
pt6 = 0
pt7 = 0
pt8 = 0
sgT1 = 0
sgT2 = 0
sgT3 = 0
sgT4 = 0
sgT5 = 0
sgT6 = 0
sgT7 = 0
sgT8 = 0
P = [pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8]
SG = [sgT1, sgT2, sgT3, sgT4, sgT5, sgT6, sgT7, sgT8]
def decisão_pênaltis(a,b):
    lt = [a,b]
    lt[0] = random.choice(lt)
    lt[1] = random.choice(lt)
    return(lt[0], lt[1])
def rodada_princ_pênaltis(c,d,e,f,g,h,i,j,k,l):
    a = 'X'
    b = 'O'
    p1 = decisão_pênaltis(a,b)
    print(c[0],p1[0])
    print(d[0],p1[1])
    print('digite 0 para sair do jogo ou 1 para continuar')
    s = int(input('digite o valor:' ))
    if s == 0:
        print('fim do jogo')
        exit
    if s != 0 and s != 1:
        print('valor inválido')
        print('fim do jogo')
        exit
    elif s == 1:
        p2 = decisão_pênaltis(a,b)
        print(c[1],p2[0])
        print(d[1],p2[1])
    s = int(input('digite 1 para proxima rodada de penaltis:' ))
    if s != 1:
        print('fim do jogo')
        exit
    else:
        p3 = decisão_pênaltis(a,b)
        print(c[2], p3[0])
        print(d[2], p3[1])
    s = int(input('digite 1 para proxima rodada de penaltis:' ))
    if s != 1:
        print('fim do jogo')
        exit
    else:
        p4 = decisão_pênaltis(a,b)
        print(c[3], p4[0])
        print(d[3], p4[1])
    s = int(input('digite 1 para proxima rodada de penaltis:' ))
    if s != 1:
        print('fim do jogo')
        exit
    else:
        p5 = decisão_pênaltis(a,b)
        print(c[4], p5[0])
        print(d[4], p5[1])
        listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0]]
        listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1]]
        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
        print(listaPT1)
        print(listaPT2)
        print(e, len(PpT1))
        print(f, len(PpT2))
    if len(PpT1) > len(PpT2):
        g
        i += 3
        j += 0
        k += len(PpT1)
        Lmes = [g, i, j]
        return(Lmes)
    elif len(PpT1) < len(PpT2):
        h
        j += 3
        i += 0
        l += len(PpT2)
        Lmes = [h, j, i]
        return(Lmes)
    elif len(PpT1) == len(PpT2):
        print('agora é disputa nas alternadas, até alguem errar')
        p6 = decisão_pênaltis(a,b)
        print(c[5], p6[0])
        print(c[5], p6[1])
        listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]]
        listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1]]
        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
        print(listaPT1)
        print(listaPT2)
        print(e, len(PpT1))
        print(f, len(PpT2))
        if len(PpT1) > len(PpT2):
            g
            i += 3
            j += 0
            k += len(PpT1)
            Lmes = [g, i, j]
            return(Lmes)
        elif len(PpT1) < len(PpT2):
            h
            j += 3
            i += 0
            l += len(PpT2)
            Lmes = [h, j, i]
            return(Lmes)
        elif len(PpT1) == len(PpT2):
            p7 = decisão_pênaltis(a,b)
            print(c[6], p7[0])
            print(c[6], p7[1])
            listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0]]
            listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1]]
            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
            print(listaPT1)
            print(listaPT2)
            print(e, len(PpT1))
            print(f, len(PpT2))
            if len(PpT1) > len(PpT2):
                g
                i += 3
                j += 0
                k += len(PpT1)
                Lmes = [g, i, j]
                return(Lmes)
            elif len(PpT1) < len(PpT2):
                h
                j += 3
                i += 0
                l += len(PpT2)
                Lmes = [h, j, i]
                return(Lmes)
            elif len(PpT1) == len(PpT2):
                p8 = decisão_pênaltis(a,b)
                print(c[7], p8[0])
                print(c[7], p8[1])
                listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0]]
                listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1]]
                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                print(listaPT1)
                print(listaPT2)
                print(e, len(PpT1))
                print(f, len(PpT2))
                if len(PpT1) > len(PpT2):
                    g
                    i += 3
                    j += 0
                    k += len(PpT1)
                    Lmes = [g, i, j]
                    return(Lmes)
                elif len(PpT1) < len(PpT2):
                    h
                    j += 3
                    i += 0
                    l += len(PpT2)
                    Lmes = [h, j, i]
                    return(Lmes)
                elif len(PpT1) == len(PpT2):
                    p9 = decisão_pênaltis(a,b)
                    print(c[8], p9[0])
                    print(c[8], p9[1])
                    listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0]]
                    listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1]]
                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                    print(listaPT1)
                    print(listaPT2)
                    print(e, len(PpT1))
                    print(f, len(PpT2))
                    if len(PpT1) > len(PpT2):
                        g
                        i += 3
                        j += 0
                        k += len(PpT1)
                        Lmes = [g, i, j]
                        return(Lmes)
                    elif len(PpT1) < len(PpT2):
                        h
                        j += 3
                        i += 0
                        l += len(PpT2)
                        Lmes = [h, j, i]
                        return(Lmes)
                    elif len(PpT1) == len(PpT2):
                        p10 = decisão_pênaltis(a,b)
                        print(c[9], p10[0])
                        print(c[9], p10[1])
                        listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0]]
                        listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1], p10[1]]
                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                        print(listaPT1)
                        print(listaPT2)
                        print(e, len(PpT1))
                        print(f, len(PpT2))
                        if len(PpT1) > len(PpT2):
                            g
                            i += 3
                            j += 0
                            k += len(PpT1)
                            Lmes = [g, i, j]
                            return(Lmes)
                        elif len(PpT1) < len(PpT2):
                            h
                            j += 3
                            i += 0
                            l += len(PpT2)
                            Lmes = [h, j, i]
                            return(Lmes)
                        elif len(PpT1) == len(PpT2):
                            p11 = decisão_pênaltis(a,b)
                            print(c[10], p11[0])
                            print(c[10], p11[1])
                            listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0], p11[0]]
                            listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1], p10[1], p11[1]]
                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                            print(listaPT1)
                            print(listaPT2)
                            print(e, len(PpT1))
                            print(f, len(PpT2))
                            if len(PpT1) > len(PpT2):
                                g
                                i += 3
                                j += 0
                                k += len(PpT1)
                                Lmes = [g, i, j]
                                return(Lmes)
                            elif len(PpT1) < len(PpT2):
                                h
                                j += 3
                                i += 0
                                l += len(PpT2)
                                Lmes = [h, j, i]
                                return(Lmes)
                            elif len(PpT1) == len(PpT2):
                                p12 = decisão_pênaltis(a,b)
                                print(c[11], p12[0])
                                print(c[11], p12[1])
                                listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0], p11[0], p12[0]]
                                listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1], p10[1], p11[1], p12[1]]
                                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                print(listaPT1)
                                print(listaPT2)
                                print(e, len(PpT1))
                                print(f, len(PpT2))
                                if len(PpT1) > len(PpT2):
                                    g
                                    i += 3
                                    j += 0
                                    k += len(PpT1)
                                    Lmes = [g, i, j]
                                    return(Lmes)
                                elif len(PpT1) < len(PpT2):
                                    h
                                    j += 3
                                    i += 0
                                    l += len(PpT2)
                                    Lmes = [h, j, i]
                                    return(Lmes)
                                elif len(PpT1) == len(PpT2):
                                    p13 = decisão_pênaltis(a,b)
                                    print(c[12], p13[0])
                                    print(c[12], p13[1])
                                    listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0], p11[0], p12[0], p13[0]]
                                    listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1], p10[1], p11[1], p12[1], p13[1]]
                                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                    print(listaPT1)
                                    print(listaPT2)
                                    print(e, len(PpT1))
                                    print(f, len(PpT2))
                                    if len(PpT1) > len(PpT2):
                                        g
                                        i += 3
                                        j += 0
                                        k += len(PpT1)
                                        Lmes = [g, i, j]
                                        return(Lmes)
                                    elif len(PpT1) < len(PpT2):
                                        h
                                        j += 3
                                        i += 0
                                        l += len(PpT2)
                                        Lmes = [h, j, i]
                                        return(Lmes)
                                    elif len(PpT1) == len(PpT2):
                                        p14 = decisão_pênaltis(a,b)
                                        print(c[13], p14[0])
                                        print(c[13], p14[1])
                                        listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0], p11[0], p12[0], p13[0], p14[0]]
                                        listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1], p10[1], p11[1], p12[1], p13[1], p14[1]]
                                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                        print(listaPT1)
                                        print(listaPT2)
                                        print(e, len(PpT1))
                                        print(f, len(PpT2))
                                        if len(PpT1) > len(PpT2):
                                            g
                                            i += 3
                                            j += 0
                                            k += len(PpT1)
                                            Lmes = [g, i, j]
                                            return(Lmes)
                                        elif len(PpT1) < len(PpT2):
                                            h
                                            j += 3
                                            i += 0
                                            l += len(PpT2)
                                            Lmes = [h, j, i]
                                            return(Lmes)
                                        elif len(PpT1) == len(PpT2):
                                            p15 = decisão_pênaltis(a,b)
                                            print(c[14], p15[0])
                                            print(c[14], p15[1])
                                            listaPT1 = [p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0], p8[0], p9[0], p10[0], p11[0], p12[0], p13[0], p14[0], p15[0]]
                                            listaPT2 = [p1[1], p2[1], p3[1], p4[1], p5[1], p6[1], p7[1], p8[1], p9[1], p10[1], p11[1], p12[1], p13[1], p14[1], p15[1]]
                                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                            print(listaPT1)
                                            print(listaPT2)
                                            print(e, len(PpT1))
                                            print(f, len(PpT2))
                                            if len(PpT1) > len(PpT2):
                                                g
                                                i += 3
                                                j += 0
                                                k += len(PpT1)
                                                Lmes = [g, i, j]
                                                return(Lmes)
                                            elif len(PpT1) < len(PpT2):
                                                h
                                                j += 3
                                                i += 0
                                                l += len(PpT2)
                                                Lmes = [h, j, i]
                                                return(Lmes)
                                            
                                        
   

c = L1
d = L2
e = Q[0]
f = Q[1]
g = R[0]
h = R[1]
i = P[0]
j = P[1]
k = SG[0]
l = SG[1]
resultado = rodada_princ_pênaltis(c,d,e,f,g,h,i,j,k,l)
print(resultado[0])
print(S[0], resultado[2])
print(S[1], resultado[1])

c = L1
d = L3
e = Q[0]
f = Q[2]
g = R[0]
h = R[2]
i = P[0]
j = P[2]
k = SG[0]
l = SG[2]
resultado = rodada_princ_pênaltis(c,d,e,f,g,h,i,j,k,l)
print(resultado[0])
print(S[0], resultado[2])
print(S[2], resultado[1])

c = L1
d = L4
e = Q[0]
f = Q[3]
g = R[0]
h = R[3]
i = P[0]
j = P[3]
k = SG[0]
l = SG[3]
resultado = rodada_princ_pênaltis(c,d,e,f,g,h,i,j,k,l)
print(resultado[0])
print(S[0], resultado[2])
print(S[3], resultado[1])

c = L1
d = L5
e = Q[0]
f = Q[4]
g = R[0]
h = R[4]
i = P[0]
j = P[4]
k = SG[0]
l = SG[4]
resultado = rodada_princ_pênaltis(c,d,e,f,g,h,i,j,k,l)
print(resultado[0])
print(S[0], resultado[2])
print(S[4], resultado[1])

c = L1
d = L6
e = Q[0]
f = Q[5]
g = R[0]
h = R[5]
i = P[0]
j = P[5]
k = SG[0]
l = SG[5]
resultado = rodada_princ_pênaltis(c,d,e,f,g,h,i,j,k,l)
print(resultado[0])
print(S[0], resultado[2])
print(S[5], resultado[1])

c = L1
d = L7
e = Q[0]
f = Q[6]
g = R[0]
h = R[6]
i = P[0]
j = P[6]
k = SG[0]
l = SG[6]
resultado = rodada_princ_pênaltis(c,d,e,f,g,h,i,j,k,l)
print(resultado[0])
print(S[0], resultado[2])
print(S[6], resultado[1])

c = L1
d = L8
e = Q[0]
f = Q[7]
g = R[0]
h = R[7]
i = P[0]
j = P[7]
k = SG[0]
l = SG[7]
resultado = rodada_princ_pênaltis(c,d,e,f,g,h,i,j,k,l)
print(resultado[0])
print(S[0], resultado[2])
print(S[7], resultado[1])












