import pandas

#nacteni dat
teplota = pandas.read_csv('temperature.csv')

#vypis prvnich par radku tabulky
teplota.head()

#zaklani info o tabulce
teplota.info()

#nazvy sloupcu
print(teplota.columns)

#Dotaz na měření, která byla provedena v Praze. (Teplota neni ve stupnich Celsia ale ve stupních Fahrenheita)
praha = teplota[teplota["City"] == "Prague"]
print(praha)
print(praha[["City","AvgTemperature"]])

#Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
teplota_80 = teplota[teplota["AvgTemperature"] > 80]
print(teplota_80)

#Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
teplota_60_evropa = teplota[(teplota["AvgTemperature"] > 60) & (teplota["Region"] == "Europe")]
print(teplota_60_evropa)

#Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než -20 stupňů.
teplota_extrem = teplota[(teplota["AvgTemperature"] > 80) | (teplota["AvgTemperature"] < -20)]
print(teplota_extrem)
