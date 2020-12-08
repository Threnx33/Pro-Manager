from functii import get_creeaza_apartament,adauga_apartament,set_cheltuiala,set_cheltuieli,sterge_apartament
from functii import sterge_cheltuieli_apartament,sterge_cheltuieli_apartamente_consecutive,sterge_tip_cheltuieli_apartamente
from functii import get_cauta_apartamente_mai_mari_ca_suma,get_cauta_cheltuiala_tip_apartamente
from functii import get_raport_suma_totala_tip_apartamente,get_raport_sortate_dupa_tip,get_raport_suma_apartament
from functii import get_filtru_elim_tip_apartamente,get_filtru_elim_cheltuieli_suma_apartamente,undo
from getters import get_cheltuiala
from validari import valideaza_apartament,valideaza_nr,valideaza_tip,valideaza_val

def ui_adauga_apartament(und,apartamente):
    print("Adauga un apartament nou")
    apa = int(input("Apa: "))
    canal = int(input("Canal: "))
    incalzire = int(input("Incalzire: "))
    gaz = int(input("Gaz: "))
    altele = int(input("Altele: "))
    valideaza_apartament(get_creeaza_apartament(apa,canal,incalzire,gaz,altele))
    und.append(["24"])
    adauga_apartament(apartamente,apa,canal,incalzire,gaz,altele)    

def ui_set_cheltuiala(und,apartamente):
    print("Set cheltuiala apartament")
    nr = int(input("Nr: "))
    valideaza_nr(apartamente,nr)
    tip = input("Tip: ")
    valideaza_tip(tip)
    val = int(input("Val: "))
    valideaza_val(val)
    und.append(["12.1",nr,tip,get_cheltuiala(apartamente[nr],tip)])
    set_cheltuiala(apartamente,nr,tip,val)
    
def ui_set_cheltuieli(und,apartamente):
    print("Set cheltuieli apartament")
    nr = int(input("Nr: "))
    apa = int(input("Apa: "))
    canal = int(input("Canal: "))
    incalzire = int(input("Incalzire: "))
    gaz = int(input("Gaz: "))
    altele = int(input("Altele: "))
    valideaza_apartament(get_creeaza_apartament(apa,canal,incalzire,gaz,altele))
    und.append(["13",nr,apartamente[nr]])
    set_cheltuieli(apartamente,nr,apa,canal,incalzire,gaz,altele)

def ui_sterge_apartament(und,apartamente):
    print("Sterge un apartament")
    nr = int(input("Nr: "))
    valideaza_nr(apartamente,nr)
    und.append(["mut",nr,apartamente[nr]])
    sterge_apartament(apartamente,nr)
    print("S-a sters apartamentul "+str(nr))

def ui_sterge_cheltuieli_apartament(und,apartamente):
    print("Sterge cheltuieli apartament")
    nr = int(input("Numar apartament: "))
    valideaza_nr(apartamente,nr)
    und.append(["13",nr,apartamente[nr]])
    sterge_cheltuieli_apartament(apartamente,nr)
    print("S-a sters cheltuielile apartamentului "+str(nr))

def ui_sterge_cheltuieli_apartamente_consecutive(und,apartamente):
    print("Sterge cheltuieli apartamente consecutive")
    nr = int(input("Numar apartament:"))
    valideaza_nr(apartamente,nr)
    und.append(["13",nr])
    if nr == 0:
        for i in range(0,2):
            und[len(und)-1].append(apartamente[i].copy())
        print("S-au sters cheltuielile apartamentelor "+str(nr-1)+","+str(nr))
    elif nr == len(apartamente)-1:
        for i in range(nr-1,nr+1):
            und[len(und)-1].append(apartamente[i].copy())
        print("S-au sters cheltuielile apartamentelor "+str(nr)+","+str(nr+1))
    else:
        for i in range(nr-1,nr+2):
            und[len(und)-1].append(apartamente[i].copy())
        print("S-au sters cheltuielile apartamentelor "+str(nr-1)+","+str(nr)+","+str(nr+1))
    sterge_cheltuieli_apartamente_consecutive(apartamente,nr)

def ui_sterge_tip_cheltuieli_apartamente(und,apartamente):
    print("Sterge cheltuieli de un anumit tip de la toate apartamentele")
    tip = input("Tipul cheltuielii: ")
    valideaza_tip(tip)
    und.append(["12.2",tip])
    for i in range(0,len(apartamente)):
        und[len(und)-1].append(get_cheltuiala(apartamente[i],tip))
    sterge_tip_cheltuieli_apartamente(apartamente,tip)
    print(f"S-au sters toate cheltuielile de tip {tip}")

def ui_get_tipar_apartamente_mai_mari_ca_suma(apartamente):
    print("Tipareste toate apartamentele care au cheltuieli mai mari ca o suma")
    suma = int(input("Suma: "))
    print("Lista: "+str(get_cauta_apartamente_mai_mari_ca_suma(apartamente,suma)))

