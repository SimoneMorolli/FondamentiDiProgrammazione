# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
#DEBUG = True
DEBUG = False
#############################################################################

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
    return 0

###############################################################################



# ----------------------------------- EX.2 ----------------------------------- #
def do_test_ex2(ID, expected, bg, color, H, W, step, score=3):
    p = 0
    img_out = f'ex2/ex2_your_image_{ID}.png'
    img_exp = f'ex2/ex2_expected_{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run
    res = program.ex2(H, bg, color, step, img_out)
    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The number of pixel different than background should be {expected} instead of {res}.\n'''
              f'''[ERROR] Il numero di pixel diversi dallo sfondo e' {expected} invece che {res}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return score
    



def test_ex2_1():
    '''imm_out = ex2/ex2_expected_A.png
    expected = 60'''
    ID = 'A'
    expected = 60
    bg, color, H, W, step = (0, 0, 0), (255, 0, 255), 10, 10, 2
    return do_test_ex2(ID, expected, bg, color, H, W, step, score=2)


def test_ex2_2():
    '''imm_out = ex2/ex2_expected_B.png
    expected = 120'''
    ID = 'B'
    expected = 120
    bg, color, H, W, step = (128, 128, 128), (0, 255, 255), 11, 11, 1
    return do_test_ex2(ID, expected, bg, color, H, W, step)

def test_ex2_3():
    '''imm_out = ex2/ex2_expected_C.png
    expected = 1848'''
    ID = 'C'
    expected = 1848
    bg, color, H, W, step = (128, 128, 128), (255, 255, 0), 127, 127, 10
    return do_test_ex2(ID, expected, bg, color, H, W, step)




################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_ex2_1,  test_ex2_2, test_ex2_3,             # disegna quadrati conc.
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
################################################################################
