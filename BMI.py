#Berat Badan Ideal

Nama=input("Nama:")
Umur=input("Umur:")
Jenis_Kelamin=input("Jenis Kelamin:")
BB=float(input("Masukan Berat Badan:"))
TB=float(input("Masukan Tinggi Badan:"))
BMI=BB/(TB*TB)

print("="*25)
print("Berat Massa Index")
print("Nama:",Nama)
print("Umur:",Umur)
print("Jenis Kelamin:",Jenis_Kelamin)
print("Berat Badan:",BB,"kg")
print("Tinggi Badan:",TB,"m")
print("BMI Anda Adalah:",BMI)
if BMI<=28.50:
    if BMI<=24.50:
        if BMI<=18.50:
            if BMI<12.50:
                print("Anda tergolong KURANG GIZI")
                print("="*25)
            else:
                print("Anda tergolong KURUS")
                print("="*25)
        else:
            print("Anda tergolong NORMAL")
            print("="*25)
    else:
        print("Anda tergolong GEMUK")
        print("="*25)
else:
    print("Anda tergolong OBESITAS")
    print("="*25)