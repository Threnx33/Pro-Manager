from validari import valideaza_apartament,valideaza_nr,valideaza_tip,valideaza_val
from getters import get_tipuri,get_cheltuiala,get_tip,set_apartament,set_apa,set_canal,set_incalzire,set_gaz,set_altele

def get_creeaza_apartament(apa,canal,incalzire,gaz,altele):
    """
    functie care adauga apartament si ofera valori de fiecare tip
    date de intrare: apa - cheltuiala apa
                     canal - cheltuiala canal
                     incalzire - cheltuiala incalzire
                     gaz - cheltuiala gaz
                     altele - cheltuiala altele
    date de iesire: apartament - un apartament care are cheltuielile de sus
    """
    """
    return [apa,canal,incalzire,gaz,altele]
    """
    return {
        "apa":apa,
        "canal":canal,
        "incalzire":incalzire,
        "gaz":gaz,
        "altele":altele
    }

def adauga_apartament(apartamente,apa,canal,incalzire,gaz,altele):
    """
    functie care pe baza datelor unui apartament, creeaza un apartament nou si il adauga in lista mare de apartamente
    date de intrare:
        apartamente-lista de dictionare
        apa-intreg
        canal-intreg
        incalzire-intreg
        gaz-intreg
        altele-intreg
    date de iesire:-
    ridica exceptiile de tip Exception:
        (e11)-daca exista erori de validare a apartamentului
    """
    apartament = get_creeaza_apartament(apa,canal,incalzire,gaz,altele)
    valideaza_apartament(apartament)
    apartamente.append(apartament)

def set_cheltuiala(apartamente,nr,tip,val):
    """
    functie care modifica o cheltuiala pentru un apartament dat
    date de intrare: 
        apartamente-lista
        nr-numarul apartamentului
        tip-tipul existent de cheltuiala care trebuie modificat
        valoare-nr oferit tipului de cheltuiala > 0
    date de iesire:-
    erori: Exception
        (egen1,egen2,egen3)-daca exista erori de nr,tip sau val
    """
    valideaza_nr(apartamente,nr)
    valideaza_tip(tip)
    valideaza_val(val)
    if tip == "apa": set_apa(apartamente[nr],val)
    elif tip == "canal": set_canal(apartamente[nr],val)
    elif tip == "incalzire": set_incalzire(apartamente[nr],val)
    elif tip == "gaz": set_gaz(apartamente[nr],val)
    elif tip == "altele": set_altele(apartamente[nr],val)

def set_cheltuieli(apartamente,nr,apa,canal,incalzire,gaz,altele):
    """
    functie care modifica cheltuielile unui apartament intreg
    date de intrare:
        apartamente-lista de apartamente
        nr-numarul apartamentului
        apa-cheltuiala noua pt apa
        canal-cheltuiala noua pt canal
        incalzire-cheltuiala noua pt incalzire
        gaz-cheltuiala noua pt gaz
        altele-cheltuiala noua pt altele
    date de iesire:-
    erori: Exception
        (egen1,egen3)-daca exista erori de nr sau valori ale cheltuielilor
    """
    valideaza_nr(apartamente,nr)
    apartament = get_creeaza_apartament(apa,canal,incalzire,gaz,altele)
    valideaza_apartament(apartament)
    apartamente[nr] = apartament

def sterge_apartament(apartamente,nr):
    """
    functie care sterge un apartament din lista de apartamente
    date de intrare:
        apartamente-lista de apartamente
        nr-numarul apartamentului care trebuie sters
    date de iesire:-
    erori: Exception
        (egen1)-daca numarul nu este valid
    """
    valideaza_nr(apartamente,nr)
    del apartamente[nr]

def sterge_cheltuieli_apartament(apartamente,nr):
    """
    funtie care sterge toate cheltuielile de la apartamentul cu numarul "nr"
    date de intrare:
        apartamente-lista de apartamente
        nr-numarul apartamentului>=0
    date de iesire:-
    erori: Exception
        (egen1)-daca exista erori de nr
    """
    #set_cheltuiala(apartamente,nr,el,0)
    valideaza_nr(apartamente,nr)
    set_cheltuieli(apartamente,nr,0,0,0,0,0)
    
