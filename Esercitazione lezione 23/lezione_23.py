# -*- coding: utf-8 -*-

def fact(n):
    return n*fact(n-1) if n > 1 else 1

# %% Permutazioni (bottom-up, al ritorno)
def perm(x):
    # se x ha lunghezza 0 o 1
    # allora caso base
    N = len(x)
    if N < 2:
        return x # stringa
    rez = [] # lista di stringhe
    # per tutti gli elementi
    for i in range(N):
        # togliamo elemento corrente
        # da 0 a i escluso U da i+1 incluso alla fine
        x_minus_i = x[:i] + x[i+1:] # nota i+1 sborda su ultima iterazione for!
        for each_str_perm in perm(x_minus_i): # for stringa in lista or for char in str
            # assemblo i-th con permutazioni su X \ {i}
            rez.append(x[i] + each_str_perm) #char + char or char + str
    return rez #lista di stringhe

# o _ _ _ 

# %%% eval perm 1
S = 'abc'
permutated_a = perm(S)
print(permutated_a)
print('*'*50)
# la lunghezza delle permutazioni
# deve essere uguale al fattoriale della lunghezza 
# della stringa iniziale
#assert len(permutated_a) == fact(len(S))
# %%% eval perm 2
S = '🎃🤖😎😍'
permutated_a = perm(S)
print(permutated_a)
#assert len(permutated_a) == fact(len(S))

