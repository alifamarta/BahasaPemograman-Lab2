# input nilai variable
a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")

# print nilai variable
print("Variabel a =", a)
print("Variabel b =",b)

#konversi nilai variable
a = int(a)
b = int(b)

#print hasil operasi kedua variable dengan string format
a = int(a)
b = int(b)
print("Hasil penggabung {1}&{0}=%d".format(a,b) %(a&b))
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d.".format(a,b) %(a/b))