#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

# Operazioni da svolgere PRIMA DI TUTTO:
# 1) Salvare questo file come program.py
# 2) Indicare nelle variabili in basso il proprio
#    NOME, COGNOME e NUMERO DI MATRICOLA

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla FINE di grade.py
#
# Per debuggare le funzioni ricorsive potete disattivare il test di ricorsione
# settando DEBUG=True nel file grade.py
#
# DEBUG=True vi attiva anche lo STACK TRACE degli errori per sapere il numero
# di linea di program.py che genera l'errore.
################################################################################



# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex2: 8 punti

Si definisca la funzione ex2(L, bg, color, step, file_out) che prende
in ingresso un intero L (larghezza immagine), una tupla bg che indica il
colore di sfondo e una tupla color che indica il colore di
foreground, infine, step che è un intero.
La funzione deve creare un'immagine quadrata di lato L in cui sono
disegnati dei quadrati concentrici di colore color.
I quadrati sono disegnati a partire dal punto (0,0),
saltando di un numero di pixel pari a step.
La funzione deve ritornare, poi, il numero di pixel che
non sono del colore di sfondo bg e salvare l'immagine in file_out.

Ad esempio, se L= 10 e step vale 2, l'immagine da costruire può essere
immaginata come:
    
    1 1 1 1 1 1 1 1 1 1
    1 * * * * * * * * 1
    1 * 2 2 2 2 2 2 * 1
    1 * 2 * * * * 2 * 1
    1 * 2 * 3 3 * 2 * 1
    1 * 2 * 3 3 * 2 * 1
    1 * 2 * * * * 2 * 1
    1 * 2 2 2 2 2 2 * 1
    1 * * * * * * * * 1
    1 1 1 1 1 1 1 1 1 1

in cui * è il colore di sfondo (bg), 1 sono i punti del primo quadrato,
2 i punti del secondo e 3 i punti del terzo.
In generale, prima si disegna il quadrato con i punti 1, poi quello con
i 2 e poi quello con i 3 e così via fino ad arrivare a meta' immagine.  I
quadrati sono tutti del colore color. Nel caso in cui L sia
dispari non si disegna il pixel che rimane, ossia basta
arrivare a disegnare fino L//2-1 compreso.

Si veda immagine in ex2/ex2_expected_A.png che corrisponde all'esempio
di sopra.

Per salvare l'immagine si usi la funzione images.save.
"""

import images
     
def ex2(L, bg, color, step, file_out):
    # INSERISCI QUI IL TUO CODICE
    pass
    

###################################################################################
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('*'*50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenit puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    print('ENG\nYou have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)
