def Taqqoslash(x,y,z):
    """Kiritilgan uchta sondan eng kattasini qaytaruvchi funksiya"""
    if x>y:
        if x>z:
            return x
        else:
            return z
    elif y>x:
        if y>z:
            return y
        else:
            return z
    # return max(x, y, z)