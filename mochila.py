import numpy  as np
import random as rd

def Gerar_Problema(n,me1,ma1,me2,ma2):
    tp = np.random.randint(me1,ma1,n)
    pr = np.random.randint(me2,ma2,n)
    
    return tp,pr

def Solucao_Inicial(n,c_max,tp):
    s = np.zeros(n,int)
    
    v = 0
    while v<c_max:
        ind = rd.randrange(0,n)
        if s[ind]==0:
            s[ind] = 1
            v += tp[ind]
    s[ind] = 0
    return s

def Avalia(n,s,tp,pr):
    valor = 0
    for i in range(n):
        valor += tp[s[i]]*(1./pr[s[i]])*s[i]
    return valor

N          = 10     # TOTAL DE CLIENTES
CAPACIDADE = 100    # CAPACIDADE DA MOCHILA

MIN_TP       = 10   # VALOR MÍNIMO PARA O TEMPO
MAX_TP       = 50   # VALOR MÁXIMO PARA O TEMPO
MIN_PRI      = 1    # VALOR MÍNIMO PARA PRIORIDADE
MAX_PRI      = 6    # VALOR MÁXIMO PARA PRIORIDADE

tempo, prior = Gerar_Problema(N,MIN_TP,MAX_TP,MIN_PRI,MAX_PRI)
print("Tempos: ",tempo)
print("Prioridade: ",prior)

si = Solucao_Inicial(N,CAPACIDADE,tempo)
print("\nSolução inicial")
print(si)


vi = Avalia(N,si,tempo,prior)
print("Avaliação da solução: ",vi)
