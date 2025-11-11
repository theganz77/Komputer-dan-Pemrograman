#tugas 4

Nama=input("Masukan Nama:")
NIM=input("Masukan NIM:")
JN=float(input("Nilai:"))
JSKS=float(input("SKS:"))
IPK=JN/JSKS
print("Predikat Mahasiswa")
print("="*20)
print("Nama Mahasiswa:",Nama)
print("NIM:",NIM)
print("Indeks Prestasi Kumulatif:",IPK)
if IPK>=3.50 and IPK <4.00 :
    print("Predikat Anda Cumlaude")
    print("="*20)
if IPK>=3.00 and IPK <3.50 :
    print("Predikat Anda Baik")
    print("="*20)
if IPK>=2.50 and IPK<3.00 :
    print("Predikat Anda Cukup")
    print("="*20)
if IPK>=2.00 and IPK<2.50 :
    print("Predikat Anda Kurang")
    print("="*20)
if IPK< 2.00 :
    print("Predikat Anda Prihatin")
    print("="*20)