import importlib

test_entries = {'1': [[]],
                '2':[ [ [['O','',''],['','X',''],['','','']] , 0, 0] , [ [['O','',''],['','X',''],['','','']] , 0, 1]],
                '3':[ [ [['O','',''], ['','X',''], ['','','O']], 0, 1,'X'], [ [['O','O',''],['','X',''],['','','O']], 0, 1, 'X'] ],
                '4':'O','5':([['O','',''],['','X',''],['O','','O']],2,0)
,'6':['X','X','X'],'7':[['O','',''],['','X',''],['O','','O']],'8':[['O','',''],['O','X',''],['O','X','O']],'9':[['O','',''],['O','X',''],['O','X','O']],
'10':[['O','X','O'],['X','O','O'],['O','X','O']]}
test_example_output = { '1': [ [['' ,'' ,''], ['' ,'' ,''], ['' ,'' ,'']] ], 
                        '2': [False, True],
                        '3': [(True, [['O','X',''], ['','X',''], ['','','O']]), (False, [['O','O',''],['','X',''],['','','O']]) ],
                        }

def check_for_errors(key):
    boolean = False
    msg=""
    try:
        #mymodule = importlib.import_module(".function_to_test", package = "submitted_files") #désigne le fichier où est stocké la 'réponse' temporaire
        import src.function_to_test.function_to_test
        importlib.reload(src.function_to_test.function_to_test)
        msg="This function did not raise any error."
        entries = test_entries[key]
        expected_outputs = test_example_output[key]
        boolean = True
        for (i,entry) in enumerate(entries):
            if not src.function_to_test.function_to_test.function(entry) == expected_outputs[i]:
                boolean = False
                break 

        if not boolean: 
            msg+= "\nThis function is incorrect."
        else:
            msg+= "\nThis function serves it's purpose. You can proceed to the next level"
    except NameError:
        msg = "You are using an undefined object."
    except IndentationError:
        msg = "There is an error in your indentation."
    except SyntaxError:
        msg = "There is a syntax error."
    except AttributeError:
        msg = "You made an invalid attribute reference or an attribute assignement failed."
    except IndexError:
        msg = "There is a problem with the indexing."
    except MemoryError:
        msg = "Some operation is taking too much memory. We invite you to check the loops (to avoid endless loop)."
    except TypeError:
        msg = "You are applying some function or operator to a type it's not supposed to support."
    except:
        msg = "There is an error of some other type."
    return boolean, msg




