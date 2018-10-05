from random import choice

mezo_darab = 0
mezo_forma = "negyzet"
mezo_forma_lehetosegek = {0:"negyszog",
                            1:"haromszog",
                            2:"hatszog",
                            3:"nyolcszog",
                            4:"kor",
                            5:"konkav"}


"""
Ebben a dokumentumban definialom a mezo neheziteseket: MN.

1. Darabszam: mezok szama
2. Forma: mezok formaja
3. Elhyezes: mezok elhelyezese
4. Viselkedes: mezok viselkedese
5. Meretek: mezok meretei
6. Kulalak: mezok kulalakja

"""


def MN_darabszam(jatekszint=0):
    global mezo_darab
    if jatekszint < 1:
        mezo_darab = choice(range(1, 5))
    elif jatekszint == 1:
        mezo_darab = choice(range(4, 11))
    elif 2 <= jatekszint:
        mezo_darab = choice(range(10, 41))
    else:
        print("Nothing happens.")
    return mezo_darab

def MN_forma(jatekszint=0):
    global mezo_forma
    if jatekszint == 1:
        mezo_forma = mezo_forma_lehetosegek[jatekszint]
    elif jatekszint ==3:
        mezo_forma = mezo_forma_lehetosegek[jatekszint]
    elif jatekszint ==4:
        mezo_forma = mezo_forma_lehetosegek[jatekszint]
    elif jatekszint ==5:
        mezo_forma = mezo_forma_lehetosegek[jatekszint]
    elif jatekszint ==6:
        mezo_forma = mezo_forma_lehetosegek[jatekszint]
    else:
        pass
    return mezo_forma

    