# %% Permutazioni (top-down, all'andata)
def perm(x, part_str=''):
    # se  x ha lunghezza 0 o 1
    # allora caso base
    N = len(x)
    # se empty string
    # allora partial_str e' completa
    if N == 0:
        return [part_str] # list OK
    rez = []
    # per tutti gli elementi
    for i in range(N):
        # togliamo elemento corrente
        # da 0 a i escluso U da i+1 incluso alla fine
        x_minus_i = x[:i] + x[i+1:]
        # estendo rez con le permutazioni su N-1
        # (controllo sui tipi) torna chiamo extend su list
        # in quanto perm() mi rende list
        rez.extend(perm(x_minus_i, part_str=part_str+x[i])
    return rez #list

# %%% eval perm 1
S = 'abc'
permutated_b = perm(S)
print(permutated_b)
print('*'*50)
# la lunghezza delle permutazioni
# deve essere uguale al fattoriale della lunghezza 
# della stringa iniziale
assert len(permutated_b) == fact(len(S))
# %%% eval perm 2
S = '🎃🤖😎😍'
permutated_b = perm(S)
print(permutated_b)
#assert len(permutated_b) == fact(len(S))
assert permutated_b == permutated_a

# %% Permutazioni (top-down, all'andata bloccando prima) 
def perm(x, part_str=''):
    # se  x ha lunghezza 0 o 1
    # allora caso base
    N = len(x)
    # se empty string
    # allora partial_str e' completa
    if N == 0:
        # partial str e' completa
        return [part_str] # list
    if N == 1:
        # partial str manca un char
        return [part_str + x] # list
    if N == 2:
        # x lungo  2
        # va messo prima x e poi suo inverso
        return  [part_str+x, part_str+x[::-1]] # list
    # N == 3 sono 6 casi quindi meglio non scriverlo
    rez = []
    # per tutti gli elementi
    for i in range(N):
        # togliamo elemento corrente
        # da 0 a i escluso U da i+1 incluso alla fine
        x_minus_i = x[:i] + x[i+1:]
        # estendo rez con le permutazioni su N-1
        # (controllo sui tipi) torna chiamo extend su list
        # in quanto perm() mi rende list
        rez.extend(perm(x_minus_i, part_str=part_str+x[i]))
    return rez #list

# %%% eval perm 1
S = 'abc'
permutated_c = perm(S)
print(permutated_c)
print('*'*50)
# la lunghezza delle permutazioni
# deve essere uguale al fattoriale della lunghezza 
# della stringa iniziale
assert len(permutated_c) == fact(len(S))
# %%% eval perm 2
S = '🎃🤖😎😍'
permutated_c = perm(S)
print(permutated_c)
assert len(permutated_c) == fact(len(S))
assert permutated_c == permutated_b == permutated_a

# %% Merge sort
# 1. riduzione -> divido la mia lista disordinata in 2 parti
# 2. caso base -> colpisco un singolo elemento (e' ordinato!)
# 3. convergenza -> dividendo in 2 arrivo ad un solo elemento
# 4. conquer dati due o piu elmenti/liste ORDINATI devo fare un merge 

from rtrace import TraceRecursion

@TraceRecursion
def merge_sort(L):
    N = len(L)
    if N == 1 or not L:
        return L # lista
    half = N//2
    L_a = merge_sort(L[:half]) #half escluso
    L_b = merge_sort(L[half:]) #half incluso
    # qui le devo unire ma devo mantenere ordinamento
    return L_a + L_b # unisco 2 liste

# eval %%% Merge sort
L = [3, 5, -2, -100, 29]
print(merge_sort(L))
merge_sort.trace(L) #anche se non funziona, faccio molto in realta'
# perche COPRO l'andata della ricorsione
# ora dobbiamo fare il ritorno

# %% Merge

# A -1, 100, 2000
# B 10, 101, 140
#  |
# confrontiamo elemento i-esimo
# prendiamo il minore
# i=0 ###################
# A -1,| 100, 2000
# B 10, 101, 140
# preso -1, posso riapplicare merge
# i=1 ###################
# A -1,| 100, 2000
# B 10,| 101, 140
# preso 10 posso riapplicare merge
# i=2 ###################
# A -1, 100,| 2000
# B 10,| 101, 140
# preso 100 posso riapplicare merge
# i=3 ###################
# A -1, 100,| 2000
# B 10, 101,| 140
# preso 101 posso riapplicare merge
# i=4 ###################
# A -1, 100,| 2000
# B 10, 101, 140 |
# preso 140 posso riapplicare merge
# i=4 ###################
# A -1, 100,| 2000
# B 10, 101, 140 |
# preso 2000 torno su

def merge(La,Lb):
    # if not La: return Lb
    # if not Lb: return La
    # sono entrambe piene
    assert len(La) >=1 and len(Lb) >=1
    a, *rest_a = La
    b, *rest_b = Lb
    if a <= b:
        return [a] + merge(rest_a, Lb) if rest_a else [a]+Lb # ho messo qui i casi base
    else:
        return [b] + merge(La, rest_b) if rest_b else [b]+La # caso base qui

@TraceRecursion
def mergesort(L):
    N = len(L)
    if N < 2:
        return L
    half = N//2
    La_sorted = mergesort(L[:half]) #half escluso
    Lb_sorted = mergesort(L[half:]) #half incluso
    sortedd = merge(La_sorted, Lb_sorted)
    # qui le devo unire ma devo mantenere ordinamento
    return sortedd



# %%% eval full Merge sort
L = [3, 5, -2, -100, 29]
print(mergesort(L))
L = [3]
print(mergesort(L))
L = []
print(mergesort(L))
L = [3, 5, -2, -100]
print(mergesort(L))


# %%% PER CASA

# Es 4: 9 punti

# Si progetti e implementi la funzione ricorsiva ex4(S) che prende in
# ingresso una sequenza sottoforma di stringa S e restitusica tutte le
# PERMUTAZIONI della stringa S.

# Ad esempio data S='abc' (si visualizza i rispettivi indici anche):

#  | indici | 0 | 1 | 2 |
#  | S      | a | b | c |

# le permutazioni devono essere restituite in questo ordine,
# partendo da indici più grandi di S via via a scendere:

#     | numero | P   |   indici |
#     |   perm |     | da S per |
#     |        |     |   fare P |
#     |--------+-----+----------|
#     |      1 | cba |      210 |
#     |      2 | cab |      201 |
#     |      3 | bca |      120 |
#     |      4 | bac |      102 |
#     |      5 | acb |      021 |
#     |      6 | abc |      012 |

# Ultima colonna significa che 'cba' = S[2]+S[1]+S[0].

# La funzione deve restituire una tupla di liste. Ciascuna lista
# rappresenta una permutazione P generata come descritto in alto.
# La lista P consta di coppie (tuple) formate da indice di S e
# carattere.  

# Ad esempio:
#   P = 'cba' --> [(2, 'c'), (1, 'b'), (0, 'a')]

# Il risultato per S='abc' è quindi:
# (
#  [(2, 'c'), (1, 'b'), (0, 'a')],
#  [(2, 'c'), (0, 'a'), (1, 'b')],
#  [(1, 'b'), (2, 'c'), (0, 'a')],
#  [(1, 'b'), (0, 'a'), (2, 'c')],
#  [(0, 'a'), (2, 'c'), (1, 'b')],
#  [(0, 'a'), (1, 'b'), (2, 'c')]
# )

# Si ricorda che le permutazioni di N elementi sono N! = N*(N-1)!
# perché, bloccato un elemento che può andare in N posizioni diverse, vi
# sono altre N-1 permutazioni.

def perm_index(S):
    # inserisci qui il tuo codice
    pass

