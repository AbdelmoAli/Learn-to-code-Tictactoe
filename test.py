def check_for_errors(name_of_fun,L):
    boolean=False
    msg=""
    try:
        from dossier.func import name_of_fun as fun
        fun(*L)
        print("This function did not raise any error.")
        boolean=True
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
        msg= "Error of other type"
    print(boolean, msg) 
    return boolean, msg

check_for_errors("hmm",[])