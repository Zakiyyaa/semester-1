bulan = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]
print(bulan[0])
print(bulan[3])
print(bulan[4])
print(bulan[5])
bulan[3]="maret"
print(bulan[3])
bulan.append("desember")
print(bulan[12])


daftar_buah = ["anggur", "nanas", "jeruk", "semangka", "apel"]
for buah in daftar_buah:
    print("buah:", buah)


nilai_siswa = [95, 85, 75, 90, 80, 80, 90]
print("nilai rata-rata :", sum (nilai_siswa)/len(nilai_siswa))
print("nilai tertinggi siswa :", max (nilai_siswa))
print("angka 80 ada :", nilai_siswa.count(80))
