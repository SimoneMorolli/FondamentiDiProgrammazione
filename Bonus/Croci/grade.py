# -*- coding: utf-8 -*-
import testlib
import isrecursive
from bintree import BinTree
import os

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    exit(0)
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################


def error_message(res, expected, msg=None):
    msg_std = f"Valore NON corretto! [NOT OK]\n TUO RISULTATO = {res} \n ma e' ATTESO = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print('*'*50)
    print(msg)



def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', "ERROR: Please assign the 'name' variable with YOUR NAME in program.py"
        assert program.surname    != 'SURNAME', "ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py"
        assert program.student_id != 'MATRICULATION NUMBER', "ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py"
    else:
        assert program.nome      != 'NOME', "ERRORE: Indica il tuo NOME in program.py"
        assert program.cognome   != 'COGNOME', "ERRORE: Indica il tuo COGNOME in program.py"
        assert program.matricola != 'MATRICOLA', "ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py"
    return 0, 0

###############################################################################



# ----------------------------------- EX.2 ----------------------------------- #
def do_ex2_tests(ID, expected, total=2):
    file_png = f"crosses/cross_{ID}.png"
    res = program.ex2(file_png)
    if res != expected:
        error_message(res, expected)
        for c, l in expected.items():
            assert sorted(l) == sorted(res[c])
        return 0, total
    return total, total


def test_ex2_1():
    r'''
    Trovate le croci su immagine crosses/cross_01.png
    '''
    ID = '01'
    expected = {(255, 255,   0): {((123, 516), (161, 516), (142, 497), (142, 535))},
                (255,   0, 255): {((129,  97), (383,  97), (256,  62), (256, 132))},
                (  0,   0, 255): {((140,  41), (390,  41), (265,  24), (265,  58))},
                (255,   0,   0): {((450, 310), (526, 310), (488, 217), (488, 403))}}
    return do_ex2_tests(ID, expected)

def test_ex2_2():
    r'''
    Trovate le croci su immagine crosses/cross_02.png
    '''

    ID = '02'
    expected = {(255, 255, 255): {((21, 266), (41, 266), (31, 162), (31, 370))},
                (0, 0, 255): {((25, 101), (49, 101), (37, 56), (37, 146)), ((36, 244), (108, 244), (72, 140), (72, 348))},
                (255, 0, 0): {((60, 64), (134, 64), (97, 34), (97, 94))},
                (255, 0, 255): {((127, 505), (213, 505), (170, 502), (170, 508))},
                (0, 255, 0): {((130, 394), (194, 394), (162, 356), (162, 432))},
                (0, 255, 255): {((140, 103), (222, 103), (181, 74), (181, 132))},
                (255, 255, 0): {((188, 294), (266, 294), (227, 281), (227, 307)), ((253, 209), (311, 209), (282, 147), (282, 271)), ((266, 127), (294, 127), (280, 105), (280, 149))}}
    return do_ex2_tests(ID, expected)

def test_ex2_3():
    r'''
    Trovate le croci su immagine crosses/cross_03.png
    '''

    ID = '03'
    expected = {(0, 255, 255): {((2, 44), (4, 44), (3, 28), (3, 60)), ((4, 18), (8, 18), (6, 15), (6, 21)), ((29, 178), (83, 178), (56, 174), (56, 182)), ((124, 15), (132, 15), (128, 10), (128, 20)), ((124, 83), (188, 83), (156, 75), (156, 91)), ((211, 94), (215, 94), (213, 86), (213, 102))},
                (255, 255, 0): {((13, 215), (27, 215), (20, 197), (20, 233)), ((22, 15), (28, 15), (25, 8), (25, 22)), ((100, 180), (168, 180), (134, 161), (134, 199)), ((173, 43), (183, 43), (178, 35), (178, 51))},
                (255, 0, 255): {((22, 64), (38, 64), (30, 44), (30, 84)), ((26, 210), (68, 210), (47, 208), (47, 212)), ((50, 122), (56, 122), (53, 74), (53, 170)), ((114, 66), (128, 66), (121, 61), (121, 71)), ((202, 60), (232, 60), (217, 52), (217, 68)), ((226, 162), (238, 162), (232, 127), (232, 197))},
                (255, 255, 255): {((25, 5), (73, 5), (49, 4), (49, 6)), ((68, 161), (102, 161), (85, 148), (85, 174)), ((98, 5), (180, 5), (139, 3), (139, 7)), ((121, 212), (173, 212), (147, 207), (147, 217)), ((145, 126), (193, 126), (169, 87), (169, 168))},
                (0, 255, 0): {((54, 187), (84, 187), (69, 182), (69, 195)), ((87, 223), (173, 223), (130, 217), (130, 229)), ((165, 25), (193, 25), (179, 18), (179, 32))},
                (0, 0, 255): {((201, 150), (221, 150), (211, 122), (211, 178))}}
    return do_ex2_tests(ID, expected, total=3)



################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex2_1,  test_ex2_2,  test_ex2_3,                               # find crosses
    test_personal_data_entry,
]

if __name__ == '__main__':
    testlib.runtests(tests, logfile='grade.csv')

################################################################################