def ui_get_cauta_cheltuiala_tip_apartamente(apartamente):
    print("Tipareste cheltuielile de un anumit tip de la toate apartamentele")
    tip = input("Tip: ")
    print("Lista: "+str(get_cauta_cheltuiala_tip_apartamente(apartamente,tip)))

def ui_get_raport_suma_totala_tip_apartamente(apartamente):
    print("Tipareste suma totala a cheltuielilor de un anumit tip de la toate apartamentele")
    tip = input("Tip: ")
    print(f"Suma este: {get_raport_suma_totala_tip_apartamente(apartamente,tip)}")
    
def ui_get_raport_sortate_dupa_tip(apartamente):
    print("Tipareste toate apartamentele sortate dupa un tip de cheltuiala")  
    tip = input("Tip: ")
    print(f"Ordinea este: {get_raport_sortate_dupa_tip(apartamente,tip)}")

def ui_get_raport_suma_apartament(apartamente):
    print("Tipareste suma cheltuielilor unui apartament")
    nr = int(input("Numar: "))
    print(f"Suma este: {get_raport_suma_apartament(apartamente,nr)}")

def ui_get_filtru_elim_tip_apartament(apartamente):
    print("Tipareste toate cheltuielile apartamentelor fara un anumit tip")
    tip = input("Tip: ")
    cerinta = get_filtru_elim_tip_apartamente(apartamente,tip)
    for el in cerinta:
        print(el)

def ui_get_filtru_elim_cheltuieli_suma_apartamente(apartamente):
    print("Tipareste toate cheltuielile apartamentelor mai mari egale cu suma")
    suma = int(input("Suma: "))
    cerinta = get_filtru_elim_cheltuieli_suma_apartamente(apartamente,suma)
    for el in cerinta:
        print(el)

def ui_undo(und,apartamente):
    print("Undo")
    undo(und,apartamente)
    print("S-a aplicat undo")

def ui_tipareste_apartamente(apartamente):
    if len(apartamente)==0:
        print("Nu ai apartamente")
    for el in range(0, len(apartamente)):
        print(f"Apartament {el}: {apartamente[el]}")

def ui_get_lista_comenzi():
    comenzi = {
        "02":ui_tipareste_apartamente,
        "11":ui_adauga_apartament,"12":ui_set_cheltuiala,"13":ui_set_cheltuieli,"24":ui_sterge_apartament,
        "21":ui_sterge_cheltuieli_apartament,"22":ui_sterge_cheltuieli_apartamente_consecutive,"23":ui_sterge_tip_cheltuieli_apartamente,
        "31":ui_get_tipar_apartamente_mai_mari_ca_suma,"32":ui_get_cauta_cheltuiala_tip_apartamente,
        "41":ui_get_raport_suma_totala_tip_apartamente,"42":ui_get_raport_sortate_dupa_tip,"43":ui_get_raport_suma_apartament,
        "51":ui_get_filtru_elim_tip_apartament,"52":ui_get_filtru_elim_cheltuieli_suma_apartamente,
        "61":ui_undo
    }
    return comenzi

def ui_afiseaza_comenzi():
    print("00:Iesire din program\n01:Afiseaza comenzile\n02:Afiseaza apartamentele")
    print("11:Adauga apartament\n12:Set cheltuiala\n13:Set cheltuieli")
    print("21:Sterge cheltuieli apartament\n22:Sterge cheltuieli apartamente consecutive\n23:Sterge tip cheltuieli apartamente\n24:Sterge un apartament")
    print("31:Tipareste apartamente cu cheltuieli mai mari ca suma\n32:Tipareste cheltuielile de un anumit tip de la toate apartamentele")
    print("41:Tipareste suma unui tip de cheltuiala\n42:Tipareste apartamentele sortate dupa un tip de cheltuiala\n43:Tipareste suma cheltuielilor unui apartament")
    print("51:Tipareste toate cheltuielile apartamentelor fara un anumit tip\n52:Tipareste toate cheltuielile apartamentelor mai mari egale cu suma")
    print("61:Undo")

def ui_run():
    comenzi = ui_get_lista_comenzi()
    ui_afiseaza_comenzi()
    apartamente = []
    und = []
    while True:
        cmd = input(">>>")
        if cmd == "00":
            print("Iesire program!")
            return
        elif cmd == "01":
            ui_afiseaza_comenzi()
        elif cmd in comenzi:
            try:
                if cmd == "11" or cmd == "12" or cmd == "13" or cmd == "21" or cmd == "22" or cmd == "23" or cmd == "24" or cmd == "61":
                    comenzi[cmd](und,apartamente)
                else:
                    comenzi[cmd](apartamente)                
            except ValueError:
                print("Valoare atribuita gresit!(ex:oferi valoare de tip string unui int)")
            except Exception as ex:
                print(str(ex))
            
                
        else:
            print ("Comanda invalida!")