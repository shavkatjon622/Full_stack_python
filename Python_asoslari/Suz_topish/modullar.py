from uzwords import words
from random import choice


def random_words():
    """Lug`at ichidan qo`shma bo`lmagan so`zlarni qaytaruvchi funksiya"""
    toxta = True
    while toxta:
        soz = choice(words).lower()
        jadval = soz.split("-")
        if len(jadval) == 1 and len(jadval[0]) < 7:
            toxta = False
            return soz
        else:
            continue


def almashtirish(harflar, soz):
    """So`z bn harflarni olib bor yoki yo`qligini tekshiradigan funksiya"""
    sanoq = ""
    for harf in list(soz):
        if harf.lower() in harflar:
            sanoq += harf.upper()
        else:
            sanoq += "-"
    return sanoq


def play():
    """O`yinning asosiy qismi"""
    soz = random_words()  # yangi so`z olamiz
    soz_harflari = set(soz.lower())
    print(f"Men {len(soz)} harfdan iborat so`z o`yladim. Topishga urinib ko`ring!")
    print(almashtirish("", soz))  # tepada yozgan funksiyamizdan foydalanib soz harflarini - larga aylantiramiz
    harflar = []
    while len(soz_harflari):  # Harflar kiritilib o`ynaladigan asosiy qism
        yangi = input("\nBiror harf kiriting: ").lower()
        if yangi in harflar:  # foydalanuvchi avval kiritgani haqida ogohlantirish
            print(f"Siz avval {yangi} harfini kiritgansiz")
            continue
        harflar.append(yangi.lower())
        if harflar:  # foydalanuvchi kiritgan harflarni ko`rsatib turadi
            kiritilganlar = ""
            for harf in harflar:
                kiritilganlar += harf.upper()
            print(f"Hozirgacha kiritilgan harflar {kiritilganlar}")
        if yangi.lower() in soz_harflari:  # Foydalanuvchiga kerakli harfni topganini ko`rsatish
            soz_harflari.remove(yangi.lower())
            print(f"{yangi} harfi to`g`ri")
        print(almashtirish(harflar, soz))
        if len(soz_harflari) == 0:  # Foydalanuvchi o`yinni tamomlagach tabriklash.
            print(f"Tabriklaymiz! Siz {soz} so`zini {len(harflar)} urinishda topdingiz.\n")