def sterge_cheltuieli_apartamente_consecutive(apartamente,nr):
    """
    functie care sterge cheltuielile de la apartamente consecutive numarului, adica vecinii sai si inclusiv el
    date de intrare:
        apartamente-lista de apartamente
        nr-numarul apartamentului caruia i se vor sterge vecinii>=0
    date de iesire:-
    erori: Exception
        (egen1)-daca exista erori de nr
    """
    #set_cheltuiala(apartamente,i,el,0) in foruri
    valideaza_nr(apartamente,nr)
    tipuri = get_tipuri()
    if nr == 0:
        for i in range(0,2):
            for el in tipuri:
                set_cheltuiala(apartamente,i,el,0)
    elif nr == len(apartamente)-1:
        for i in range(nr-1,nr+1):
            for el in tipuri:
                 set_cheltuiala(apartamente,i,el,0)
    else:
        for i in range(nr-1,nr+2):
            for el in tipuri:
                set_cheltuiala(apartamente,i,el,0)

def  sterge_tip_cheltuieli_apartamente(apartamente,tip):
    """
    funtcite care sterge cheltuielile de un anumit tip de la toate apartamente
    date de intrare:
        apartamente-lista de apartamente
        tip-tipul cheltuielii care va fi sters de la toate apartamentele
    date de iesire:-
    erori: Exception
        (egen2)
        "Tip de cheltuiala inexistent!\n"-daca tipul cheltuielii nu exista
    """
    valideaza_tip(tip)
    for i in range(0,len(apartamente)):
        set_cheltuiala(apartamente,i,tip,0)

def get_cauta_apartamente_mai_mari_ca_suma(apartamente,suma):
    """
    functie care returneaza toate apartamentele care au cheltuieli mai mari ca suma
    date de intrare:
        apartamente-lista de apartamente
        suma-suma citita
    date de iesire:
        cerinta-lista cu num arul apartamentelor mai mari ca suma
    erori:-
    """
    tipuri = get_tipuri()
    cerinta = []
    for i in range(0,len(apartamente)):
        ok = 0
        for el in tipuri:
            if get_cheltuiala(apartamente[i],el) > suma:
                ok = 1
        if ok == 1:
            cerinta.append(i)
    if len(cerinta) > 0:
        return cerinta
    else:
        return (f"Nu exista apartamente cu cheltuieli mai mari decat {suma}!\n")

def get_cauta_cheltuiala_tip_apartamente(apartamente,tip):
    """
    functie care returneaza cheltuielile de un anumit tip de la toate apartamentele
    date de intrare:
        apartamente-lista de apartamente
        tip-tip de cheltuiala
    date de iesire:
        cerinta-lista cu cheltuielile de un anumit tip de la toate apartamentele
    erori: Exception
        (egen2)
        "Tip de cheltuiala inexistent!\n"-daca tipul cheltuielii nu exista
    """
    valideaza_tip(tip)
    cerinta = []
    for i in range(0,len(apartamente)):
        cerinta.append(get_cheltuiala(apartamente[i],tip))
    if len(apartamente) > 0:
        return cerinta
    else:
        return ("Nu exista apartamente!\n")

def get_raport_suma_totala_tip_apartamente(apartamente,tip):
    """
    functie care returneaza suma totala a cheltuielilor de un anumit tip de la toate apartamentele
    date de intrare:
        apartamente-lista de apartamente
        tip-tip de cheltuiala
    date de iesire:
        cerinta-suma totala a cheltuielilor de un anumit tip de la toate apartamentele
    erori: Exception
        (egen2)
        "Tip de cheltuiala inexistent!\n"-daca tipul cheltuielii nu exista
    """
    valideaza_tip(tip)
    suma = 0
    for i in range(0,len(apartamente)):
        suma += get_cheltuiala(apartamente[i],tip)
    if len(apartamente) > 0:
        return suma
    else:
        return ("Nu exista apartamente!\n")

def get_raport_sortate_dupa_tip(apartamente,tip):
    """
    functie care returneaza toate apartamentele sortate dupa un tip de cheltuiala
    date de intrare:
        apartamente-lista de apartamente
        tip-tip de cheltuiala
    date de iesire:
        cerinta-lista apartamentelor ordonate in functie de un tip
    erori: Exception
        (egen2)
        "Tip de cheltuiala inexistent!\n"-daca tipul cheltuielii nu exista
    """
    valideaza_tip(tip)
    cerinta = [None] * len(apartamente)
    v = [None] * len(apartamente)
    for i in range(0,len(apartamente)):
        cerinta[i] = i
        v[i] = get_cheltuiala(apartamente[i],tip)
    
    i = 0
    while i < len(apartamente) - 1:
        j = i + 1
        while j < len(apartamente):
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
                aux = cerinta[i]
                cerinta[i] = cerinta[j]
                cerinta[j] = aux
            j += 1
        i += 1
    if len(apartamente) > 0:
        return cerinta
    else:
        return ("Nu exista apartamente!\n")

