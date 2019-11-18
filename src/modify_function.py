def modify_function():
    fichier = open("src/submitted_files/file.py", 'r')
    function = fichier.readlines()
    for row in function:
        if row[::3] == 'def':
            i = row.index('(')
            return str(row[4::i])
    return 'test'

    
 
