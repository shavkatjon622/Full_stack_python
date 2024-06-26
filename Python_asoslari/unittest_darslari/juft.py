def Juft(sonli_royxat):
    """Sonli ro`yxat ichidan juft sonlarni ajratib beruvchi funksiya"""
    juft_sonlar = []
    for son in sonli_royxat:
        if son % 2 == 0:
            juft_sonlar.append(son)
    return juft_sonlar