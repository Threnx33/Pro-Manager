from getters import get_apa,get_canal,get_incalzire,get_gaz,get_altele

def valideaza_apartament(apartament):
    """
    funtie care verifica daca apartamentul are apa,canal,incalzire,gaz,altele>0
    date de intrare: apartament - un apartament
    date de iesire:-
    ridica exceptie de tip Exception cu mesajul:
        (e11)
        -"Apa invalida!\n"      - daca apa<0
        -"Canal invalid!\n"     - daca canal<0
        -"Incalzire invalida!\n"- daca incalzire<0
        -"Gaz invalid!\n"       - daca gaz<0
        -"Altele invalide!\n"   - daca altele<0
    """
    er=""
    if get_apa(apartament)<0:
        er += "Apa invalida!\n"
    if get_canal(apartament)<0:
        er += "Canal invalid!\n"
    if get_incalzire(apartament)<0:
        er += "Incalzire invalida!\n"
    if get_gaz(apartament)<0:
        er += "Gaz invalid!\n"
    if get_altele(apartament)<0:
        er += "Altele invalide!\n"
    if len(er) > 0:
        raise Exception(er)

def valideaza_nr(apartamente,nr):
    """
    ridica o exceptie de tip Exception cu mesajul:
        (egen1)
        "Numar de apartament invalid!\n"-daca numarul nu apartine intervalului [0,39]
    """
    if nr < 0 or nr > 39 or nr > len(apartamente) - 1:
        raise Exception("Numar de apartament invalid!\n")

def valideaza_tip(tip):
    """
    ridica exceptie de tip Exception cu mesajul:
        (egen2)
        "Tip de cheltuiala inexistent!\n"-daca tipul cheltuielii nu exista
    """
    """
    if isinstance(tip,int) and (tip < 0 or tip > 4):
        raise Exception("Tip de cheltuiala inexistent!\n")
    """
    if tip != "apa" and tip != "canal" and tip != "incalzire" and tip != "gaz" and tip != "altele":
        raise Exception("Tip de cheltuiala inexistent!\n")

def valideaza_val(val):
    """
    ridica exceptie de tip Exception cu mesajul:
        (egen3)
        "Valoare incorecta!\n'- daca val < 0
    """
    if val < 0:
        raise Exception("Valoare incorecta!\n")
