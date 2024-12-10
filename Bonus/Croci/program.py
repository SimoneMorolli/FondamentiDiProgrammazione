#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da svolgere PRIMA DI TUTTO:
 1) Salvare questo file come program.py
 2) Indicare nelle variabili in basso il proprio
    NOME, COGNOME e NUMERO DI MATRICOLA
"""

nome        = "Simone"
cognome     = "Morolli"
matricola   = "2166644"

################################################################################
################################################################################
################################################################################
# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #
# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la
# lista 'test' è assegnata alla fine di grade.py
#
# Per controllare lo stack trace degli errori, si può decommentare la linea
# dedicata in testlib.py (vedere il commento nel corpo della funzione runOne)
################################################################################


# ----------------------------------- EX.2 ----------------------------------- #


"""
Es 2: 7 punti
Viene fornita un'immagine con sfondo nero al cui interno sono presenti
un numero variabile di croci, che possono avere colori sia diversi
sia uguali fra loro.  Ciascuna croce è composta da due linee, una
orizzontale e una verticale che si incontrano. Le linee hanno
spessore di 1 pixel e possono essere di lunghezza diversa.  Due croci
arbitrarie non possono sovrapporsi e c'è sempre almeno un pixel di sfondo
fra le due. Ciascun lato/braccio della croce è lungo almeno un pixel.

Consiglio: prima di iniziare vedere le immagini nella dir 'crosses/'

Si progetti e implementi la funzione ex2 che prende in ingresso
l'immagine suddetta e individua tutte le croci. Ogni croce deve essere
descritta come una tupla di 4 punti più la tupla del colore.
I 4 punti sono nell'ordine "alto", "basso", "sinistra", "destra", dove:
    - "alto" è il punto più in alto,
    - "basso" è il punto più in basso,
    - "sinistra" è il punto più a sinistra,
    - "destra" è il punto più a destra.
Ogni punto è una tupla di coordinate y, x, dove y è la riga e x la colonna.

Ad esempio, la croce seguente:

     0 1 2 3 4
   0 . . . . .
   1 . . x . .
   2 . x x x x
   3 . . x . .
   4 . . x . .
   5 . . . . .

                    alto   basso   sx     dx       colore
è descritta da:  ((1, 2), (4,2), (2, 1), (2, 4), (r, g, b))

La funzione deve ritornare tutte le croci individuate come un dizionario
che ha:
- come chiavi i colori delle croci
- come valore un insieme con tutte le croci del colore indicato
  dalla chiave.
"""

import images

def ex2(path_to_im):
    checkImg = images.load(path_to_im)
    indexList = findAllCenter(checkImg)
    dictionaryResult = {}
    
    for element in indexList:
        tempList = findLengCross(element, checkImg)
        color = tempList[4]
        tempList.pop(4)
        if (color in dictionaryResult.keys()):
            dictionaryResult[color].append(tempList)
        else:
            dictionaryResult[color] = [tempList]

    return dictionaryResult

def findLengCross (index, img):
    i = index[0]
    j = index[1]
    resultList = []
    
    while(img[i][j] != (0, 0, 0) and j >= 0):
        j -= 1
        
    resultList.append((i, j + 1))
    i = index[0]
    j = index[1]
    
    while(img[i][j] != (0, 0, 0) and j <= len(img[0])):
        j += 1
        
    resultList.append((i, j - 1))
    i = index[0]
    j = index[1]
    
    while(img[i][j] != (0, 0, 0) and j >= 0):
        i -= 1
        
    resultList.append((i + 1, j))
    i = index[0]
    j = index[1]
    
    while(img[i][j] != (0, 0, 0) and j <= len(img[0])):
        i += 1
        
    resultList.append((i - 1,j))
    resultList.append(index[2])
    
    return resultList
    

def findAllCenter (img):
    centerList = []
    
    for i in range(len(img)):
        for j in range(len(img[0])):
            if(img[i][j] != (0,0,0)):
                if(img[i + 1][j] != (0,0,0) and img[i][j + 1] != (0,0,0) and img[i][j - 1] != (0,0,0) and img[i - 1][j] != (0,0,0)):
                    centerList.append((i, j, img[i][j]))
    return centerList        
            
if __name__ == '__main__':
    # inserisci qui i tuoi test
    print('*'*50)
    print('Devi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print('Altrimenti puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*'*50)
    pass
