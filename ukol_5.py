#seznam namerenych teplot
teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#print(teploty)

#seznam prumernych dennich teplot

#seznam rannich teplot
ranni_teploty = [hodnoty[0] for hodnoty in teploty]
print(ranni_teploty)

#seznam nocnich teplot
nocni_teploty = [hodnoty[3] for hodnoty in teploty]
print(nocni_teploty)

#seznam polednich a nocnich teplot
poledni_nocni_teploty = [hodnoty[1:5:2] for hodnoty in teploty]
print(poledni_nocni_teploty)