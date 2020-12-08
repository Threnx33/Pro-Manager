from functii import get_creeaza_apartament,adauga_apartament,set_cheltuiala,set_cheltuieli,sterge_apartament
from functii import sterge_cheltuieli_apartament,sterge_cheltuieli_apartamente_consecutive,sterge_tip_cheltuieli_apartamente
from functii import get_cauta_apartamente_mai_mari_ca_suma,get_cauta_cheltuiala_tip_apartamente
from functii import get_raport_suma_totala_tip_apartamente,get_raport_sortate_dupa_tip,get_raport_suma_apartament
from functii import get_filtru_elim_tip_apartamente,get_filtru_elim_cheltuieli_suma_apartamente,undo
from getters import get_apa,get_canal,get_incalzire,get_gaz,get_altele
from getters import get_tip_apa,get_tip_canal,get_tip_incalzire,get_tip_gaz,get_tip_altele,get_tipuri,get_tip
from getters import get_cheltuiala
from validari import valideaza_apartament,valideaza_nr

def run_all_tests():
    test_get_creeaza_apartament()
    test_set_cheltuiala()
    test_set_cheltuieli()
    test_adauga_apartament()
    test_sterge_apartament()
    test_sterge_cheltuieli_apartament()
    test_sterge_cheltuieli_apartamente_consecutive()
    test_sterge_tip_cheltuieli_apartament()
    test_get_cauta_apartamente_mai_mari_ca_suma()
    test_get_cauta_cheltuiala_tip_apartamente()
    test_get_raport_suma_totala_tip_apartamente()
    test_get_raport_sortate_dupa_tip()
    test_get_raport_suma_apartament()
    test_get_filtru_elim_tip_apartamente()
    test_get_filtru_elim_cheltuieli_suma_apartamente()
    test_undo()

