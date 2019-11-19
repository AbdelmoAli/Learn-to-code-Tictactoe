def read_and_modify_function(fichier):
    fichier=fichier.split('\n')
    name=""
    L=[]
    for row in fichier:
        if row[:3] == 'def':
            i = row.index('(')
            name=str(row[4:i])
            L.append(row+'\n')
        else:
            L.append("\t"+row+'\n')
    return "".join(L), name

