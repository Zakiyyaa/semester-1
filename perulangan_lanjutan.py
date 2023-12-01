#tugas 1
for angka in range(1, 11) :
    if angka % 2 !=0 :
        print("angka ganjil pertama yang ditemukan", angka)
        break
    
#tugas 2
total = 0
while True :
    bilangan = int(input("masukan bilangan bulat positif :"))
    if bilangan < 0 :
        break
    total += bilangan
print("jumlah dari bilangan positif yang dimasukan :", total)

#tugas 3
count = 0
for angka in range(1, 51) :
    if angka % 5 == 0:
        print(angka)
        count += 1
    if count == 10 :
        break