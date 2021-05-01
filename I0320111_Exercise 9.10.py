import array
A = array.array('i', [100,200,300,400,500])

A[1] = -700   # mengubah elemen kedua
A[4] = 800    # mengubah elemen kelima

# nilai awal (sebelum dibalik)
print(A)

# membalik urutan elemen array
A.reverse()

# nilai akhir (setelah dibalik)
print(A)