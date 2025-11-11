#tugas 3

Nama=input('Nama:')
NIM=input('NIM:')
NUTS=float(input("Nilai UTS:"))
NUAS=float(input("Nilai UAS:"))
NA=(NUTS+NUAS)/2
print("Grade Mahasiswa Berdasarkan Nilai")
print("="*25)
print("Nama",Nama)
print("NIM:",NIM)
print("NIlai Akhir:",NA)
if NA>=80:
    print("Dapat Grade A")
    print("="*25)
else:
    if NA>=70:
       print("Dapat Grade B")
       print("="*25)
    else:
        if NA>=60:
          print("Dapat Grade C")
          print("="*25)
        else:
            if NA>=50:
                print("Dapat Grade D")
                print("="*25)
            else:
                if NA<50:
                    print("Dapat Grade E")
                    print("="*25) 
