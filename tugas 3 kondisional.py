#tugas 3

Nama=input("Masukkan Nama:")
Kelas=input("Masukkan Kelas:")
NUTS=float(input("Masukkan nilai NUTS:"))
NUAS=float(input("Masukkan nilai NUAS:"))
NA=(NUTS+NUAS)/2
if NA >= 60:
    print("Mencetak Nilai Mahasiswa")
    print("="*25)
    print("Nama Mahasiswa:",Nama)
    print("Kelas Mahasiswa:",Kelas)
    print("Nilai Akhir:",NA)
    print("Keterangan: Lulus")
    print("="*25)
else:
    print("Mencetak Nilai Mahasiswa")
    print("="*25)
    print("Nama Mahasiswa:",Nama)
    print("Kelas Mahasiswa:",Kelas)
    print("Nilai Akhir:",NA)
    print("Keterangan: Gagal")
    print("="*25)