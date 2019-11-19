import importlib

def check_for_errors(L):
    boolean = False
    msg=""
    try:
        #mymodule = importlib.import_module(".function_to_test", package = "submitted_files") #désigne le fichier où est stocké la 'réponse' temporaire
        import src.submitted_files.function_to_test
        importlib.reload(src.submitted_files.function_to_test)
        src.submitted_files.function_to_test.function(L)
        msg="This function did not raise any error."
        boolean = True
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
    #except :
     #   msg= "Error of other type"
    return boolean, msg

print(check_for_errors([3,4]))



