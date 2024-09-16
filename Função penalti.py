import random
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

def rodada_princ_pênaltis(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    lista = [a,b]
    p1t1 = random.choice(lista)
    p1t2 = random.choice(lista)
    print(c[0], p1t1)
    print(d[0], p1t2)
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
        p2t1 = random.choice(lista)
        p2t2 = random.choice(lista)
        print(c[1], p2t1)
        print(d[1], p2t2)
        s = int(input('digite 1 para proxima rodada de penaltis:' ))
    if s != 1:
        print('fim do jogo')
        exit
    else:
        p3t1 = random.choice(lista)
        p3t2 = random.choice(lista)
        print(c[2], p3t1)
        print(d[2], p3t2)
        s = int(input('digite 1 para proxima rodada de penaltis:' ))
    if s != 1:
        print('fim do jogo')
        exit
    else:
        p4t1 = random.choice(lista)
        p4t2 = random.choice(lista)
        print(c[3], p4t1)
        print(d[3], p4t2)
        s = int(input('digite 1 para proxima rodada de penaltis:' ))
    if s != 1:
        print('fim do jogo')
        exit
    else:
        p5t1 = random.choice(lista)
        p5t2 = random.choice(lista)
        print(c[4], p5t1)
        print(d[4], p5t2)
    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1]
    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2]
    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
    print(listaPT1)
    print(listaPT2)
    print(e, len(PpT1))
    print(f, len(PpT2))
    if len(PpT1) > len(PpT2):
        print(g)
        k += 3
        l += 0
        m += len(PpT1)
        n += len(PpT2)
        R1 = (i, k)
        R2 = (j, l)
        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
        return(Res)
        return(v)
    elif len(PpT1) < len(PpT2):
        print(h)
        k += 0
        l += 3
        m += len(PpT1)
        n += len(PpT2)
        R1 = (i, k)
        R2 = (j, l)
        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
        return(Res)
    elif len(PpT1) == len(PpT2):
        print('agora é disputa nas alternadas, até alguem errar')
        p6t1 = random.choice(lista)
        p6t2 = random.choice(lista)
        print(c[5], p6t1)
        print(d[5], p6t2)
        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1]
        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2]
        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
        print(listaPT1)
        print(listaPT2)
        print(e, len(PpT1))
        print(f, len(PpT2))
        if len(PpT1) > len(PpT2):
            print(g)
            k += 3
            l += 0
            m += len(PpT1)
            n += len(PpT2)
            R1 = (i, k)
            R2 = (j, l)
            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
            return(Res)
        elif len(PpT1) < len(PpT2):
            print(h)
            k += 0
            l += 3
            m += len(PpT1)
            n += len(PpT2)
            R1 = (i, k)
            R2 = (j, l)
            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
            return(Res)
        elif len(PpT1) == len(PpT2):
            p7t1 = random.choice(lista)
            p7t2 = random.choice(lista)
            print(c[6], p7t1)
            print(d[6], p7t2)
            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1]
            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2]
            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
            print(listaPT1)
            print(listaPT2)
            print(e, len(PpT1))
            print(f, len(PpT2))
            if len(PpT1) > len(PpT2):
                print(g)
                k += 3
                l += 0
                m += len(PpT1)
                n += len(PpT2)
                R1 = (i, k)
                R2 = (j, l)
                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                return(Res)
            elif len(PpT1) < len(PpT2):
                print(h)
                k += 0
                l += 3
                m += len(PpT1)
                n += len(PpT2)
                R1 = (i, k)
                R2 = (j, l)
                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                return(Res)
            elif len(PpT1) == len(PpT2):
                p8t1 = random.choice(lista)
                p8t2 = random.choice(lista)
                print(c[7], p8t1)
                print(d[7], p8t2)
                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1]
                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2]
                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                print(listaPT1)
                print(listaPT2)
                print(e, len(PpT1))
                print(f, len(PpT2))
                if len(PpT1) > len(PpT2):
                    print(g)
                    k += 3
                    l += 0
                    m += len(PpT1)
                    n += len(PpT2)
                    R1 = (i, k)
                    R2 = (j, l)
                    Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                    return(Res)
                elif len(PpT1) < len(PpT2):
                    print(h)
                    k += 0
                    l += 3
                    m += len(PpT1)
                    n += len(PpT2)
                    R1 = (i, k)
                    R2 = (j, k)
                    Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                    return(Res)
                elif len(PpT1) == len(PpT2):
                    p9t1 = random.choice(lista)
                    p9t2 = random.choice(lista)
                    print(c[8], p9t1)
                    print(d[8], p9t2)
                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1]
                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2]
                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                    print(listaPT1)
                    print(listaPT2)
                    print(e, len(PpT1))
                    print(f, len(PpT2))
                    if len(PpT1) > len(PpT2):
                        print(g)
                        k += 3
                        l += 0
                        m += len(PpT1)
                        n += len(PpT2)
                        R1 = (i, k)
                        R2 = (j, l)
                        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                        return(Res)
                    elif len(PpT1) < len(PpT2):
                        print(h)
                        k += 0
                        l += 3
                        m += len(PpT1)
                        n += len(PpT2)
                        R1 = (i, k)
                        R2 = (j, l)
                        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                        return(Res)
                    elif len(PpT1) == len(PpT2):
                        p10t1 = random.choice(lista)
                        p10t2 = random.choice(lista)
                        print(c[9], p10t1)
                        print(d[9], p10t2)
                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1]
                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2]
                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                        print(listaPT1)
                        print(listaPT2)
                        print(e, len(PpT1))
                        print(f, len(PpT2))
                        if len(PpT1) > len(PpT2):
                            print(g)
                            k += 3
                            l += 0
                            m += len(PpT1)
                            n += len(PpT2)
                            R1 = (i, k)
                            R2 = (j, l)
                            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                            return(Res)
                        elif len(PpT1) < len(PpT2):
                            print(h)
                            k += 0
                            l += 3
                            m += len(PpT1)
                            n += len(PpT2)
                            R1 = (i, k)
                            R2 = (j, l)
                            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                            return(Res)
                        elif len(PpT1) == len(PpT2):
                            p11t1 = random.choice(lista)
                            p11t2 = random.choice(lista)
                            print(c[10], p11t1)
                            print(d[10], p11t2)
                            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1]
                            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2]
                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                            print(listaPT1)
                            print(listaPT2)
                            print(e, len(PpT1))
                            print(f, len(PpT2))
                            if len(PpT1) > len(PpT2):
                                print(g)
                                k += 3
                                l += 0
                                m += len(PpT1)
                                n += len(PpT2)
                                R1 = (i, k)
                                R2 = (j, l)
                                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                return(Res)
                            elif len(PpT1) < len(PpT2):
                                print(h)
                                k += 3
                                l += 0
                                m += len(PpT1)
                                n += len(PpT2)
                                R1 = (i, k)
                                R2 = (j, l)
                                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                return(Res)
                            elif len(PpT1) == len(PpT2):
                                p12t1 = random.choice(lista)
                                p12t2 = random.choice(lista)
                                print(c[11], p12t1)
                                print(d[11], p12t2)
                                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1]
                                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2]
                                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                print(listaPT1)
                                print(listaPT2)
                                print(e, len(PpT1))
                                print(f, len(PpT2))
                                if len(PpT1) > len(PpT2):
                                    print(g)
                                    k += 3
                                    l += 0
                                    m += len(PpT1)
                                    n += len(PpT2)
                                    R1 = (i, k)
                                    R2 = (j, l)
                                    Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                    return(Res)
                                elif len(PpT1) < len(PpT2):
                                    print(h)
                                    k += 0
                                    l += 3
                                    m += len(PpT1)
                                    n += len(PpT2)
                                    R1 = (i, k)
                                    R2 = (j, l)
                                    Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                    return(Res)
                                elif len(PpT1) == len(PpT2):
                                    p13t1 = random.choice(lista)
                                    p13t2 = random.choice(lista)
                                    print(c[12], p13t1)
                                    print(d[12], p13t2)
                                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1]
                                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2]
                                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                    print(listaPT1)
                                    print(listaPT2)
                                    print(e, len(PpT1))
                                    print(f, len(PpT2))
                                    if len(PpT1) > len(PpT2):
                                        print(g)
                                        k += 3
                                        l += 0
                                        m += len(PpT1)
                                        n += len(PpT2)
                                        R1 = (i, k)
                                        R2 = (j, l)
                                        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                        return(Res)
                                    elif len(PpT1) < len(PpT2):
                                        print(h)
                                        k += 0
                                        l += 3
                                        m += len(PpT1)
                                        n += len(PpT2)
                                        R1 = (i, k)
                                        R2 = (j, l)
                                        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                        return(Res)
                                    elif len(PpT1) == len(PpT2):
                                        p14t1 = random.choice(lista)
                                        p14t2 = random.choice(lista)
                                        print(c[13], p14t1)
                                        print(d[13], p14t2)
                                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1]
                                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2]
                                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                        print(listaPT1)
                                        print(listaPT2)
                                        print(e, len(PpT1))
                                        print(f, len(PpT2))
                                        if len(PpT1) > len(PpT2):
                                            print(g)
                                            k += 3
                                            l += 0
                                            m += len(PpT1)
                                            n += len(PpT2)
                                            R1 = (i, k)
                                            R2 = (j, l)
                                            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                            return(Res)
                                        elif len(PpT1) < len(PpT2):
                                            print(h)
                                            k += 0
                                            l += 3
                                            m += len(PpT1)
                                            n += len(PpT2)
                                            R1 = (i, k)
                                            R2 = (j, l)
                                            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                            return(Res)
                                        elif len(PpT1) == len(PpT2):
                                            p15t1 = random.choice(lista)
                                            p15t2 = random.choice(lista)
                                            print(c[14], p15t1)
                                            print(d[14], p15t2)
                                            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1, p15t1]
                                            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2, p15t2]
                                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                            print(listaPT1)
                                            print(listaPT2)
                                            print(e, len(PpT1))
                                            print(f, len(PpT2))
                                            if len(PpT1) > len(PpT2):
                                                print(g)
                                                k += 3
                                                l += 0
                                                m += len(PpT1)
                                                n += len(PpT2)
                                                R1 = (i, k)
                                                R2 = (j, l)
                                                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                                return(Res)
                                            elif len(PpT1) < len(PpT2):
                                                print(h)
                                                k += 0
                                                l += 3
                                                m += len(PpT1)
                                                n += len(PpT2)
                                                R1 = (i, k)
                                                R2 = (j, l)
                                                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                                return(Res)

def rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
    lista = [a,b]
    p1t1 = random.choice(lista)
    p1t2 = random.choice(lista)
    p2t1 = random.choice(lista)
    p2t2 = random.choice(lista)
    p3t1 = random.choice(lista)
    p3t2 = random.choice(lista)
    p4t1 = random.choice(lista)
    p4t2 = random.choice(lista)
    p5t1 = random.choice(lista)
    p5t2 = random.choice(lista)
    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1]
    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2]
    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
    print(listaPT1)
    print(listaPT2)
    print(e, len(PpT1))
    print(f, len(PpT2))
    if len(PpT1) > len(PpT2):
        print(g)
        k += 3
        l += 0
        m += len(PpT1)
        n += len(PpT2)
        R1 = (i, k)
        R2 = (j, l)
        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
        return(Res)
        return(v)
    elif len(PpT1) < len(PpT2):
        print(h)
        k += 0
        l += 3
        m += len(PpT1)
        n += len(PpT2)
        R1 = (i, k)
        R2 = (j, l)
        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
        return(Res)
    elif len(PpT1) == len(PpT2):
        print('agora é disputa nas alternadas, até alguem errar')
        p6t1 = random.choice(lista)
        p6t2 = random.choice(lista)
        print(c[5], p6t1)
        print(d[5], p6t2)
        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1]
        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2]
        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
        print(listaPT1)
        print(listaPT2)
        print(e, len(PpT1))
        print(f, len(PpT2))
        if len(PpT1) > len(PpT2):
            print(g)
            k += 3
            l += 0
            m += len(PpT1)
            n += len(PpT2)
            R1 = (i, k)
            R2 = (j, l)
            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
            return(Res)
        elif len(PpT1) < len(PpT2):
            print(h)
            k += 0
            l += 3
            m += len(PpT1)
            n += len(PpT2)
            R1 = (i, k)
            R2 = (j, l)
            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
            return(Res)
        elif len(PpT1) == len(PpT2):
            p7t1 = random.choice(lista)
            p7t2 = random.choice(lista)
            print(c[6], p7t1)
            print(d[6], p7t2)
            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1]
            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2]
            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
            print(listaPT1)
            print(listaPT2)
            print(e, len(PpT1))
            print(f, len(PpT2))
            if len(PpT1) > len(PpT2):
                print(g)
                k += 3
                l += 0
                m += len(PpT1)
                n += len(PpT2)
                R1 = (i, k)
                R2 = (j, l)
                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                return(Res)
            elif len(PpT1) < len(PpT2):
                print(h)
                k += 0
                l += 3
                m += len(PpT1)
                n += len(PpT2)
                R1 = (i, k)
                R2 = (j, l)
                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                return(Res)
            elif len(PpT1) == len(PpT2):
                p8t1 = random.choice(lista)
                p8t2 = random.choice(lista)
                print(c[7], p8t1)
                print(d[7], p8t2)
                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1]
                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2]
                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                print(listaPT1)
                print(listaPT2)
                print(e, len(PpT1))
                print(f, len(PpT2))
                if len(PpT1) > len(PpT2):
                    print(g)
                    k += 3
                    l += 0
                    m += len(PpT1)
                    n += len(PpT2)
                    R1 = (i, k)
                    R2 = (j, l)
                    Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                    return(Res)
                elif len(PpT1) < len(PpT2):
                    print(h)
                    k += 0
                    l += 3
                    m += len(PpT1)
                    n += len(PpT2)
                    R1 = (i, k)
                    R2 = (j, k)
                    Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                    return(Res)
                elif len(PpT1) == len(PpT2):
                    p9t1 = random.choice(lista)
                    p9t2 = random.choice(lista)
                    print(c[8], p9t1)
                    print(d[8], p9t2)
                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1]
                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2]
                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                    print(listaPT1)
                    print(listaPT2)
                    print(e, len(PpT1))
                    print(f, len(PpT2))
                    if len(PpT1) > len(PpT2):
                        print(g)
                        k += 3
                        l += 0
                        m += len(PpT1)
                        n += len(PpT2)
                        R1 = (i, k)
                        R2 = (j, l)
                        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                        return(Res)
                    elif len(PpT1) < len(PpT2):
                        print(h)
                        k += 0
                        l += 3
                        m += len(PpT1)
                        n += len(PpT2)
                        R1 = (i, k)
                        R2 = (j, l)
                        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                        return(Res)
                    elif len(PpT1) == len(PpT2):
                        p10t1 = random.choice(lista)
                        p10t2 = random.choice(lista)
                        print(c[9], p10t1)
                        print(d[9], p10t2)
                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1]
                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2]
                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                        print(listaPT1)
                        print(listaPT2)
                        print(e, len(PpT1))
                        print(f, len(PpT2))
                        if len(PpT1) > len(PpT2):
                            print(g)
                            k += 3
                            l += 0
                            m += len(PpT1)
                            n += len(PpT2)
                            R1 = (i, k)
                            R2 = (j, l)
                            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                            return(Res)
                        elif len(PpT1) < len(PpT2):
                            print(h)
                            k += 0
                            l += 3
                            m += len(PpT1)
                            n += len(PpT2)
                            R1 = (i, k)
                            R2 = (j, l)
                            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                            return(Res)
                        elif len(PpT1) == len(PpT2):
                            p11t1 = random.choice(lista)
                            p11t2 = random.choice(lista)
                            print(c[10], p11t1)
                            print(d[10], p11t2)
                            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1]
                            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2]
                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                            print(listaPT1)
                            print(listaPT2)
                            print(e, len(PpT1))
                            print(f, len(PpT2))
                            if len(PpT1) > len(PpT2):
                                print(g)
                                k += 3
                                l += 0
                                m += len(PpT1)
                                n += len(PpT2)
                                R1 = (i, k)
                                R2 = (j, l)
                                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                return(Res)
                            elif len(PpT1) < len(PpT2):
                                print(h)
                                k += 3
                                l += 0
                                m += len(PpT1)
                                n += len(PpT2)
                                R1 = (i, k)
                                R2 = (j, l)
                                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                return(Res)
                            elif len(PpT1) == len(PpT2):
                                p12t1 = random.choice(lista)
                                p12t2 = random.choice(lista)
                                print(c[11], p12t1)
                                print(d[11], p12t2)
                                listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1]
                                listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2]
                                PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                print(listaPT1)
                                print(listaPT2)
                                print(e, len(PpT1))
                                print(f, len(PpT2))
                                if len(PpT1) > len(PpT2):
                                    print(g)
                                    k += 3
                                    l += 0
                                    m += len(PpT1)
                                    n += len(PpT2)
                                    R1 = (i, k)
                                    R2 = (j, l)
                                    Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                    return(Res)
                                elif len(PpT1) < len(PpT2):
                                    print(h)
                                    k += 0
                                    l += 3
                                    m += len(PpT1)
                                    n += len(PpT2)
                                    R1 = (i, k)
                                    R2 = (j, l)
                                    Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                    return(Res)
                                elif len(PpT1) == len(PpT2):
                                    p13t1 = random.choice(lista)
                                    p13t2 = random.choice(lista)
                                    print(c[12], p13t1)
                                    print(d[12], p13t2)
                                    listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1]
                                    listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2]
                                    PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                    PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                    print(listaPT1)
                                    print(listaPT2)
                                    print(e, len(PpT1))
                                    print(f, len(PpT2))
                                    if len(PpT1) > len(PpT2):
                                        print(g)
                                        k += 3
                                        l += 0
                                        m += len(PpT1)
                                        n += len(PpT2)
                                        R1 = (i, k)
                                        R2 = (j, l)
                                        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                        return(Res)
                                    elif len(PpT1) < len(PpT2):
                                        print(h)
                                        k += 0
                                        l += 3
                                        m += len(PpT1)
                                        n += len(PpT2)
                                        R1 = (i, k)
                                        R2 = (j, l)
                                        Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                        return(Res)
                                    elif len(PpT1) == len(PpT2):
                                        p14t1 = random.choice(lista)
                                        p14t2 = random.choice(lista)
                                        print(c[13], p14t1)
                                        print(d[13], p14t2)
                                        listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1]
                                        listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2]
                                        PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                        PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                        print(listaPT1)
                                        print(listaPT2)
                                        print(e, len(PpT1))
                                        print(f, len(PpT2))
                                        if len(PpT1) > len(PpT2):
                                            print(g)
                                            k += 3
                                            l += 0
                                            m += len(PpT1)
                                            n += len(PpT2)
                                            R1 = (i, k)
                                            R2 = (j, l)
                                            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                            return(Res)
                                        elif len(PpT1) < len(PpT2):
                                            print(h)
                                            k += 0
                                            l += 3
                                            m += len(PpT1)
                                            n += len(PpT2)
                                            R1 = (i, k)
                                            R2 = (j, l)
                                            Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                            return(Res)
                                        elif len(PpT1) == len(PpT2):
                                            p15t1 = random.choice(lista)
                                            p15t2 = random.choice(lista)
                                            print(c[14], p15t1)
                                            print(d[14], p15t2)
                                            listaPT1 = [p1t1, p2t1, p3t1, p4t1, p5t1, p6t1, p7t1, p8t1, p9t1, p10t1, p11t1, p12t1, p13t1, p14t1, p15t1]
                                            listaPT2 = [p1t2, p2t2, p3t2, p4t2, p5t2, p6t2, p7t2, p8t2, p9t2, p10t2, p11t2, p12t2, p13t2, p14t2, p15t2]
                                            PpT1 = [listaPT1 for listaPT1 in listaPT1 if listaPT1 != 'X']
                                            PpT2 = [listaPT2 for listaPT2 in listaPT2 if listaPT2 != 'X']
                                            print(listaPT1)
                                            print(listaPT2)
                                            print(e, len(PpT1))
                                            print(f, len(PpT2))
                                            if len(PpT1) > len(PpT2):
                                                print(g)
                                                k += 3
                                                l += 0
                                                m += len(PpT1)
                                                n += len(PpT2)
                                                R1 = (i, k)
                                                R2 = (j, l)
                                                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                                return(Res)
                                            elif len(PpT1) < len(PpT2):
                                                print(h)
                                                k += 0
                                                l += 3
                                                m += len(PpT1)
                                                n += len(PpT2)
                                                R1 = (i, k)
                                                R2 = (j, l)
                                                Res = [R1[0], R1[1], R2[0], R2[1], m, n]
                                                return(Res)

