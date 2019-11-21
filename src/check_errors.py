import importlib

output_of_7_entry=[ [ ['O','',''], ['','X',''], ['O','','O'], ['O','','O'], ['','X',''], ['','','O'], ['O','X','O'], ['','X','O'] ] ]

test_entries = {'1': [[]],
                '2':[ [ [['O','',''],['','X',''],['','','']] , 0, 0] , [ [['O','',''],['','X',''],['','','']] , 0, 1]],
                '3':[ [ [['O','',''], ['','X',''], ['','','O']], 0, 1], [ [['O','O',''],['','X',''],['','','O']], 0, 1] ],
                '4':[ [ [['O','',''], ['','X',''], ['','','O']], 0, 0,'X'] , [ [['O','',''], ['','X',''], ['','','O']], 0, 1,'X'] ],
                '5':[ ['X'], ['O'] ],
                '6':[ [ ['X','X','X'] ] , [ ['X','O','X'] ] ],
                '7':[ [ [['O','',''],['','X',''],['O','','O']] ] ],
                '8':[ [ [['O','',''],['O','X',''],['','X','O']] ], [ [['O','',''],['O','X',''],['O','0','O']] ] ],
                '9':[ [ [['O','',''],['O','X',''],['O','0','O']] ], [ [['O','',''],['O','X',''],['X','X','X']] ] ],
                '10':[ [ [['O','X','O'],['X','O','O'],['O','X','O']] ], [ [['O','X','O'],['X','O','O'],['O','','O']] ] ]}

test_example_output = { '1': [ [['' ,'' ,''], ['' ,'' ,''], ['' ,'' ,'']] ], 
                        '2': ['O', ''],
                        '3': [True, False],
                        '4': [ (False,[['O','',''], ['','X',''], ['','','O']]) , (True,[['O','X',''], ['','X',''], ['','','O']]) ],
                        '5': ['O', 'X'],
                        '6': [True, False],
                        '7': output_of_7_entry,
                        '8': [False, True],
                        '9': ['O','X'],
                        '10': [True, False]
                        }

def check_for_errors(key):
    boolean = False
    msg=""
    try:
        #mymodule = importlib.import_module(".function_to_test", package = "submitted_files") #désigne le fichier où est stocké la 'réponse' temporaire
        import src.function_to_test.function_to_test
        importlib.reload(src.function_to_test.function_to_test)
        msg="This function did not raise any error."
        if key=='7':
            entries = test_entries[key]
            expected_outputs = test_example_output[key]
            boolean = True
            def sort(L):
                for i in range(len(L)):
                    L[i]=sorted(L[i])
                return sorted(L)
            for (i,entry) in enumerate(entries):
                if not sort(src.function_to_test.function_to_test.function(entry)) == sort(expected_outputs[i]):
                    boolean = False
                    break
        else:
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
        boolean = False
    except IndentationError:
        msg = "There is an error in your indentation."
        boolean = False
    except SyntaxError:
        msg = "There is a syntax error."
        boolean = False
    except AttributeError:
        msg = "You made an invalid attribute reference or an attribute assignement failed."
        boolean = False
    except IndexError:
        msg = "There is a problem with the indexing."
        boolean = False
    except MemoryError:
        msg = "Some operation is taking too much memory. We invite you to check the loops (to avoid endless loop)."
        boolean = False
    except TypeError:
        msg = "You are applying some function or operator to a type it's not supposed to support."
        boolean = False
    except:
        msg = "There is an error of some other type."
        boolean = False
    return boolean, msg




