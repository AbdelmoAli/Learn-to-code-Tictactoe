def exercice2():
    str="txt goes here"
    def find_all():
        dico={}
        for c in str:
            if c in dico:
                dico[c]=dico[c]+1
            else:
                dico[c]=1
        return dico
    dico=find_all()
    L=[]
    for c in dico.keys():
        if dico[c]==1:
            L.append(c)
    print(L)

def exercice3():
    exo3="txt goes here"
    tempo=""
    for c in exo3:
        if c!="\n":
            tempo+=c
    exo3=tempo
    L=[]
    for c in exo3:
        if c.isupper():
            L.append(1)
        else:
            L.append(0)
    r=[]
    reponse=""
    for i in range(1,len(L)-6-1):
        if L[i]==L[i+1]==L[i+2]==L[i+4]==L[i+5]==L[i+6]==1 and L[i+3]==L[i-1]==L[i+7]==0:
            reponse=exo3[i:i+7]
            r.append(reponse)
            #if exo3[i]==exo3[i+4]:

    print(r)

import urllib.request

def exercice4(url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=",acc="93781"):
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    compt=1
    while compt<100:
        lire=urllib.request.urlopen(url+acc)
        string=lire.read()
        string=string.decode('utf-8')
        print(string)
        acc=""
        for c in string:
            if is_number(c):
                acc+=str(c)
        print(acc+"\n")
        compt+=1
        print(compt)

import pickle
def exercice5():
    path="C:\\Users\\HP\\Desktop\\banner.pkl"
    res=pickle.load(open(path,'rb'))
    acc=""
    for c in res:
        for i in c:
            acc+=(i[0]*i[1])
        print(acc)
def exercice5_correct_version():
    path="C:\\Users\\HP\\Desktop\\"
    res=pickle.load(open(path+"banner.pkl",'rb'))
    out=open(path+'lol.txt','w')
    print(res)
    for sublist in res:
        for subtuple in sublist:
            out.write((subtuple[0]*subtuple[1]))
        out.write('\n')
    out.close()

import zipfile
def exercice6():
    def ordre_exercice6(depart="90052"):
        acc=""
        L=[]
        compt=1
        while compt<909:
            compt+=1
            f=open(path+depart+".txt",'r')
            texte=f.read()
            for c in texte:
                if is_number(c):
                    acc+=str(c)
            L.append(acc)
            depart=acc
            acc=""
            f.close()
        return L
    def comment( L=ordre_exercice6() ):
        out=open("C:\\Users\\HP\\Desktop\\lol.txt", "w")
        archive = zipfile.ZipFile("C:\\Users\\HP\\Desktop\\channel.zip", 'r')
        liste_comments=[]
        for c in L:

            tempo=archive.getinfo(c+".txt").comment
            tempo=tempo.decode('utf-8')
            liste_comments.append( tempo )
            out.write(tempo)

        return liste_comments
    comment()

import numpy

def exercice7():
    path="C:\\Users\\HP\\Desktop\\oxygen.png"

    from PIL import Image
    img=Image.open(path)

    largeur, hauteur=img.size

    L=[img.getpixel((x,hauteur/2)) for x in range(largeur) ]

    L=[r for (r,g,b,a) in L]
    L=L[:-21]
    i=0
    tempo=[]
    while i<len(L):
        tempo.append(L[i])
        i+=7
    L=tempo

    L=[105, 110, 116, 101, 103, 114, 105, 116, 121]
    for i in range(len(L)):
        L[i]=chr(L[i])
    return L

import bz2
def exercice8():
    username=bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
    password=bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
    return username,password
#exercice9 sur internet
def exercice10(fin=30,num_debut="1"):
    def list_render(num):
        num=str(num)
        tempo=[]
        for c in num:
            tempo.append(int(c))
        return tempo
    def reader(num):
        i=1
        num=list_render(num)
        res=""
        for j in range(1,len(num)):
            if num[j]==num[j-1]:
                i+=1
            else:
                res+=str(i)+str(num[j-1])
                i=1
        return res+str(i)+str(num[-1])
    def boucle():
        res=num_debut
        L=[]
        for i in range(fin+1):
            L.append(len(res))
            res=reader(res)

        return L
    return boucle()

































