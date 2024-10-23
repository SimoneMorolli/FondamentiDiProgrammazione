#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Implementa una funzione leetv(line) che prende come input una stringa
line e la modifica in modo da avere una versione della stringa in
formato leetspeak. Esempio: `Programming Unit 1` diventa `pR09R4mm1N9_uN1t_1`
Per creare la stringa usare le seguenti regole:

    1) 'a', 'i', 'e', 'o', 'z', 's', e 'g'
       devono essere sostituite con
       '4', '1', '3', '0', '7', '5', e '9' rispettivamente
       a prescindere che siano lower- or UPPER-case
       (quindi la solita regola si applica a
       'A', 'I', 'E', 'O', 'Z', 'S', e 'G', rispettivamente);

    2) 'f', 'n', 'r', 'w', 'l', 'y' e 'x'  (lower-case) devono essere
       sostituite con la loro versione UPPER-case
       ('F', 'N', 'R', 'W', 'L', 'Y' e 'X', rispettivamente);
    3) tutte gli altri caratteri UPPER-case non menzionati in
       in (1) e (2) devono diventare lower-case (e.g., 'B' diventa 'b',
       mentre 'N' rimane 'N');
    4) ' ' (spazio) deve diventare '_' (underscore);
    5) tutti gli altri caratteri non devono cambiare

   La funzione deve ritornare una tupla definita come:
   - primo elemento della tupla contiene la stringa in leet-version
   - il secondo elemento e' un numero che conta il numero di caratteri
     sostituiti

   Ad esempio input e' `"My name is Neo"`, la funzione
   deve ritornare `('mY_N4m3_15_N30', 12)`.
"""
# ---------------------------------------------------------------------- #
#            INPUT                      EXPECTED OUTPUT
# tests = [('My name is Neo',             ('mY_N4m3_15_N30', 12),),
#          ('Follow the White Rabbit!',   ('F0LL0W_th3_Wh1t3_R4bb1t!', 13)),
#          ('What is the Matrix?',        ('Wh4t_15_th3_m4tR1X?', 12))]
# ----------------------------------------------------------------------- #
def characterToNumber(character: str) -> str:
    newString = ""
    if(character == "a" or character == "A"):
        newString = "4"
    elif(character == "i" or character == "I"):
        newString = "1"
    elif(character == "e" or character == "E"):
        newString = "3"
    elif(character == "o" or character == "O"):
        newString = "0"
    elif(character == "z" or character == "Z"):
        newString = "7"
    elif(character == "s" or character == "S"):
        newString = "5"
    elif(character == "g" or character == "G"):
        newString = "9"
    else:
        newString = "not"
    return newString

def conditionCharacterToUpper(line: str) -> bool:
    lowerControll = line == "f" or line == "n" or line == "r" or line == "w" or line == "l" or line == "y" or line == "x"
    return lowerControll

def conditionCharacterAlreadyUpper(line: str) -> bool:
    upperControll = line == "F" or line == "N" or line == "R" or line == "W" or line == "L" or line == "Y" or line == "X"
    return upperControll

def onlyLetterOrWhitespace(string: str) -> bool:
    checkOnlyUpperLetter = 65 <= ord(string) <= 90
    checkOnlyLowerLetter = 97 <= ord(string) <= 122
    checkWhitespace = string == " "

    return checkOnlyLowerLetter or checkOnlyUpperLetter or checkWhitespace
    
def leetv(line):
    characterCount = 0
    newString = ""
    
    for i in range(len(line)):
        if(onlyLetterOrWhitespace(line[i])):
            if(characterToNumber(line[i]) != "not"):
                newString += characterToNumber(line[i])
                characterCount += 1

            elif(conditionCharacterToUpper(line[i]) or conditionCharacterAlreadyUpper(line[i])):
                newString += line[i].upper()

                if(conditionCharacterToUpper(line[i])):
                    characterCount += 1
    
            elif(line[i] == " "):
                newString += "_"
                characterCount += 1
            
            elif(line[i].islower() != 1):
                newString += line[i].lower()
                characterCount += 1
            else:
                newString += line[i]
        else:
            newString += line[i]
            
    return (newString, characterCount)
    

if __name__ == '__main__':
    # Valutazione
    tests = [('My name is Neo', ('mY_N4m3_15_N30', 12),),
             ('Follow the White Rabbit!', ('F0LL0W_th3_Wh1t3_R4bb1t!', 13)),
             ('What is the Matrix?', ('Wh4t_15_th3_m4tR1X?', 12))]

    # se assert vi da errore controllate il vostro output rispetto a
    # quello atteso. Se passate un test vi stampa > Test xx PASSED !
    for i, (inp, expt) in enumerate(tests, 1):
        out = leetv(inp)
        assert out == expt, f'\n{"="*50}\noutput {out}\nexpected {expt}\n{"="*50}'
        print(f'> Test {i} PASSED!')
