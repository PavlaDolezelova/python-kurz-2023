#vytvoreni tridy Auto
class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne == True:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla."
        else: 
            return "Vozidlo není k dispozici."

    def get_info(self):
        return f"Auto: {self.registracni_znacka}, Typ vozidla: {self.typ_vozidla}, Počet najetých km: {self.najete_km} km."

Peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
Škoda = Auto("1P3 4747", "Škoda Octavia", 41253)  
        
pujcovna = input("Zadejte značku auta, které chcete půjčit (Peugeot, Škoda): ")

Peugeot.pujc_auto()
print(Peugeot.get_info())
print(Peugeot.pujc_auto())
