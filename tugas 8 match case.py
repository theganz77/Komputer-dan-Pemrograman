#tugas 8 

Pilih=int(input('Input Pilihan OPERATOR 1/2/3/4:'))
match Pilih:
    case 1:
        a=float(input('Masukan Nilai a:'))
        b=float(input('Masukan Nilai b:'))
        c=a+b
        print("Hasil Jumlah",c)
    case 2:
        a=float(input("Masukan Nilai a:"))
        b=float(input('Masukan Nilai b:'))
        c=a-b
        print("Hasil Selisih",c)
    case 3:
        a=float(input('Masukan Nilai a:'))
        b=float(input('Masukan Nilai b:'))
        c=a*b
        print("Hasil Kali",c)
    case 4:
        a=float(input("Masukan Nilai a:"))
        b=float(input('Masukan Nilai b:'))
        c=a/b
        print("Hasil Bagi",c)
    case _:

        print("Pilihan Tidak Tersedia")
