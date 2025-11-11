#tugas 7

Nama=input('Nama:')
NIM=input('NIM:')
JN=float(input("Masukan Jumlah Nilai:"))
JSKS=int(input("Masukan Jumlah SKS:"))
IPK=JN/JSKS
print("Predikat Mahasiswa Berdasarkan IPK")
print("_"*35)
print("Nama:",Nama)
print("NIM:",NIM)
print("Index Prestasi Kumulatif:",IPK)
if IPK>=3.50:
    print("Anda Berpredikat CumLaude")
    print("_"*35)
else:
    if IPK>=3.00:
        print("Anda Berpredikat Baik")
        print("_"*35)
    else:
        if IPK>=2.50:
            print("Anda Berpredikat Cukup")
            print("_"*35)
        else:
            if IPK>=2.00:
                print("Anda Berpredikat Kurang")
                print("_"*35)
            else:
                print("Anda Berpredikat Memprihatinkan")
                print("_"*35)