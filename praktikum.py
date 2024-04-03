print("_-_"*15)
print(" MASUKKAN DATA NILAI ".center(45,"~"))
print("_-_"*15)
nama = input("Masukkan Nama = ")
nim = input("Masukkan NIM = ")
prodi = input("Masukkan Prodi = ")
absen = int(input("Masukkan Nomor Absen = "))
uts = int(input("Masukkan Nilai UTS = "))
uas = int(input("Masukkan Nilai UAS = "))
print("~"*50)
print("Nama Mahasiswa "+":",nama)
print("NIM Mahasiswa " + ":",nim)
print("Prodi Mahasiswa " + ":",prodi)
print("~"*50)
nilai_batas = 60
jumlah = absen + uts + uas
rata_rata = jumlah/3
print("Jumlah Niai =",jumlah)
print("rata_rata Nilai = ",rata_rata)
print("~"*50
)
if rata_rata >=90 <=100:
 print("anda mendapatkan nilai A+")
elif rata_rata >= 80 <= 90:
  print("anda mendapatkan nilai A")
elif rata_rata >= 70 <= 80:
  print("anda mendapatkan nilai B+")
elif rata_rata >= 60 <= 70:
  print("anda mendapatkan nilai B")
elif rata_rata >= 50 <= 60:
  print("anda mendapatkan nilai C")  
else:
  print("nilai kamu buruk")
  
if rata_rata >= nilai_batas:
  print("selamat anda mendapatkan nilai yang bagus")
else:
  print("anda gagal dan harus belajar lagi wkwk")