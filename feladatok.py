import random

def feladat1():
    szam:int=int(input("Kérek egy páros számot!"))
    while szam%2!=0:
        szam:int=int(input("Ez nem páros! PÁROS számot kérek!"))
    print(szam)


def feladat2():
    lista=[]
    i=0
    while i<13:
        szam2:int=int(random.random()*(141)+10)
        lista.append(szam2)
        i+=1
    return lista

def feladat2_szamolas(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if(lista[i]%3==0):
            db+=1
        i+=1
    return db

def feladat3(text,N):
    i:int=0
    hossz:int=0
    if N>len(text):
       print("Nincs N karakter!")
    else:
        print(text[N-1].upper() * 3)

def feladat4():
    szov=[]
    s=szov
    szoveg:str=""
    while szoveg !="@":
        szoveg=input("Ajd meg egy nevet!(Kilépés a @-jellel!)")
        szov.append(szoveg)
        if szoveg!="@":
            print(szoveg)
    print(f"A használó {szov} adott meg!")
    
    
    


    



    