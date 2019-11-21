from check_errors import *
from get_name_of_function import *

from os.path import exists
from os import remove

def test_check_errors1():
    valid_function = 'def new_grid():\n\treturn [['' for i in range(3)] for j in range(3)]'


    user_code, name = get_name_of_function(valid_function)

    with open("src/function_to_test/function_to_test.py", "w") as fichier:
        fichier.write('def function(L):\n' +  '\t' + user_code + '\treturn (' + name + '(*L))' )

    assert check_for_errors('1') == (True, "This function did not raise any error.\nThis function serves it's purpose. You can proceed to the next level")

    path = "src/function_to_test/function_to_test.py"
    remove(path)

def test_check_errors2():
    invalid_function = 'def new_grid(a):\n\treturn [['' for i in range(3)] for j in range(3)]'

    user_code, name = get_name_of_function(invalid_function)

    with open("src/function_to_test/function_to_test.py", "w") as fichier:
        fichier.write('def function(L):\n' +  '\t' + user_code + '\treturn (' + name + '(*L))' )

    assert check_for_errors('1') == (False, "You are applying some function or operator to a type it's not supposed to support.")

    path = "src/function_to_test/function_to_test.py"
    remove(path)


    