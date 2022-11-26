loop = 1
while loop == 1:
      print("Pilih program\n 1. Penjumlahan\n 2. Pengurangan\n 3. Perkalian\n 4. Pembagian\n 5. Exit")
      menu = int(input("Masukkan pilihan : "))
      if menu == 1: 
        pilihan = "penjumlahan"
        angka1 =float(input ("Masukkan nilai pertama : "))
        angka2 =float(input ("Masukkan nilai kedua   : "))
        hasil = angka1 + angka2
        print("Hasil",pilihan, "antara %0.2f dengan %0.2f adalah %0.2f \n" %(angka1, angka2, hasil))
      elif menu == 2: 
        pilihan = "pengurangan" 
        angka1 =float(input ("Masukkan nilai pertama : "))
        angka2 =float(input ("Masukkan nilai kedua   : "))
        hasil = angka1 - angka2
        print("Hasil",pilihan, "antara %0.2f dengan %0.2f adalah %0.2f \n" %(angka1, angka2, hasil))
      elif menu == 3: 
        pilihan = "perkalian"
        angka1 =float(input ("Masukkan nilai pertama : "))
        angka2 =float(input ("Masukkan nilai kedua   : "))
        hasil = angka1 * angka2
        print("Hasil",pilihan, "antara %0.2f dengan %0.2f adalah %0.2f \n" %(angka1, angka2, hasil))
      elif menu == 4:
        pilihan = "pembagian"
        angka1 =float(input ("Masukkan nilai pertama : "))
        angka2 =float(input ("Masukkan nilai kedua   : "))
        hasil = angka1 / angka2
        print("Hasil",pilihan, "antara %0.2f dengan %0.2f adalah %0.2f \n" %(angka1, angka2, hasil))
      elif menu == 5:
        NAMA = "Fathiah Nuraisyah Radam"
        print(f"Terimakasih, telah menggunakan kalkulator {NAMA}")
        loop = 0
        break
      else:
            print("Input anda salah, silahkan coba lagi \n")
            
