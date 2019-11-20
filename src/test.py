import importlib

test_entries = {'1': [],'2':[['O','',''],['','X',''],['','','O']],'3':([['O','',''],['','X',''],['','','O']],1,1,'X'),'4':'O','5':([['O','',''],['','X',''],['O','','O']],2,0)
,'6':['X','X','X'],'7':[['O','',''],['','X',''],['O','','O']],'8':[['O','',''],['O','X',''],['O','X','O']],'9':[['O','',''],['O','X',''],['O','X','O']],
'10':[['O','X','O'],['X','O','O'],['O','X','O']]}
test_example_input = { '1': [], '2':[] }
test_example_output = { '1': [], '2':[] }

def check_for_errors(key):
    boolean = False
    msg_error=""
    msg_example=""
    try:
        #mymodule = importlib.import_module(".function_to_test", package = "submitted_files") #désigne le fichier où est stocké la 'réponse' temporaire
        import src.function_to_test.function_to_test
        importlib.reload(src.function_to_test.function_to_test)
        entry = test_entries[key]
        src.function_to_test.function_to_test.function(entry)
        msg_error="This function did not raise any error."
        boolean = True
    except NameError:
        msg_error = "You are using an undefined object."
    except IndentationError:
        msg_error = "There is an error in your indentation."
    except SyntaxError:
        msg_error = "There is a syntax error."
    except AttributeError:
        msg_error = "You made an invalid attribute reference or an attribute assignement failed."
    except IndexError:
        msg_error = "There is a problem with the indexing."
    except MemoryError:
        msg_error = "Some operation is taking too much memory. We invite you to check the loops (to avoid endless loop)."
    except TypeError:
        msg_error = "You are applying some function or operator to a type it's not supposed to support."
    except :
        msg_error = "Error of other type"
    if boolean:
        input = test_example_input[key]
        output = test_example_output[key]
        boolean = (output==function(input))
        if not boolean: 
            msg_example = "This function is incorrect."
    msg=msg_error+msg_example
    return boolean, msg




