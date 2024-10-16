import math
################################################################################
# Esercizi 2 Ottobre 2024
################################################################################

# Ignorate le linee fino alla 18, servono a noi per stampare i risultati dei test
# e per il momento non è necessario che sappiate come funzionano
from typing import Any, Callable, List
# Stampa un test
def print_test(func: Callable, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        print(f'{func_str}({args_str}) => {result_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'ERROR: {func_str}({args_str}) => {error_str}')

################################################################################
# Errori
################################################################################

# Iniziate a prendere familiarità con i messaggi di errore che Python vi da.
# Provate ad introdurre di proposito degli errori e a vedere quale messaggio
# di errore ottenete. Meglio fare errori ora e di proposito(e capirli),
# piuttosto che accidentalmente in seguito e non riuscire a capire dov'è
# l'errore. Ad esempio:


# Cosa succede se dimenticate gli apici alla fine di una stringa?

# Cosa succede se dividete un numero per `0`?

# Cosa succede se in una istruzione di stampa(print) dimenticate una o
# entrambe le parentesi?

# Per esprimere un numero negativo, si antepone il segno meno (ad esempio, `-2`).
# Cosa succede se anteponete il segno `+?` e se fate `2++2`?

# Nella notazione matematica, gli `0` iniziali sono ammessi (ad esempio, `02`).
# Cosa succede in Python?

# Nella notazione matematica, possiamo omettere il simbolo di moltiplicazione.
# Ad esempio `x*y` può essere scritto come `xy`. E' permesso anche in Python?

# In Python possiamo assegnare un numero ad una variabile, ad esempio: `n = 42`.

# Cosa succede se facciamo `42 = n`?

# Cosa succede con `x = y = 1`?

# In alcuni linguaggi, come il C, ogni istruzione termina con un punto e
# virgola (`;`). Cosa succede se mettiamo un punto e virgola alla fine di
# un'istruzione Python? E se mettiamo un punto?

################################################################################
# Calcoli
################################################################################

# Scrivete una espressione che calcoli il numero di secondi che ci sono in
# 42 minuti e 42 secondi.

# Scrivete una espressione che calcoli il numero di miglia che ci sono in
# 10 chilometri. (1 miglio=1.61 km).

# Scrivete una espressione che calcoli la velocità media e la cadenza media
# (tempo per miglio, in minuti e secondi) di un corridore che corre una gara
# di 10 chilometri in 42 minuti e 42 secondi.

# Il volume di una sfera di raggio `r` è `4/3 * PI * r ^ 3`.
# Scrivere una espressione che calcoli il volume di una sfera di raggio 5.

# Il prezzo di copertina di un libro è 24.95, ma una liberia ottiene il 40%
# di sconto. I costi di spedizione sono 3 euro per la prima copia, e 75
# centesimi per ogni copia aggiuntiva. Qual'è il costo totale di 60 copie?

# Se uscite di casa alle 6: 52 di mattina e correte un miglio a ritmo blando
# (8 minuti e 15 secondi al miglio), e poi 3 miglia a ritmo moderato
# (7 minuti e 12 secondi al miglio), e infine un altro miglio a ritmo blando
# (9 minuti e 45 secondi al miglio), a che ora sarete tornati a casa?

################################################################################
# Stringhe
################################################################################

# Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale.
# Ad esempio, `s = "85721"`. Stampate la somma delle cifre contenute nella stringa.
def dec_str_to_dec(s):
    somma = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4])
    print(somma)
                                                                  
                                                                     

print("Result of dec_str_to_dec: ", end="")
dec_str_to_dec("85721")

# Scrivete una espressione che a partire da una stringa di 5 caratteri,
# rappresentante un numero binario, stampi la sua rappresentazione decimale.
# Ad esempio, `s = "00101" -> 5`.
def bin_str_to_dec(s):
    print (int(s, 2))

print("Result of bin_str_to_dec: ", end="")
bin_str_to_dec("00101")

# Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale
# ('.'). Ad esempio, s = "52.29". Stampare il numero decimale rappresentato
# dalla stringa(stamparlo come numero, non come stringa).
def dec_frac_str_to_dec(s):
    print(float(s))

print("Result of dec_frac_str_to_dec: ", end="")
dec_frac_str_to_dec("52.29")

################################################################################
# Funzioni
################################################################################
# Scrivere una funzione che prende un numero in virgola mobile, ne calcola la
# radice cubica, e la ritorna.
def cubic_root(n):
    return n ** 3

# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e ritorna la maggiore.
# Se le radici sono complesse, la funzione restituisce una qualsiasi
# delle due radici
def root_max(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta >= 0:
        r1 = ((b + math.sqrt(delta)) / 2 * a)
        r2 = ((b - math.sqrt(delta)) / 2 * a)
    else:
        r1 = 0
        r2 = 0
    return max(r1, r2)

# Scrivere una funzione che prende tre numeri in virgola mobile(`a`, `b`, `c`)
# e calcola le radici dell'equazione `a x ^ 2 + b x + c` e le ritorna entrambe.
def roots(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta >= 0:
        r1 = ((b + math.sqrt(delta)) / 2 * a)
        r2 = ((b - math.sqrt(delta)) / 2 * a)
    else:
        r1 = 0
        r2 = 0
    return (r1, r2)

# Scrivere una funzione che prende come input cinque numeri e ritorna la somma
# dei numeri pari meno quella dei numeri dispari.
def even_minus_odd(a, b, c, d, e):
    even = 0
    odd = 0
    if (a % 2) == 0:
        even += a
    else:
        odd += a
    if (b % 2) == 0:
        even += b
    else:
        odd += b
    if (c % 2) == 0:
        even += c
    else:
        odd += c
    if (d % 2) == 0:
        even += d 
    else:
        odd += d
    if (e % 2) == 0:
        even += e
    else:
        odd += e
                        
    return (even - odd)
    

# Scrivere una funzione che prende tre valori di input, e ritorna la
# loro somma se i valori sono punteggi di esame validi(`0 <= grade <= 30`),
# e altrimenti ritorna `- 1`. Scriverne poi una variante che legge i valori da
# terminale con `input`.
def check_grade(a, b, c):
    result = 0
    if 0 <= a <= 30:
        result += a
    else:
        return -1
    if 0 <= b <= 30:
        result += b
    else:
        return -1
    if 0 <= c <= 30:
        result += c
    else:
        return -1
    
    return result

# Scrivere una funzione che prende tre valori(`d`, `m`, `y`) e ritorna se la
# data è valida o no. Si possono ignorare gli anni bisestili. Ad esempio,
# ritorna `False` per `30/2/2017` e `True` per `1/1/1111`.
def check_date(d, m, y):
    pass

# Scrivere una funzione che ritorna una stringa di saluto formata da
# `Ciao `, seguito dal nome letto come input e poi da `Buona giornata!`
def print_hello():
    s = input("inserisci il tuo nome: ")
    return "Ciao " + s

print_test(cubic_root, 8)
print_test(cubic_root, -1)
print_test(root_max, 2, 3, 4)
print_test(root_max, 1, 200, 4)
print_test(roots, 2, 3, 4)
print_test(roots, 1, 200, 4)
print_test(even_minus_odd, 2, 4, 1, 3, 6)
print_test(even_minus_odd, 2, 2, 2, 2, 2)
print_test(even_minus_odd, 1, 1, 1, 1, 1)
print_test(check_grade, 21, 18, 2)
print_test(check_grade, 21, 32, 2)
print_test(check_grade, 21, 18, -2)
print_test(check_date, -1, 12, 2011)
print_test(check_date, 1, 14, 2011)
print_test(check_date, 1, 12, -1)
print_test(check_date, 31, 4, 2011)
print_test(check_date, 30, 4, 2011)
print_test(print_hello)