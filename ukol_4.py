# Overeni platnosti telefonniho cisla (9 nebo 13mistne s platnou predvolbou)
def overeni_cisla(telefonni_cislo):
    # prvni ctyri znaky z telefonniho cisla
    predvolba = telefonni_cislo[:4]
    # Overeni delky telefonniho cisla a pripadne spravnosti predvolby
    if len(telefonni_cislo) == 9:
        return True
    elif len(telefonni_cislo) == 13:
        return predvolba == "+420"
    else:
        return False

# Vypocet ceny za SMS zpravu. 3 Kc za kazdych zapocatych 180 znaku.
def cena_sms(sms):
    return (3 + int(len(text_zpravy)/180) * 3)


# Zadani telefonniho cisla
telefonni_cislo = input("Zadejte telefonní číslo, na které bude zaslána SMS: ")

# Overeni, zda je zadane telefonni cislo platne (9 nebo 13mistne s platnou predvolbou)
platnost_cisla = overeni_cisla(telefonni_cislo)

if platnost_cisla == True:
    text_zpravy = input("Napište text SMS zprávy: ")    # Text SMS zpravy
    cena = cena_sms(text_zpravy)    # Cena za SMS zpravu
    print(f"Cena za SMS zpravu je {cena} Kc.")
else:
    print(False)
