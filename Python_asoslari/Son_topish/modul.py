from random import randint

def kompyuter(y):
    """Kompyuter o`ylaydigan son"""
    input(f"Keling son topish o`ynaymiz!\nMen 1 dan {y} gacha bo`lgan bir son o`yladim.")
    x = randint(1, y)
    sanoq = 1
    while True:
        savol = int(input("Topishga urinib ko`ring:\n>>>"))
        if savol == x:
            print(f"Qoyil men {x} sonini o'ylagan edim siz {sanoq} urinishda topdingiz")
            break
        elif savol > x:
            sanoq += 1
            print(f"Yo`q men o`ylagan son kichikroq")
        elif savol < x:
            sanoq += 1
            print(f"Yo`q men o`ylagan son kattaroq")
    return sanoq



def inson(x):
    """Inson o`ylaydigan son"""
    input(f"1 dan {x} gacha son o`ylang topishga urinib ko`raman.")
    sanoq = 1
    boshi = 1
    while True:
        y = randint(boshi, x)
        savol = input(f"Siz {y} ni o`yladingiz topdimmi? ha/yo`q men o`ylagan son kattaroq(+)/yo`q men o`ylagan son kichikroq(-)\n>>>")
        if savol == 'ha':
            print(f"Men siz o`ylagan sonni {sanoq} urinishda topdim")
            break
        elif savol == '+':
            sanoq += 1
            boshi = y+1
        elif savol == '-':
            sanoq += 1
            x = y-1
    return sanoq