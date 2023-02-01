sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky = input("Zadej kod soucastky: ")
pocet_kusu = input("Zadej pocet kusu: ")

if kod_soucastky in sklad:  # Produkt je ve skladu
    if sklad[kod_soucastky] >= int(pocet_kusu): # Na sklade je vetsi pocet kusu nez je pozadovan
        print(f'Poptavku po soucastce {kod_soucastky} lze uspokojit v plne vysi.')
        sklad[kod_soucastky] = sklad[kod_soucastky] -int(pocet_kusu) # Snizeni poctu kusu o prodane mnozstvi
    else: # Na sklade je mene kusu, nez chce zakaznik
        print(f'Soucastky {kod_soucastky} lze prodat pouze omezene mnozstvi. Na sklade je {sklad[kod_soucastky]} kusu.')
        sklad.pop(kod_soucastky) # Vyrazeni polozky ze skladu
else:  # Produkt neni ve skladu
    print(f'Soucastka {kod_soucastky} neni skladem.')

print(sklad)