print('--------------------RODADA 1--------------------')
print('partida 1')
print('--casa--: time 1')
print('--visitante--: time 2')
a = 'X'
b = 'O'
c = L1
d = L2
e = Q[0]
f = Q[1]
g = R[0]
h = R[1]
i = S[0]
j = S[1]
k = P[0]
l = P[1]
m = SG[0]
n = SG[1]
Resultado1 = rodada_princ_pênaltis(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
print(Resultado1[0], Resultado1[1])
print(Resultado1[2], Resultado1[3])

print('--------------------RODADA 1--------------------')
print('partida 2')
print('--casa--: time 1')
print('--visitante--: time 3')
a = 'X'
b = 'O'
c = L1
d = L3
e = Q[0]
f = Q[2]
g = R[0]
h = R[2]
i = S[0]
j = S[2]
k = P[0]
l = P[2]
m = SG[0]
n = SG[2]
Resultado2 = rodada_princ_pênaltis(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado2[1] = Resultado2[1] + Resultado1[1]
print(Resultado2[0], Resultado2[1])
print(Resultado2[2], Resultado2[3])

print('--------------------RODADA 1--------------------')
print('partida 3')
print('--casa--: time 1')
print('--visitante--: time 4')
a = 'X'
b = 'O'
c = L1
d = L4
e = Q[0]
f = Q[3]
g = R[0]
h = R[3]
i = S[0]
j = S[3]
k = P[0]
l = P[3]
m = SG[0]
n = SG[3]
Resultado3 = rodada_princ_pênaltis(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado3[1] = Resultado3[1] + Resultado2[1]
print(Resultado3[0], Resultado3[1])
print(Resultado3[2], Resultado3[3])

print('--------------------RODADA 1--------------------')
print('partida 4')
print('--casa--: time 1')
print('--visitante--: time 5')
a = 'X'
b = 'O'
c = L1
d = L5
e = Q[0]
f = Q[4]
g = R[0]
h = R[4]
i = S[0]
j = S[4]
k = P[0]
l = P[4]
m = SG[0]
n = SG[4]
Resultado4 = rodada_princ_pênaltis(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado4[1] = Resultado4[1] + Resultado3[1]
print(Resultado4[0], Resultado4[1])
print(Resultado4[2], Resultado4[3])

SgT1 = Resultado1[4] + Resultado2[4] + Resultado3[4] + Resultado4[4]
SgT2 = Resultado1[5]
SgT3 = Resultado2[5]
SgT4 = Resultado3[5]
SgT5 = Resultado4[5]
SgT6 = 0
SgT7 = 0
SgT8 = 0

print('--------------------PONTUAÇÃO FINAL RODADA 1--------------------')

print('PONTUAÇÃO ATUAL')

d = {S[0]:Resultado4[1], S[1]:Resultado1[3], S[2]:Resultado2[3], S[3]:Resultado3[3], S[4]:Resultado4[3], S[5]:P[5], S[6]:P[6], S[7]:P[7]}
for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
d = [('time 1', Resultado4[1], SgT1), ('time 2', Resultado1[3], SgT2), ('time 3', Resultado2[3], SgT3), ('time 4', Resultado3[3], SgT4), ('time 5', Resultado4[3], SgT5), ('time 6', P[5], SgT6), ('time 7', P[6], SgT7), ('time 8', P[7], SgT8)]
d.sort(key=lambda x: (x[1], x[2]), reverse=True)
e = d
lista1 = list(e[0])
lista1.insert(0,'1º')
print(lista1)
lista2 = list(e[1])
lista2.insert(0,'2º')
print(lista2)
lista3 = list(e[2])
lista3.insert(0,'3º')
print(lista3)
lista4 = list(e[3])
lista4.insert(0,'4º')
print(lista4)
lista5 = list(e[4])
lista5.insert(0,'5º')
print(lista5)
lista6 = list(e[5])
lista6.insert(0,'6º')
print(lista6)
lista7 = list(e[6])
lista7.insert(0,'7º')
print(lista7)
lista8 = list(e[7])
lista8.insert(0,'8º')
print(lista8)

print('--------------------RODADA 2--------------------')
print('partida 5')
print('--casa--: time 1')
print('--visitante--: time 6')
a = 'X'
b = 'O'
c = L1
d = L6
e = Q[0]
f = Q[5]
g = R[0]
h = R[5]
i = S[0]
j = S[5]
k = P[0]
l = P[5]
m = SG[0]
n = SG[5]
Resultado5 = rodada_princ_pênaltis(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado5[1] = Resultado5[1] + Resultado4[1]
print(Resultado5[0], Resultado5[1])
print(Resultado5[2], Resultado5[3])

print('--------------------RODADA 2--------------------')
print('partida 6')
print('--casa--: time 1')
print('--visitante--: time 7')
a = 'X'
b = 'O'
c = L1
d = L7
e = Q[0]
f = Q[6]
g = R[0]
h = R[6]
i = S[0]
j = S[6]
k = P[0]
l = P[6]
m = SG[0]
n = SG[6]
Resultado6 = rodada_princ_pênaltis(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado6[1] = Resultado6[1] + Resultado5[1]
print(Resultado6[0], Resultado6[1])
print(Resultado6[2], Resultado6[3])

print('--------------------RODADA 2--------------------')
print('partida 7')
print('--casa--: time 1')
print('--visitante--: time 8')
a = 'X'
b = 'O'
c = L1
d = L8
e = Q[0]
f = Q[7]
g = R[0]
h = R[7]
i = S[0]
j = S[7]
k = P[0]
l = P[7]
m = SG[0]
n = SG[7]
Resultado7 = rodada_princ_pênaltis(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado7[1] = Resultado7[1] + Resultado6[1]
print(Resultado7[0], Resultado7[1])
print(Resultado7[2], Resultado7[3])

print('--------------------RODADA 2--------------------')
print('partida 8')
print('--casa--: time 2')
print('--visitante--: time 3')
a = 'X'
b = 'O'
c = L2
d = L3
e = Q[1]
f = Q[2]
g = R[1]
h = R[2]
i = S[1]
j = S[2]
k = P[1]
l = P[2]
m = SG[1]
n = SG[2]
Resultado8 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado8[1] = Resultado8[1] + Resultado1[3]
Resultado8[3] = Resultado8[3] + Resultado2[3]
print(Resultado8[0], Resultado8[1])
print(Resultado8[2], Resultado8[3])

SgT1 = SgT1 + Resultado5[4] + Resultado6[4] + Resultado7[4]
SgT2 = SgT2 + Resultado8[4]
SgT3 = SgT3 + Resultado8[5]
SgT4 = Resultado3[5]
SgT5 = Resultado4[5]
SgT6 = Resultado5[5]
SgT7 = Resultado6[5]
SgT8 = Resultado7[5]

print('--------------------PONTUAÇÃO FINAL RODADA 2--------------------')

print('PONTUAÇÃO ATUAL')

d = {S[0]:Resultado7[1], S[1]:Resultado8[1], S[2]:Resultado8[3], S[3]:Resultado3[3], S[4]:Resultado4[3], S[5]:Resultado5[3], S[6]:Resultado6[3], S[7]:Resultado7[3]}
for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
d = [('time 1', Resultado7[1], SgT1), ('time 2', Resultado8[1], SgT2), ('time 3', Resultado8[3], SgT3), ('time 4', Resultado3[3], SgT4), ('time 5', Resultado4[3], SgT5), ('time 6', Resultado5[3], SgT6), ('time 7', Resultado6[3], SgT7), ('time 8', Resultado7[3], SgT8)]
d.sort(key=lambda x: (x[1], x[2]), reverse=True)
e = d
lista1 = list(e[0])
lista1.insert(0,'1º')
print(lista1)
lista2 = list(e[1])
lista2.insert(0,'2º')
print(lista2)
lista3 = list(e[2])
lista3.insert(0,'3º')
print(lista3)
lista4 = list(e[3])
lista4.insert(0,'4º')
print(lista4)
lista5 = list(e[4])
lista5.insert(0,'5º')
print(lista5)
lista6 = list(e[5])
lista6.insert(0,'6º')
print(lista6)
lista7 = list(e[6])
lista7.insert(0,'7º')
print(lista7)
lista8 = list(e[7])
lista8.insert(0,'8º')
print(lista8)

print('--------------------RODADA 3--------------------')
print('partida 9')
print('--casa--: time 2')
print('--visitante--: time 4')
a = 'X'
b = 'O'
c = L2
d = L4
e = Q[1]
f = Q[3]
g = R[1]
h = R[3]
i = S[1]
j = S[3]
k = P[1]
l = P[3]
m = SG[1]
n = SG[3]
Resultado9 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado9[1] = Resultado9[1] + Resultado8[1]
Resultado9[3] = Resultado9[3] + Resultado3[3]
print(Resultado9[0], Resultado9[1])
print(Resultado9[2], Resultado9[3])

print('--------------------RODADA 3--------------------')
print('partida 10')
print('--casa--: time 2')
print('--visitante--: time 5')
a = 'X'
b = 'O'
c = L2
d = L5
e = Q[1]
f = Q[4]
g = R[1]
h = R[4]
i = S[1]
j = S[4]
k = P[1]
l = P[4]
m = SG[1]
n = SG[4]
Resultado10 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado10[1] = Resultado10[1] + Resultado9[1]
Resultado10[3] = Resultado10[3] + Resultado4[3]
print(Resultado10[0], Resultado10[1])
print(Resultado10[2], Resultado10[3])

print('--------------------RODADA 3--------------------')
print('partida 11')
print('--casa--: time 2')
print('--visitante--: time 6')
a = 'X'
b = 'O'
c = L2
d = L6
e = Q[1]
f = Q[5]
g = R[1]
h = R[5]
i = S[1]
j = S[5]
k = P[1]
l = P[5]
m = SG[1]
n = SG[5]
Resultado11 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado11[1] = Resultado11[1] + Resultado10[1]
Resultado11[3] = Resultado11[3] + Resultado5[3]
print(Resultado11[0], Resultado11[1])
print(Resultado11[2], Resultado11[3])

print('--------------------RODADA 3--------------------')
print('partida 12')
print('--casa--: time 2')
print('--visitante--: time 7')
a = 'X'
b = 'O'
c = L2
d = L7
e = Q[1]
f = Q[6]
g = R[1]
h = R[6]
i = S[1]
j = S[6]
k = P[1]
l = P[6]
m = SG[1]
n = SG[6]
Resultado12 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado12[1] = Resultado12[1] + Resultado11[1]
Resultado12[3] = Resultado12[3] + Resultado6[3]
print(Resultado12[0], Resultado12[1])
print(Resultado12[2], Resultado12[3])


SgT2 = SgT2 + Resultado9[4] + Resultado10[4] + Resultado11[4] + Resultado12[4]
SgT4 = Resultado9[5]
SgT5 = Resultado10[5]
SgT6 = Resultado11[5]
SgT7 = Resultado12[5]


print('--------------------PONTUAÇÃO FINAL RODADA 3--------------------')

print('PONTUAÇÃO ATUAL')

d = {S[0]:Resultado7[1], S[1]:Resultado12[1], S[2]:Resultado8[3], S[3]:Resultado9[3], S[4]:Resultado10[3], S[5]:Resultado11[3], S[6]:Resultado12[3], S[7]:Resultado7[3]}
for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
d = [('time 1', Resultado7[1], SgT1), ('time 2', Resultado12[1], SgT2), ('time 3', Resultado8[3], SgT3), ('time 4', Resultado9[3], SgT4), ('time 5', Resultado10[3], SgT5), ('time 6', Resultado11[3], SgT6), ('time 7', Resultado12[3], SgT7), ('time 8', Resultado7[3], SgT8)]
d.sort(key=lambda x: (x[1], x[2]), reverse=True)
e = d
lista1 = list(e[0])
lista1.insert(0,'1º')
print(lista1)
lista2 = list(e[1])
lista2.insert(0,'2º')
print(lista2)
lista3 = list(e[2])
lista3.insert(0,'3º')
print(lista3)
lista4 = list(e[3])
lista4.insert(0,'4º')
print(lista4)
lista5 = list(e[4])
lista5.insert(0,'5º')
print(lista5)
lista6 = list(e[5])
lista6.insert(0,'6º')
print(lista6)
lista7 = list(e[6])
lista7.insert(0,'7º')
print(lista7)
lista8 = list(e[7])
lista8.insert(0,'8º')
print(lista8)

print('--------------------RODADA 4--------------------')
print('partida 13')
print('--casa--: time 2')
print('--visitante--: time 8')
a = 'X'
b = 'O'
c = L2
d = L8
e = Q[1]
f = Q[7]
g = R[1]
h = R[7]
i = S[1]
j = S[7]
k = P[1]
l = P[7]
m = SG[1]
n = SG[7]
Resultado13 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado13[1] = Resultado13[1] + Resultado12[1]
Resultado13[3] = Resultado13[3] + Resultado7[3]
print(Resultado13[0], Resultado13[1])
print(Resultado13[2], Resultado13[3])

print('--------------------RODADA 4--------------------')
print('partida 14')
print('--casa--: time 3')
print('--visitante--: time 4')
a = 'X'
b = 'O'
c = L3
d = L4
e = Q[2]
f = Q[3]
g = R[2]
h = R[3]
i = S[2]
j = S[3]
k = P[2]
l = P[3]
m = SG[2]
n = SG[3]
Resultado14 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado14[1] = Resultado14[1] + Resultado8[3]
Resultado14[3] = Resultado14[3] + Resultado9[3]
print(Resultado14[0], Resultado14[1])
print(Resultado14[2], Resultado14[3])

print('--------------------RODADA 4--------------------')
print('partida 15')
print('--casa--: time 3')
print('--visitante--: time 5')
a = 'X'
b = 'O'
c = L3
d = L5
e = Q[2]
f = Q[4]
g = R[2]
h = R[4]
i = S[2]
j = S[4]
k = P[2]
l = P[4]
m = SG[2]
n = SG[4]
Resultado15 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado15[1] = Resultado15[1] + Resultado14[1]
Resultado15[3] = Resultado15[3] + Resultado10[3]
print(Resultado15[0], Resultado15[1])
print(Resultado15[2], Resultado15[3])

print('--------------------RODADA 4--------------------')
print('partida 16')
print('--casa--: time 3')
print('--visitante--: time 6')
a = 'X'
b = 'O'
c = L3
d = L6
e = Q[2]
f = Q[5]
g = R[2]
h = R[5]
i = S[2]
j = S[5]
k = P[2]
l = P[5]
m = SG[2]
n = SG[5]
Resultado16 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado16[1] = Resultado16[1] + Resultado15[1]
Resultado16[3] = Resultado16[3] + Resultado11[3]
print(Resultado16[0], Resultado16[1])
print(Resultado16[2], Resultado16[3])

SgT2 = SgT2 + Resultado13[4]
SgT3 = SgT3 + Resultado16[5]
SgT4 = SgT4 + Resultado14[5]
SgT5 = SgT5 + Resultado15[5]
SgT6 = SgT6 + Resultado16[5]

print('--------------------PONTUAÇÃO FINAL RODADA 4--------------------')

print('PONTUAÇÃO ATUAL')

d = {S[0]:Resultado7[1], S[1]:Resultado13[1], S[2]:Resultado16[1], S[3]:Resultado14[3], S[4]:Resultado15[3], S[5]:Resultado16[3], S[6]:Resultado12[3], S[7]:Resultado13[3]}
for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
d = [('time 1', Resultado7[1], SgT1), ('time 2', Resultado13[1], SgT2), ('time 3', Resultado16[1], SgT3), ('time 4', Resultado14[3], SgT4), ('time 5', Resultado15[3], SgT5), ('time 6', Resultado16[3], SgT6), ('time 7', Resultado12[3], SgT7), ('time 8', Resultado13[3], SgT8)]
d.sort(key=lambda x: (x[1], x[2]), reverse=True)
e = d
lista1 = list(e[0])
lista1.insert(0,'1º')
print(lista1)
lista2 = list(e[1])
lista2.insert(0,'2º')
print(lista2)
lista3 = list(e[2])
lista3.insert(0,'3º')
print(lista3)
lista4 = list(e[3])
lista4.insert(0,'4º')
print(lista4)
lista5 = list(e[4])
lista5.insert(0,'5º')
print(lista5)
lista6 = list(e[5])
lista6.insert(0,'6º')
print(lista6)
lista7 = list(e[6])
lista7.insert(0,'7º')
print(lista7)
lista8 = list(e[7])
lista8.insert(0,'8º')
print(lista8)

print('--------------------RODADA 5--------------------')
print('partida 17')
print('--casa--: time 3')
print('--visitante--: time 7')
a = 'X'
b = 'O'
c = L3
d = L7
e = Q[2]
f = Q[6]
g = R[2]
h = R[6]
i = S[2]
j = S[6]
k = P[2]
l = P[6]
m = SG[2]
n = SG[6]
Resultado17 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado17[1] = Resultado17[1] + Resultado16[1]
Resultado17[3] = Resultado17[3] + Resultado12[3]
print(Resultado17[0], Resultado17[1])
print(Resultado17[2], Resultado17[3])

print('--------------------RODADA 5--------------------')
print('partida 18')
print('--casa--: time 3')
print('--visitante--: time 8')
a = 'X'
b = 'O'
c = L3
d = L8
e = Q[2]
f = Q[7]
g = R[2]
h = R[7]
i = S[2]
j = S[7]
k = P[2]
l = P[7]
m = SG[2]
n = SG[7]
Resultado18 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado18[1] = Resultado18[1] + Resultado17[1]
Resultado18[3] = Resultado18[3] + Resultado13[3]
print(Resultado18[0], Resultado18[1])
print(Resultado18[2], Resultado18[3])

print('--------------------RODADA 5--------------------')
print('partida 19')
print('--casa--: time 4')
print('--visitante--: time 5')
a = 'X'
b = 'O'
c = L4
d = L5
e = Q[3]
f = Q[4]
g = R[3]
h = R[4]
i = S[3]
j = S[4]
k = P[3]
l = P[4]
m = SG[3]
n = SG[4]
Resultado19 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado19[1] = Resultado19[1] + Resultado14[3]
Resultado19[3] = Resultado19[3] + Resultado15[3]
print(Resultado19[0], Resultado19[1])
print(Resultado19[2], Resultado19[3])

print('--------------------RODADA 5--------------------')
print('partida 20')
print('--casa--: time 4')
print('--visitante--: time 6')
a = 'X'
b = 'O'
c = L4
d = L6
e = Q[3]
f = Q[5]
g = R[3]
h = R[5]
i = S[3]
j = S[5]
k = P[3]
l = P[5]
m = SG[3]
n = SG[5]
Resultado20 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado20[1] = Resultado20[1] + Resultado19[1]
Resultado20[3] = Resultado20[3] + Resultado16[3]
print(Resultado20[0], Resultado20[1])
print(Resultado20[2], Resultado20[3])

SgT3 = SgT3 + Resultado17[4] + Resultado18[4]
SgT4 = SgT4 + Resultado19[4] + Resultado20[4]
SgT5 = SgT5 + Resultado19[5]
SgT6 = SgT6 + Resultado20[5]
SgT7 = SgT7 + Resultado17[5]
SgT8 = SgT8 + Resultado18[5]

print('--------------------PONTUAÇÃO FINAL RODADA 5--------------------')

print('PONTUAÇÃO ATUAL')

d = {S[0]:Resultado7[1], S[1]:Resultado13[1], S[2]:Resultado18[1], S[3]:Resultado20[1], S[4]:Resultado19[3], S[5]:Resultado20[3], S[6]:Resultado17[3], S[7]:Resultado18[3]}
for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
d = [('time 1', Resultado7[1], SgT1), ('time 2', Resultado13[1], SgT2), ('time 3', Resultado18[1], SgT3), ('time 4', Resultado20[1], SgT4), ('time 5', Resultado19[3], SgT5), ('time 6', Resultado20[3], SgT6), ('time 7', Resultado17[3], SgT7), ('time 8', Resultado18[3], SgT8)]
d.sort(key=lambda x: (x[1], x[2]), reverse=True)
e = d
lista1 = list(e[0])
lista1.insert(0,'1º')
print(lista1)
lista2 = list(e[1])
lista2.insert(0,'2º')
print(lista2)
lista3 = list(e[2])
lista3.insert(0,'3º')
print(lista3)
lista4 = list(e[3])
lista4.insert(0,'4º')
print(lista4)
lista5 = list(e[4])
lista5.insert(0,'5º')
print(lista5)
lista6 = list(e[5])
lista6.insert(0,'6º')
print(lista6)
lista7 = list(e[6])
lista7.insert(0,'7º')
print(lista7)
lista8 = list(e[7])
lista8.insert(0,'8º')
print(lista8)

print('--------------------RODADA 6--------------------')
print('partida 21')
print('--casa--: time 4')
print('--visitante--: time 7')
a = 'X'
b = 'O'
c = L4
d = L7
e = Q[3]
f = Q[6]
g = R[3]
h = R[6]
i = S[3]
j = S[6]
k = P[3]
l = P[6]
m = SG[3]
n = SG[6]
Resultado21 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado21[1] = Resultado21[1] + Resultado20[1]
Resultado21[3] = Resultado21[3] + Resultado17[3]
print(Resultado21[0], Resultado21[1])
print(Resultado21[2], Resultado21[3])

print('--------------------RODADA 6--------------------')
print('partida 22')
print('--casa--: time 4')
print('--visitante--: time 8')
a = 'X'
b = 'O'
c = L4
d = L7
e = Q[3]
f = Q[7]
g = R[3]
h = R[7]
i = S[3]
j = S[7]
k = P[3]
l = P[7]
m = SG[3]
n = SG[7]
Resultado22 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado22[1] = Resultado22[1] + Resultado21[1]
Resultado22[3] = Resultado22[3] + Resultado18[3]
print(Resultado22[0], Resultado22[1])
print(Resultado22[2], Resultado22[3])

print('--------------------RODADA 6--------------------')
print('partida 23')
print('--casa--: time 5')
print('--visitante--: time 6')
a = 'X'
b = 'O'
c = L5
d = L6
e = Q[4]
f = Q[5]
g = R[4]
h = R[5]
i = S[4]
j = S[5]
k = P[4]
l = P[5]
m = SG[4]
n = SG[5]
Resultado23 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado23[1] = Resultado23[1] + Resultado19[3]
Resultado23[3] = Resultado23[3] + Resultado20[3]
print(Resultado23[0], Resultado23[1])
print(Resultado23[2], Resultado23[3])

print('--------------------RODADA 6--------------------')
print('partida 24')
print('--casa--: time 5')
print('--visitante--: time 7')
a = 'X'
b = 'O'
c = L5
d = L7
e = Q[4]
f = Q[6]
g = R[4]
h = R[6]
i = S[4]
j = S[6]
k = P[4]
l = P[6]
m = SG[4]
n = SG[6]
Resultado24 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado24[1] = Resultado24[1] + Resultado23[1]
Resultado24[3] = Resultado24[3] + Resultado21[3]
print(Resultado24[0], Resultado24[1])
print(Resultado24[2], Resultado24[3])

SgT4 = SgT4 + Resultado22[4]
SgT5 = SgT5 + Resultado24[4]
SgT6 = SgT6 + Resultado23[5]
SgT7 = SgT7 + Resultado24[5]
SgT8 = SgT8 + Resultado22[5]

print('--------------------PONTUAÇÃO FINAL RODADA 6--------------------')

print('PONTUAÇÃO ATUAL')

d = {S[0]:Resultado7[1], S[1]:Resultado13[1], S[2]:Resultado18[1], S[3]:Resultado22[1], S[4]:Resultado24[1], S[5]:Resultado23[3], S[6]:Resultado24[3], S[7]:Resultado22[3]}
for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
d = [('time 1', Resultado7[1], SgT1), ('time 2', Resultado13[1], SgT2), ('time 3', Resultado18[1], SgT3), ('time 4', Resultado22[1], SgT4), ('time 5', Resultado24[1], SgT5), ('time 6', Resultado23[3], SgT6), ('time 7', Resultado24[3], SgT7), ('time 8', Resultado22[3], SgT8)]
d.sort(key=lambda x: (x[1], x[2]), reverse=True)
e = d
lista1 = list(e[0])
lista1.insert(0,'1º')
print(lista1)
lista2 = list(e[1])
lista2.insert(0,'2º')
print(lista2)
lista3 = list(e[2])
lista3.insert(0,'3º')
print(lista3)
lista4 = list(e[3])
lista4.insert(0,'4º')
print(lista4)
lista5 = list(e[4])
lista5.insert(0,'5º')
print(lista5)
lista6 = list(e[5])
lista6.insert(0,'6º')
print(lista6)
lista7 = list(e[6])
lista7.insert(0,'7º')
print(lista7)
lista8 = list(e[7])
lista8.insert(0,'8º')
print(lista8)

print('--------------------RODADA 7--------------------')
print('partida 25')
print('--casa--: time 5')
print('--visitante--: time 8')
a = 'X'
b = 'O'
c = L5
d = L8
e = Q[4]
f = Q[7]
g = R[4]
h = R[7]
i = S[4]
j = S[7]
k = P[4]
l = P[7]
m = SG[4]
n = SG[7]
Resultado25 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado25[1] = Resultado25[1] + Resultado24[1]
Resultado25[3] = Resultado25[3] + Resultado22[3]
print(Resultado25[0], Resultado25[1])
print(Resultado25[2], Resultado25[3])

print('--------------------RODADA 7--------------------')
print('partida 26')
print('--casa--: time 6')
print('--visitante--: time 7')
a = 'X'
b = 'O'
c = L6
d = L7
e = Q[5]
f = Q[6]
g = R[5]
h = R[6]
i = S[5]
j = S[6]
k = P[5]
l = P[6]
m = SG[5]
n = SG[6]
Resultado26 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado26[1] = Resultado26[1] + Resultado23[3]
Resultado26[3] = Resultado26[3] + Resultado24[3]
print(Resultado26[0], Resultado26[1])
print(Resultado26[2], Resultado26[3])

print('--------------------RODADA 7--------------------')
print('partida 27')
print('--casa--: time 6')
print('--visitante--: time 8')
a = 'X'
b = 'O'
c = L6
d = L8
e = Q[5]
f = Q[7]
g = R[5]
h = R[7]
i = S[5]
j = S[7]
k = P[5]
l = P[7]
m = SG[5]
n = SG[7]
Resultado27 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado27[1] = Resultado27[1] + Resultado26[1]
Resultado27[3] = Resultado27[3] + Resultado25[3]
print(Resultado27[0], Resultado27[1])
print(Resultado27[2], Resultado27[3])

print('--------------------RODADA 7--------------------')
print('partida 28')
print('--casa--: time 7')
print('--visitante--: time 8')
a = 'X'
b = 'O'
c = L7
d = L8
e = Q[6]
f = Q[7]
g = R[6]
h = R[7]
i = S[6]
j = S[7]
k = P[6]
l = P[7]
m = SG[6]
n = SG[7]
Resultado28 = rodada_princ_pênaltis_PC(a,b,c,d,e,f,g,h,i,j,k,l,m,n)
Resultado28[1] = Resultado28[1] + Resultado26[3]
Resultado28[3] = Resultado28[3] + Resultado27[3]
print(Resultado28[0], Resultado28[1])
print(Resultado28[2], Resultado28[3])

SgT5 = SgT5 + Resultado25[4]
SgT6 = SgT6 + Resultado26[4] + Resultado27[4]
SgT7 = SgT7 + Resultado26[5] + Resultado28[4]
SgT8 = SgT8 + Resultado25[5] + Resultado27[5] + Resultado28[5]

print('--------------------PONTUAÇÃO FINAL RODADA 6--------------------')

print('PONTUAÇÃO ATUAL')

d = {S[0]:Resultado7[1], S[1]:Resultado13[1], S[2]:Resultado18[1], S[3]:Resultado22[1], S[4]:Resultado25[1], S[5]:Resultado27[1], S[6]:Resultado28[1], S[7]:Resultado28[3]}
for i in sorted(d, key = d.get, reverse=True):
    print(i, d[i])

print('TABELA ATUAL DOS RESULTADOS')
print('(Posição, Time, Pontuação, Saldo de Gols)')
d = [('time 1', Resultado7[1], SgT1), ('time 2', Resultado13[1], SgT2), ('time 3', Resultado18[1], SgT3), ('time 4', Resultado22[1], SgT4), ('time 5', Resultado25[1], SgT5), ('time 6', Resultado27[1], SgT6), ('time 7', Resultado28[1], SgT7), ('time 8', Resultado28[3], SgT8)]
d.sort(key=lambda x: (x[1], x[2]), reverse=True)
e = d
lista1 = list(e[0])
lista1.insert(0,'1º')
print(lista1)
lista2 = list(e[1])
lista2.insert(0,'2º')
print(lista2)
lista3 = list(e[2])
lista3.insert(0,'3º')
print(lista3)
lista4 = list(e[3])
lista4.insert(0,'4º')
print(lista4)
lista5 = list(e[4])
lista5.insert(0,'5º')
print(lista5)
lista6 = list(e[5])
lista6.insert(0,'6º')
print(lista6)
lista7 = list(e[6])
lista7.insert(0,'7º')
print(lista7)
lista8 = list(e[7])
lista8.insert(0,'8º')
print(lista8)
