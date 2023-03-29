import pandas

#Nacteni dat
zam_praha = pandas.read_csv('zam_praha.csv')
zam_plzen = pandas.read_csv('zam_plzen.csv')
zam_liberec = pandas.read_csv('zam_liberec.csv')

#Zobrazeni dat
#print(zam_praha)
#print(zam_plzen)
#print(zam_liberec)

#Pridani sloupce s nazvem mesta
zam_praha['mesto'] = 'Praha'
zam_plzen['mesto'] = 'Plzeň'
zam_liberec['mesto'] = 'Liberec'

#print(zam_praha)
#print(zam_plzen)
#print(zam_liberec)

#Slouceni tabulek se zamestnanci
zam_mesta = pandas.concat([zam_praha, zam_plzen, zam_liberec], ignore_index=True)
print(zam_mesta)

#Nacteni dat s platy za unor
platy_2021_02 = pandas.read_csv('platy_2021_02.csv')
print(platy_2021_02)

#Pridani vyse platu k jednotlivym zamestnancům (podle cislo_zamestnance)
zam_platy = pandas.merge(zam_mesta, platy_2021_02, on=['cislo_zamestnance'], how = 'outer')
print(zam_platy)

#kontrola rozmeru tabulky pred spojenim a po spojeni
print(zam_platy.shape)
print(zam_mesta.shape)

#propusteni zamestnanci
print(zam_platy[zam_platy['plat'].isnull()])

#spojeni bez propustenych
zam_platy_akt = pandas.merge(zam_mesta, platy_2021_02, on=['cislo_zamestnance'])
print(zam_mesta.shape)
print(zam_platy_akt.shape)

#prumerny plat podle mest
print(zam_platy_akt.groupby('mesto')['plat'].mean())

####################################################################################
#Zadani c. 2

#Nacteni dat
vykazy = pandas.read_csv('vykazy.csv')

#Zobrazeni dat
print(vykazy)

#Celkovy pocet vykazanych hodin za jednotlive projekty
print(vykazy.groupby('project')['hours'].sum())