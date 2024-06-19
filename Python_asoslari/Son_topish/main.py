from modul import kompyuter, inson

while True:
    komp = kompyuter(10)
    input(f"Endi sizni navbatingiz!")
    odam = inson(10)
    if komp == odam:
        print(f"Ikkimiz ham {odam} urinishda topdik. Natija durrang")
    elif komp > odam:
        print(f"Men {odam} urinishda topdim va yutdim.")
    elif komp < odam:
        print(f"Tabriklayman. Siz {komp} urinishda topdingiz va g`olib bo`ldingiz.")
    oxiri = input("Yana o`ynaysizmi?(ha/yoq)\n>>>")
    if oxiri == "ha":
        continue
    elif oxiri == "yoq":
        break