#tugas 6

Nama=input('Nama:')
NIM=input('NIM:')
JN=float(input("Masukan Jumlah Nilai:"))
JSKS=int(input("Masukan Jumlah SKS:"))
IPK=JN/JSKS
print("Predikat Mahasiswa Berdasarkan IPK")
print("*"*35)
print("Nama:",Nama)
print("NIM:",NIM)
print("Index Prestasi Kumulatif:",IPK)
if IPK<=3.50:
    if IPK<=3.00:
        if IPK<=2.50:
            if IPK<=2.00:
                print("Predikat Anda Memprihatinkan")
                print("_"*35)
            else:
                print("Predikat Anda Kurang")
                print("_"*35)
        else:
            print("Predikat Anda Cukup")
            print("_"*35)
    else:
        print("Predikat Anda Baik")
        print("_"*35)
else:
    print("Predikat Anda Cumlaude")
    print("_"*35)