def get_exemplu_apartamente():
    """
    functie care creeaza un exemplu detaliat de apartamente
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = []
    p = 100
    for i in range(0,10):
        adauga_apartament(apartamente,i*p,i*p+1,i*p+2,i*p+3,i*p+4)
    return apartamente

def test_get_creeaza_apartament():
    apartament = get_creeaza_apartament(300,200,100,0,400.5)
    assert abs(get_apa(apartament)-300)<0.0001
    assert abs(get_canal(apartament)-200)<0.0001
    assert abs(get_incalzire(apartament)-100)<0.0001
    assert abs(get_gaz(apartament)-0)<0.0001
    assert abs(get_altele(apartament)-400.5)<0.0001

def test_set_cheltuiala():
    apartamente = []
    adauga_apartament(apartamente,300,200,100,0,400.5)
    set_cheltuiala(apartamente,0,"canal",500)
    assert abs(get_canal(apartamente[0])-500)<0.001
    try:
        set_cheltuiala(apartamente,0,"incalzire",-20)
        assert False
    except Exception as ex:
        assert str(ex)=="Valoare incorecta!\n"
    try:
        set_cheltuiala(apartamente,0,"canak",100)
        assert False
    except Exception as ex:
        assert str(ex)=="Tip de cheltuiala inexistent!\n"  

def test_set_cheltuieli():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartament[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    set_cheltuieli(apartamente,1,300,200,500,100,1.5)
    assert abs(get_apa(apartamente[1])-300)<0.001
    assert abs(get_canal(apartamente[1])-200)<0.001
    assert abs(get_incalzire(apartamente[1])-500)<0.001
    assert abs(get_gaz(apartamente[1])-100)<0.001
    assert abs(get_altele(apartamente[1])-1.5)<0.001
    try:
        set_cheltuieli(apartamente,-1,2,2,2,2,2)
        assert False
    except Exception as ex:
        assert str(ex) == "Numar de apartament invalid!\n"
    try:
        set_cheltuieli(apartamente,2,3,2,1000000000,-2,0)
        assert False
    except Exception as ex:
        assert str(ex) == "Gaz invalid!\n"
    assert abs(get_apa(apartamente[2])-200)<0.001

def test_adauga_apartament():
    apartamente=[]
    adauga_apartament(apartamente,100,100,100,100,100)
    assert len(apartamente)==1
    try:
        adauga_apartament(apartamente,0,0,0,0,-1)
        assert False
    except Exception as ex:
        assert str(ex)=="Altele invalide!\n"
    assert len(apartamente)==1
    adauga_apartament(apartamente,200,200,200,200,200)
    assert len(apartamente)==2

def test_sterge_apartament():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartament[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    assert abs(get_cheltuiala(apartamente[2],"apa")-200)<0.001
    assert len(apartamente) == 10
    sterge_apartament(apartamente,2)
    assert abs(get_cheltuiala(apartamente[2],"apa")-300)<0.001
    assert len(apartamente) == 9
    try:
        sterge_apartament(apartamente,9)
        assert False
    except Exception as ex:
        assert str(ex)=="Numar de apartament invalid!\n"
    

def test_sterge_cheltuieli_apartament():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartament[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    sterge_cheltuieli_apartament(apartamente,1)
    tipuri = get_tipuri()
    for el in tipuri:
        assert get_cheltuiala(apartamente[1],el)==0
    try:
        sterge_cheltuieli_apartament(apartamente,10)
        assert False
    except Exception as ex:
        assert str(ex)=="Numar de apartament invalid!\n"

def test_sterge_cheltuieli_apartamente_consecutive():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    tipuri = get_tipuri()
    apartamente = get_exemplu_apartamente()
    sterge_cheltuieli_apartamente_consecutive(apartamente,0)
    for i in range(0,1):
        for el in tipuri:
            assert get_cheltuiala(apartamente[i],el)==0
    sterge_cheltuieli_apartamente_consecutive(apartamente,5)
    for i in range(4,7):
        for el in tipuri:
            assert get_cheltuiala(apartamente[i],el)==0
    sterge_cheltuieli_apartamente_consecutive(apartamente,9)
    for i in range(8,10):
        for el in tipuri:
            assert get_cheltuiala(apartamente[i],el)==0
    try:
        sterge_cheltuieli_apartamente_consecutive(apartamente,10)
        assert False
    except Exception as ex:
        assert str(ex)=="Numar de apartament invalid!\n"

def test_sterge_tip_cheltuieli_apartament():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    sterge_tip_cheltuieli_apartamente(apartamente,"incalzire")
    for el in apartamente:
        assert el[get_tip_incalzire()]==0
    try:
        sterge_tip_cheltuieli_apartamente(apartamente,"gazz")
        assert False
    except Exception as ex:
        assert str(ex)=="Tip de cheltuiala inexistent!\n"

def test_get_cauta_apartamente_mai_mari_ca_suma():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    assert get_cauta_apartamente_mai_mari_ca_suma(apartamente,500) == [5,6,7,8,9]
    assert get_cauta_apartamente_mai_mari_ca_suma(apartamente,903) == [9]
    assert get_cauta_apartamente_mai_mari_ca_suma(apartamente,904) == "Nu exista apartamente cu cheltuieli mai mari decat 904!\n"
    assert get_cauta_apartamente_mai_mari_ca_suma(apartamente,-1) == [0,1,2,3,4,5,6,7,8,9]

def test_get_cauta_cheltuiala_tip_apartamente():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    assert get_cauta_cheltuiala_tip_apartamente(apartamente,"altele") == [4,104,204,304,404,504,604,704,804,904]
    try:
        get_cauta_cheltuiala_tip_apartamente(apartamente,"canak")
        assert False
    except Exception as ex:
        assert str(ex) == "Tip de cheltuiala inexistent!\n"
    apartamente = []
    assert get_cauta_cheltuiala_tip_apartamente(apartamente,"apa") == "Nu exista apartamente!\n"

def test_get_raport_suma_totala_tip_apartamente():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    assert get_raport_suma_totala_tip_apartamente(apartamente,"canal") == 4510
    try:
        get_raport_suma_totala_tip_apartamente(apartamente,"canak")
        assert False
    except Exception as ex:
        assert str(ex) == "Tip de cheltuiala inexistent!\n"
    apartamente = []
    assert get_cauta_cheltuiala_tip_apartamente(apartamente,"apa") == "Nu exista apartamente!\n"

def test_get_raport_sortate_dupa_tip():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    assert get_raport_sortate_dupa_tip(apartamente,"canal") == [0,1,2,3,4,5,6,7,8,9]
    try:
        get_raport_sortate_dupa_tip(apartamente,"canak")
        assert False
    except Exception as ex:
        assert str(ex) == "Tip de cheltuiala inexistent!\n"
    apartamente3 = []
    assert get_raport_sortate_dupa_tip(apartamente3,"altele") == "Nu exista apartamente!\n"
    

def test_get_raport_suma_apartament():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    assert get_raport_suma_apartament(apartamente,0) == 10
    assert get_raport_suma_apartament(apartamente,1) == 510
    try:
        get_raport_suma_apartament(apartamente,10)
        assert False
    except Exception as ex:
        assert str(ex) == "Numar de apartament invalid!\n"
    

def test_get_filtru_elim_tip_apartamente():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    cerinta = get_filtru_elim_tip_apartamente(apartamente,"canal")
    for i in range(0,10):
        assert cerinta[i] == ("apartament "+str(i)+": apa:"+str(get_apa(apartamente[i]))+
            " incalzire:"+str(get_incalzire(apartamente[i]))+" gaz:"+str(get_gaz(apartamente[i]))+
            " altele:"+str(get_altele(apartamente[i])))
    
def test_get_filtru_elim_cheltuieli_suma_apartamente():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    apartamente = get_exemplu_apartamente()
    cerinta = get_filtru_elim_cheltuieli_suma_apartamente(apartamente,501)
    for i in range(0,5):
        assert cerinta[i] == "apartament "+str(i)+":"
    assert cerinta[5] == "apartament 5: canal:501 incalzire:502 gaz:503 altele:504"
    for i in range(6,10):
        assert cerinta[i] == ("apartament "+str(i)+": apa:"+str(get_apa(apartamente[i]))+" canal:"+str(get_canal(apartamente[i]))+
            " incalzire:"+str(get_incalzire(apartamente[i]))+" gaz:"+str(get_gaz(apartamente[i]))+
            " altele:"+str(get_altele(apartamente[i])))
            
def test_undo():
    """
    apartamente[0]={0,1,2,3,4}
    apartamente[1]={100,101,102,103,104}
    apartamente[2]={200,201,202,203,204}
    ...
    apartamente[9]={900,901,902,903,904}
    """
    und = []
    tipuri = get_tipuri()
    for i in range(0,10):
        und.append(["24"])
    apartamente = get_exemplu_apartamente()
    undo(und,apartamente)
    assert len(und) == 9
    assert len(apartamente) == 9

    und.append(["12.1",1,"apa",100])
    set_cheltuiala(apartamente,1,"apa",50)
    undo(und,apartamente)
    assert abs(get_apa(apartamente[1])-100)<0.001

    und.append(["13",3,apartamente[3]])
    set_cheltuieli(apartamente,3,9,9,9,9,9)
    undo(und,apartamente)
    i = 300
    j = 0
    for el in tipuri:
        assert get_cheltuiala(apartamente[3],el) == i + j
        j +=1

    und.append(["13",5,apartamente[5]])
    sterge_cheltuieli_apartament(apartamente,5)
    undo(und,apartamente)
    i = 500
    j = 0 
    for el in tipuri:
        assert abs(get_cheltuiala(apartamente[5],el)-(i + j))<0.001
        j +=1
    ap1 = apartamente[1].copy()
    ap2 = apartamente[2].copy()
    ap3 = apartamente[3].copy()
    und.append(["13",2,ap1,ap2,ap3])
    sterge_cheltuieli_apartamente_consecutive(apartamente,2)
    undo(und,apartamente)
    i = 100
    for ind in range(1,4):
        j = 0
        for el in tipuri:
            assert abs(get_cheltuiala(apartamente[ind],el)-(i+j))<0.001
            j += 1
        i += 100

    und.append(["12.2","gaz",3,103,203,303,403,503,603,703,803])
    sterge_tip_cheltuieli_apartamente(apartamente,"gaz")
    undo(und,apartamente)
    i = 3
    for ind in range(0,len(apartamente)):
        assert abs(get_gaz(apartamente[ind]))-i<0.001
        i += 100

    und.append(["mut",2,apartamente[2]])
    sterge_apartament(apartamente,2)
    undo(und,apartamente)
    assert len(apartamente) == 9
    i = 0
    j = 0
    for ind in range(0,len(apartamente)):
        for el in tipuri:
            abs(get_cheltuiala(apartamente[ind],el)-(i + j))<0.001
            j += 1
        i += 100