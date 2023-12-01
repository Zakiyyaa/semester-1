for i in range(1, 25) :
    for j in range(1, 61):
        print("---", j)
    print(i)

for i in range(1, 6):
    for j in range(1, 4):
        print(i, "x", j, "=", int(i * j))
    print(i)

kumpulan_barang = [["meja", "kursi", "tatakan"], ["mpnitor", "tv", "handphone"]]
for barang in kumpulan_barang :
    for item in barang :
        print(item, end=",")
    print()

#tugas 1
matriks = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print (matriks)
for angka in matriks :
    for number in angka :
        print (number)

#tugas 2 & 3
buku_alamat = [
    ["John Doe", "555-1234"],
    ["Jane Smith", "555-5678"],
    ["Bob Johnson", "555-7890"]
]
for alamat in buku_alamat :
    print(alamat[0], " - ", alamat[1])

#tugas 4
for i in range (1,6) :
    for j in range (1,6) :
        print(i * j, end="\t")
    print()

#tugas 5
for i in range (1,6) :
    for j in range (1, i + 1) :
        print(i * j, end= "\t")
    print()