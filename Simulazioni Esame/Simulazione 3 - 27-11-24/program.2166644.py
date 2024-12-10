#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# type: ignore

"""
#####################    ISTRUZIONI PER LA SIMULAZIONE.  ####################

PRIMA DI TUTTO: Assegna le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Aggiungi le tue implementazioni delle funzioni descritte sotto.
Per ottenere il punteggio esegui il file grade.py contenuto nella cartella.
Per superare la simulazione e' sufficiente ottenere un punteggio maggiore o 
uguale a 18.

Per commentare/decommentare il codice velocemente usate Control + 1 !
"""

nome = 'caio'
cognome = 'sempronio'
matricola  = "2166644"

################################################################################
################################################################################
################################################################################

################################################################################

# %% ----------------------------------- FUNC1 ------------------------- #
""" func1: 6 punti

Si definisca una funzione func1(img_in) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG. La funzione deve restituire il numero dei pixel dell'immagine
il cui canale rosso ha valore maggiore (stretto) di 150.
"""


import images


def func1(img_in) -> int:
    checkImg = images.load(img_in)
    redPixelNumber = 0
    
    for row in checkImg:
        for element in row:
            if(element[0] > 150):
                redPixelNumber += 1
    return redPixelNumber


# %% ----------------------------------- FUNC2 ------------------------- #
""" func2: 8 punti

Definire una funzione che dato il nome di un file (img_in) contenente 
un'immagine, calcola l'immagine il cui canale blu viene incrementato di un 
certo numero di unità val indicato come paramentro (val). 
Quando la somma supera il valore 255, si riparte da 0. Ad es. 240+100 = 85.
L'immagine risultante viene salvata nel file con nome indicato come parametro 
(img_out).
La funzione restituisce il numero di pixel che hanno sforato 255 nel 
canale blu.
Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" 
visto a lezione.
"""


import images


def func2(img_in: str, img_out: str, val: int) -> int:
    loadImage = images.load(img_in)
    newImage = loadEmptyMatric(len(loadImage), len(loadImage[0]))   
    count = 0
    
    for i in range(len(loadImage)):
        for j in range(len(loadImage[0])):
            tupleWhitResult = fixedNumber(loadImage[i][j][2], val)
            newImage[i][j] = (loadImage[i][j][0], loadImage[i][j][1], tupleWhitResult[0])
            
            if(tupleWhitResult[1]):
                count += 1
            
    images.save(newImage, img_out)
    return count
            
    
def fixedNumber(val, toSum):
    temp = val
    flag = False
    for i in range(toSum):
        temp += 1
        if(temp > 255):
            temp = 0
            flag = True
    return (temp, flag)

def loadEmptyMatric(row: int, coll: int):
    newMatrix = []
    
    for i in range(row):
        tempList = []
        for j in range(coll):
            tempList.append(0)
        newMatrix.append(tempList)
            
    return newMatrix

# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 8 punti

Si definisca una funzione func3(input_pngfile) che prende in ingresso
una stringa che contiene il percorso ad un file con un'immagine in
formato PNG. L'immagine indicata dal 'input_pngfile' contiene solo
pixel neri e bianchi. La funzione deve individuare tutti i segmenti
orizzontali di colore bianco e restituirli in una lista.
I segmenti orizzontali su una riga possono essere al più uno.
Inoltre un segmento puo' essere lungo quanto tutta la larghezza
dell'immagine oppure anche lungo solamente un pixel.
La funzione restituiste una lista in cui ogni segmento orizzontale
è codificato come tupla con coordinate (y, xstart, xend),
dove y è il numero di riga, xstart il primo pixel del segmento, xend
l'ultimo pixel del segmento. La lista è ordinata in ordine crescente
in base alla coordinata y.

Ad esempio data l'immagine:

 0 1 2 3 4 5
0. . . . . .
1. . . . . .
2. . x . . .
3. . . . . .
4. . . . . .
5x x x x x x

dove . è nero e x è bianco, la funzione deve restituire:
[(2,2,2), (5,0,5)].

Per vedere i casi di test si vedano le immagini in func5/image01.png etc.
"""

import images


def func3(input_pngfile):
    pass



# %% ----------------------------------- FUNC4 ------------------------- #
''' func4: 8 punti

Si definisca una funzione func4 che prende in input un'immagine RGB.
La funzione conta e restituisce il numero di pixel non neri che sono
preceduti e seguiti da pixel neri (ovvero, dato un pixel P,
c'è un pixel nero che lo precede e uno che lo segue).
Se il pixel non nero si trova al bordo sinistro dell'immagine, si considera 
come pixel che lo precede quello posizionato alla fine della riga. 
Allo stesso modo, se il pixel non nero si trova al bordo destro dell'immagine,
si considera come pixel che lo segue quello posizionato all'inizio della riga.
Inoltre, la funzione salva un'immagine RGB con la stessa larghezza e altezza
dell'immagine di input, in cui sono copiati solo i pixel contati.

Ad esempio, se B rappresenta un pixel nero e * rappresenta
un pixel non nero, data l'immagine:

BB*BBBB*
*BBB*BBB
B*BB**B*
BBBBBB*B
*BBB**BB

La funzione restituisce 8 e salva l'immagine:

BB*BBBB*
*BBB*BBB
B*BBBBB*
BBBBBB*B
*BBBBBBB
'''

import images

def func4(input_file_name, output_file_name):
nome = 'caio'
    newImage = loadEmptyMatric(len(checkImage), len(checkImage[0]))
    checkPixel = 0
    black = (0, 0, 0)
    
    for i in range(len(checkImage)):
        for j in range(len(checkImage[0])):
            if(checkImage[i][j] != black):
                if(j == 0):
                    if(checkImage[i][j + 1] == black):
                        checkPixel += 1
                        newImage[i][j] = checkImage[i][j]
                    else:
                        newImage[i][j] = black
                elif(j == (len(checkImage[0]) - 1)):
                    if(checkImage[i][j - 1] == black):
                        checkPixel += 1
                        newImage[i][j] = checkImage[i][j]
                    else:
                        newImage[i][j] = black
                else:
                    if(checkImage[i][j - 1] == black and checkImage[i][j + 1] == black):
                        checkPixel += 1
                        newImage[i][j] = checkImage[i][j]
                    else:
                        newImage[i][j] = black
                    
            else:
                newImage[i][j] = black
                
    images.save(newImage, output_file_name)
    return checkPixel
                    