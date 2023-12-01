print("TUGAS 1")
produk = "laptop ASUS"
harga = 8000000
print("harga", produk, "adalah", harga, "\n")

print("TUGAS 2")
makanan = "nasi goreng"
jumlah = 2
print("saya makan", jumlah, "porsi", makanan, "\n")

print("haloo siapa nama kamu?")
nama = input("memasukan nama :")
print("dimana kamu tinggal?")
alamat = input("memasukan alamat :")
print("berapa umur kamu?")
umur = input("memasukan umur kamu")
print("dimana kamu lahir?")
tempat_lahir = input("memasukan tempat :")
print("senang bertemu denganmu", nama, "dari", alamat, "umur:", umur, "tempat lahir di:", tempat_lahir, "/n")

print("TUGAS ALGORITMA LUAS SEGITIGA")
alas = 10
tinggi = 25
luas = 1/2 * alas * tinggi 
print(luas)

print("latihan 1")
angka = int(input("masukan angka:"))
if angka > 10:
    print("angka yang Anda masukkan lebih besar dari 10")
else:
    print("angka yang Anda masukkan 10 atau kurang")

print("latihan 2")
angka = int(input("masukan angka:"))
if angka < 0:
    print("bilangan negatif")
elif angka > 0:
    print("bilangan positif")
else:
    print("bilangan nol")

print("latihan 3")
total_pembelanjaan = int(input("masukan total pembelajaan: "))
if total_pembelanjaan >= 100000:
    print("anda mendapatkan diskon 10%")
    diskon = total_pembelanjaan * 0.10
    harga_diskon = total_pembelanjaan - diskon
    print("total pembayaran: ", harga_diskon)
else: 
    print("anda tidak mendapatkan diskon")

print("latihan 4")
print("masukanlah angka 0-100")
nilai = int(input("masukan grade :"))
if nilai > 100:
    print("nilai tidak boleh lebih dari 100")
elif nilai >= 90:
    print("grade A")
elif nilai >= 80:
    print("grade B")
elif nilai >= 70:
    print("grade C")
elif nilai >= 60:
    print("grade D")
elif nilai < 0:
    print("masukan nilai dengan benar")
else :
    print("grade E")