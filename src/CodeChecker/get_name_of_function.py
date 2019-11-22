def get_name_of_function(file):
    
    '''
    Takes a function as parameter
    Returns the well indented function, and its name
    '''

    new_file = file.split('\n')
    name=""
    L=[]
    for row in new_file:
        if row[:3] == 'def':
            try:
                i = row.index('(')
            except:
                L=[file]
                name = ""
                break
            name = str(row[4:i])
            L.append(row+'\n')
        else:
            L.append("\t"+row+'\n')
    return "".join(L), name

