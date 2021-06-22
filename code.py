import csv
import matplotlib.pyplot as plt
import math


ratings = []

with open('got_imdb.csv', 'r') as readFile:
    reader = csv.reader(readFile)
    bolumler = list(reader)[1:]  # basliklar silindi
    for bolum in bolumler:
        ratings.append(float(bolum[4]))


readFile.close()
ratings.sort()



def ortalamaHesapla(liste):
    total = 0
    for bolum in liste:
        total += bolum
    ortalama = total/(len(liste))
    return ortalama


def medyan(liste):
    boyut = len(liste)
    if((boyut % 2) == 0):  # cift
        return((liste[int(boyut/2-1)]+liste[int(boyut/2)])/2)
    else:
        return(liste[int(boyut/2)])


def varyans(liste):
    boyut = len(liste)
    total2 = 0

    for bolum in liste:
        total2 += (bolum-ortalamaHesapla(liste))**2

    return total2/boyut


def standartSapma(liste):
    return ((math.sqrt(varyans(liste))))


def standartHata(liste):
    return((standartSapma(liste))/(math.sqrt(len(liste))))


def dagiliminSekli(liste):
    if(ortalamaHesapla(liste) > medyan(liste)):
        return("Right Skewed")
    elif(ortalamaHesapla(liste) < medyan(liste)):
        return("Left Skewed")
    else:
        return("Center Skewed")


def histogram(liste):
    plt.hist(liste, bins=7,
             color="bisque", label="Ratings", histtype="step", orientation="vertical")
    plt.xlabel("Oranlar")
    plt.ylabel("Dağılımlar")
    plt.legend()
    plt.title("Game of Thrones imdb rating oranları")
    plt.show()


def Q1(liste):
    boyut = len(liste)
    if((boyut % 2) == 0):  # cift
        return((liste[int(boyut/4-1)]+liste[int(boyut/4)])/2)
    else:
        return(liste[int(boyut/4)])


def Q3(liste):
    boyut = len(liste)
    if((boyut % 2) == 0):  # cift
        return((liste[int(3*(boyut/4)-1)]+liste[int(3*boyut/4)])/2)
    else:
        return(liste[int(3*boyut/4)])


def Iqr(liste):
    return(Q3(liste)-Q1(liste))


def minimum(liste):
    return (Q1(liste)-((1.5)*Iqr(liste)))


def maksimum(liste):
    return (Q3(liste)+((1.5)*Iqr(liste)))

def aykiriDegerler(liste):#%95 için Z0.025=1.96
    aykiridegerler=[]
    for deger in liste:
        if deger>maksimum(liste) or deger<minimum(liste):
            aykiridegerler.append(deger)
    return aykiridegerler
def güvenAraligi(liste):
    return ortalamaHesapla(liste)+1.96*(standartSapma(liste)/math.sqrt(len(liste)))
def güvenAraligi(liste):
    return ortalamaHesapla(liste)+1.96*(standartSapma(liste)/math.sqrt(len(liste)))


# print(ratings)
print("ortalama:",ortalamaHesapla(ratings))

print("medyan:",medyan(ratings))

print("varyans:",varyans(ratings))
print("standart sapma:",standartSapma(ratings))
print("standart hata:",standartHata(ratings))

print("Dagilim şekli:",dagiliminSekli(ratings))

print("Q1: ", Q1(ratings))
print("Q3: ", Q3(ratings))
print("iqr ", Iqr(ratings))

print("minimum: ", minimum(ratings))
print("maksimum: ", maksimum(ratings))
print("aykiri degerler: ", aykiriDegerler(ratings))
histogram(ratings)

print("%95 için güven araligi: ",güvenAraligi(ratings[0:50:2]))


