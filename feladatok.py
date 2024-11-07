def feladat1():
    szam:int=int(input("Kérek egy páros számot!"))
    while szam%2!=0:
        szam:int=int(input("Kérek egy páros számot!"))
    print(szam)