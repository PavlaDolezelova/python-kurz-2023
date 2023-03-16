import pandas

#nacteni dat
adopce = pandas.read_csv('adopce-zvirat.csv',sep = ';')

print(adopce)

#zaklani info o tabulce
adopce.info()

#pocet radku
print(adopce.shape[0])

#pocet sloupcu
print(adopce.shape[1])

#nazvy sloupcu
print(adopce.columns)

#zaznam s indexem 34 (nazev v cz a en)
print(adopce.iloc[34,[1,2]])
