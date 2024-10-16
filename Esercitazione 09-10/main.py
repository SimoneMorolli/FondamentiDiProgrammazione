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
# Stringhe
################################################################################


# Scrivere una funzione che restituisce una stringa di saluto formata da
# `Ciao `, seguito dal nome come parametro, e poi da `Buona giornata!`
def make_hello(name: str) -> str:
    newstring = "Ciao " + str(name) + ". Buona giornata!"
    return newstring


# Scrivere una funzione che implenta la stessa funzionalità di `str.strip()`,
# che rimuove spazi all'inizio e alla fine della stringa.
# Usare solo costrutti del linguaggio e non librerie.
def strip_whitespace(string: str) -> str:
    start_spaces=0
    end_spaces=0
    #strip start
    for i in range (len(string)):
        if(string[i] == " "): 
            start_spaces+=1
        else: 
            break
    for i in reversed(range(len(string)-1)):
        if(string[i] == " "):
            end_spaces+=1
        else: 
            break 
    return string[start_spaces:(len(string)-end_spaces-1)]


# Scrivere una funzione che implenta la stessa funzionalità di `str.split()`,
# rimuovendo uno dei caratteri presi in input. Non ritornare stringhe vuote.
# Usare solo costrutti del linguaggio e non librerie.
def split_string(string: str, characters: str = '') -> List[str]:
    templist = []
    start=0
    for i in range (len(string)):
        if(i==len(string)-1): templist.append(string[start::])
        if(string[i] == characters):
           templist.append(string[start:i])
           start=i
           
    for i in range(len(templist)):
        if(templist[i] == ""):
            templist.remove(templist[i])
    return templist


# Scrivere una funziona che si comporta come `str.replace()`.
# Usare solo costrutti del linguaggio e non librerie.
def replace_substring(string: str, find: str, replace: str) -> str:
    start=0
    newString=""
    wordToFindLength = len(find)
    
    for i in range(len(string)):
        if(string.find(find, start) == -1):
            break
        else:
                newString += string[start:string.find(find, start)] + replace
                start = string.find(find, start) + wordToFindLength
    newString += string[start::]
    return newString


# Scrivere una funzione che codifica un messaggio con il cifrario di
# Cesare, che sostituisce ad ogni carattere il carattere che si
# trova ad un certo offset nell'alfabeto. Quando si applica l'offset,
# si riparte dall'inizio se necessario (pensate a cosa fa il modulo).
# La funzione permette anche di decrittare un messaggio applicando
# l'offset in negativo. Si può assumere che il testo è minuscolo e
# fatto delle sole lettere dell'alfabeto inglese e spazi che non sono crittati.
# Suggerimento: Sono utili le funzioni `ord()` e `chr()`.
def caesar_cypher(string: str, offset: int, decrypt: bool = False) -> str:
    newString = ""
    
    if(decrypt):
        for i in range (len(string)):
            if(string[i] != " "):
                newCharacterIndexValue = (ord(string[i]) - offset)
                while (newCharacterIndexValue < 97):
                    newCharacterIndexValue += 25
                    print(newCharacterIndexValue)
                newString += chr(newCharacterIndexValue)
            else:
                newString += " "
    else:
        for i in range (len(string)):
            if(string[i] != " "):
                newCharacterIndexValue = (ord(string[i]) + offset)
                
                while (newCharacterIndexValue > 122):
                    newCharacterIndexValue -= 25
                    print(newCharacterIndexValue)
                    
                newString += chr(newCharacterIndexValue)
            else:
                print("la stringa è vuota e gli aggiungo uno spazio")
                newString += " "
                
    return newString
        
            


# Test funzioni
print_test(make_hello, 'Pippo')
print_test(strip_whitespace, '  Pippo  ')
print_test(strip_whitespace, '   ')
print_test(split_string, 'Pippo Pluto  ', ' \t\r\n')
print_test(split_string, 'Pippo   Pluto  ', ' \t\r\n')
print_test(replace_substring, 'Ciao Pippo. Ciao Pluto.', 'Ciao', 'Hello')
print_test(caesar_cypher, 'ciao pippo', 17, False)
print_test(caesar_cypher, 'tzrg hzhhg', 17, True)

################################################################################
# Liste
################################################################################


# Scrivere una funzione che somma i quadrati degli elementi di una lista.
def sum_squares(elements: List[int]) -> int:
    summ = 0 
    for i in range (len(elements)):
        summ += elements[i] ** 2
    return summ
# Scrivere una funzione che ritorna il valore massimo degli elementi di una lista.
def max_element(elements: List[int]) -> int:
    pass


# Scrivere una funzione che rimuove i duplicati da una lista.
# Commentare sul tempo di esecuzione.
def remove_duplicates(elements: list) -> list:
    pass


# Scrivere una funzione che si comporta come `reverse()`.
# Usare solo costrutti del linguaggio e non librerie.
def reverse_list(elements: list) -> list:
    pass


# Scrivere una funzione `flatten_list()` che prende una lista che contiene
# elementi o altre liste, e restituisce una lista contenente tutti gli elementi.
# Si può assumere che le liste contenute non contengono altre liste.
# Usare la funzione `isinstance()` per determinare se un elemento è una lista.
# Usare solo costrutti del linguaggio e non librerie.
def flatten_list(elements: list) -> list:
    pass


# Test funzioni
print_test(sum_squares, [1, 2, 3])
print_test(max_element, [1, 2, 3, -1, -2])
print_test(max_element, [-1, -2])
print_test(max_element, [])
print_test(remove_duplicates, [1, 2, 3, 2, 3])
print_test(reverse_list, [1, 2, 3])
print_test(flatten_list, [1, [2, 3]])
print_test(flatten_list, [1, [2, [3, 4]]])
