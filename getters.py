def get_apa(apartament):
    """
    return apartament[0]
    """
    return apartament["apa"]

def get_canal(apartament):
    """
    return apartament[1]
    """
    return apartament["canal"]

def get_incalzire(apartament):
    """
    return apartament[2]
    """
    return apartament["incalzire"]

def get_gaz(apartament):
    """
    return apartament[3]
    """
    return apartament["gaz"]

def get_altele(apartament):
    """
    return apartament[4]
    """
    return apartament["altele"]

def get_cheltuiala(apartament,tip):
    if tip == "apa": return get_apa(apartament)
    elif tip == "canal": return get_canal(apartament)
    elif tip == "incalzire": return get_incalzire(apartament)
    elif tip == "gaz": return get_gaz(apartament)
    elif tip == "altele": return get_altele(apartament)

def get_tip_apa():
    """
    return 0
    """
    return "apa"

def get_tip_canal():
    """
    return 1
    """
    return "canal"

def get_tip_incalzire():
    """
    return 2
    """
    return "incalzire"

def get_tip_gaz():
    """
    return 3
    """
    return "gaz"

def get_tip_altele():
    """
    return 4
    """
    return "altele"

def get_tip(tip):
    if tip == "apa": return get_tip_apa()
    elif tip == "canal": return get_tip_canal()
    elif tip == "incalzire": return get_tip_incalzire()
    elif tip == "gaz": return get_tip_gaz()
    elif tip == "altele": return get_tip_altele()

def get_tipuri():
    return ["apa","canal","incalzire","gaz","altele"]

def set_apartament(apartamente,nr,apartament2):
    """
    functie care seteaza un apartament1 cu valoarea lui apartament2
    date de intrare:
        apartament1-apartamentul care preia valoarea
        apartament2-apartamentul care ofera valoarea
    date de iesire:-
    """
    apartamente[nr] = apartament2

def set_apa(apartament,val):
    """
    apartament[0] = val
    """
    apartament["apa"] = val

def set_canal(apartament,val):
    """
    apartamente[1] = val
    """
    apartament["canal"] = val

def set_incalzire(apartament,val):
    """
    apartamente[2] = val
    """
    apartament["incalzire"] = val

def set_gaz(apartament,val):
    """
    apartamente[3] = val
    """
    apartament["gaz"] = val

def set_altele(apartament,val):
    """
    apartamente[4] = val
    """
    apartament["altele"] = val

