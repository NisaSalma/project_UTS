listKota = [ 'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makassar' ]

for i, kota in enumerate(listKota): print(i, kota)

a = int(input('Masukkan bilangan ganjil lebih dari 50: '))

while a % 2 != 1 or a <= 50: a = int(input('Salah, masukkan lagi: '))

print('Benar')