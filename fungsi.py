def menyapa(nama, tempat):
    print("halo deq", nama)
    print("welkom bek di", tempat)

menyapa("perli", "isekai")

#soal 1
def hitung (angka1, angka2, operator) :
    if(operator == "+") :
        return angka1 + angka2
    elif(operator == "-") :
        return angka1 - angka2
    elif(operator == "x") :
        return angka1 * angka2
    else :
        print("operator tidak valid")
print(hitung(4, 3, "+"))
print(hitung(7, 2, "-"))
print(hitung(5, 2, "x"))

#soal 2
def perulangan(nama, perulangan) :
    for i in range(perulangan) :
        print(nama)
perulangan("p hlo", 10)