u = int (input("Masukkan Usia Anda: "))
d = int (input("Masukkan Tekanan Darah Anda: "))

if u >= 60 and d > 140:
    print("Status Kesehatan: Tinggi")
elif u >= 60 and d <= 140:
    print("Status Kesehatan: Normal")
elif u < 60 and d > 130:
    print("Status Kesehatan: Tinggi")
elif u < 60 and d <= 130:
    print("Status Kesehatan: Normal")
else:
    print()