def get_raport_suma_apartament(apartamente,nr):
    """
    functie care returneaza suma cheltuielilor unui apartament
    date de intrare:
        apartament-lista de apartamente
        nr-numarul apartamentului
    date de iesire:
        cerinta-suma cheltuielilor unui apartament
    erori: Exception
        (egen1)
        "Numar de apartament invalid!\n"-daca numarul nu apartine intervalului [0,39]
    """
    valideaza_nr(apartamente,nr)
    tipuri = get_tipuri()
    suma = 0
    for el in tipuri:
        suma += get_cheltuiala(apartamente[nr],el)
    return suma

def get_filtru_elim_tip_apartamente(apartamente,tip):
    """
    functie care returneaza o lista de cheltuieli care exclude cheltuielile de un anumit tip
    date de intrare:
        apartamente-lista de apartamente
        tip-tipul cheltuielii
    date de iesire:
        cerinta-lista de dictionare de cheltuieli care exclude cheltuielile de un anumit tip
    erori: Exception
        (egen2)
        "Tip de cheltuiala inexistent!\n"-daca tipul cheltuielii nu exista
    """
    valideaza_tip(tip)
    tipuri = get_tipuri()
    cerinta = [None] * len(apartamente) 
    for i in range(0,len(apartamente)):
        cerinta[i] = "apartament "+str(i)+":"
        for el in tipuri:
            if el != tip:
                cerinta[i] += " "+str(el)+":"+str(get_cheltuiala(apartamente[i],el))
    return cerinta

def get_filtru_elim_cheltuieli_suma_apartamente(apartamente,suma):
    """
    functie care returneaza o lista de cheltuieli care exclude cheltuielile mai mici decat suma
    date de intrare:
        apartamente-lista de apartamente
        suma-val oferita
    date de iesire:
        cerinta-lista de cheltuieli care excludecheltuielile mai mici decat suma
    """
    tipuri = get_tipuri()
    cerinta = [None] * len(apartamente)
    for i in range(0,len(apartamente)):
        cerinta[i] = "apartament "+str(i)+":"
        for el in tipuri:
            if get_cheltuiala(apartamente[i],el) >= suma:
                cerinta[i] += " "+str(el)+":"+str(get_cheltuiala(apartamente[i],el))
    return cerinta

def undo(und,apartamente):
    """
    functie care se intoarce cu o comanda in urma, comenzile valide cu undo sunt:adaugare, stergere(deci intervalul [11,24])
    date de intrare:
        apartamente-lista de apartamente
        und-lista de undo
    date de iesire:-
    """
    if len(und) > 0:
        uc = und[len(und)-1]
        if uc[0] == "24":
            sterge_apartament(apartamente,len(apartamente)-1)
        elif uc[0] == "12.1":
            set_cheltuiala(apartamente,uc[1],uc[2],uc[3])
        elif uc[0] == "13":
            if len(uc) == 3:
                set_apartament(apartamente,uc[1],uc[2])
            else:
                if uc[1] == 0:
                    set_apartament(apartamente,0,uc[2])
                    set_apartament(apartamente,1,uc[3])
                elif uc[1] == len(apartamente)-1:
                    set_apartament(apartamente,uc[1]-1,uc[2])
                    set_apartament(apartamente,uc[1],uc[3])
                else:
                    set_apartament(apartamente,uc[1]-1,uc[2])
                    set_apartament(apartamente,uc[1],uc[3])
                    set_apartament(apartamente,uc[1]+1,uc[4])
        elif uc[0] == "12.2":
            for i in range(0, len(apartamente)):
                set_cheltuiala(apartamente,i,uc[1],uc[2+i])
        elif uc[0] == "mut":
            if uc[1] < len(apartamente)-1:
                apartamente.append(apartamente[len(apartamente)-1])
                for i in (len(apartamente)-1,uc[1],-1):
                    set_apartament(apartamente,i,apartamente[i-1])
            set_apartament(apartamente,uc[1],uc[2])
        del und[len(und)-1]