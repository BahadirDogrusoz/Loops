liste = ["Adana","Ankara","İzmir","Kayseri"]

for sehirler in liste:
    print(sehirler)


print("--------------------------------------------")

maaslar = [1500,1750,3500,5400]

for maas in maaslar:
    if maas > 1000 and maas < 2000:
        yeni_maas = maas + 200
        print(yeni_maas)

print("--------------------------------------------")

sayilar = [1,2,3,4]

for sayi in sayilar:
    print(sayi)
    if sayi == 2:
        break
print("--------------------------------------------")

for sayi1 in sayilar:
    print(sayi1)
    if sayi == 2:
        continue

print("--------------------------------------------")
print("While Kullanımı")

i = 1
while i < 6:
    print(i)
    i += 1