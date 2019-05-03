def pangkat (x,y):
    angka = []
    hasil = 1
    for i in range(y):
        angka.append(x)
        hasil *= angka[i]
    return hasil

print(pangkat(2, 2))
print(pangkat(3, 3))
print(pangkat(10, 5))

# Bila menggunakan input dari user
# x = int(input('Silakan masukkan angka pertama: '))
# y = int(input('Silakan masukkan angka kedua: '))
# z = pangkat(x,y)
# print(x, 'pangkat', y, '=', z)