#Nacteni dat
import pandas
import matplotlib.pyplot as plt
platy = pandas.read_csv('platy_2021_02.csv')

#print(platy)
print(platy['plat'].describe())

#platy.plot(kind='hist', bins=5, grid=True, subplots=True)
#platy['plat'].plot(kind='hist', bins=7, grid=True, subplots=True, edgecolor="black")
platy['plat'].plot(kind='hist', bins=[30000, 34000, 38000, 42000, 46000, 50000, 54000, 58000, 62000],  subplots=True, edgecolor="black")

#Nazev grafu
plt.title('Histogram platů v softwarové firmě')

#Popisek osy y
plt.ylabel('Četnost')

#Popisek osy x
plt.xlabel('Výše platu v Kč')

#Zobrazeni grafu
plt.show()


