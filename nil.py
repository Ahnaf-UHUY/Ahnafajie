nil = int(input("Masukkan Nilai Ujian Anda (0-100): "))

if 100 >= nil >= 90:
    print("Feedback: Sangat Baik")
elif 89 >= nil >= 80:
    print("Feedback: Baik")
elif 79 >= nil >= 70:
    print("Feedback: Cukup")
elif 69 >= nil >= 60:
    print("Feedback: Kurang")
else:
    print("feedback: Sangat Kurang")