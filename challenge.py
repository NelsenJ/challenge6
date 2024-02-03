x = int(input("Masukkan Angka : "))
while x > 0:
    if x > 20:
        if x % 2 == 0:
            x = int(input("Masukkan Angka : "))
        elif x % 2 == 1:
            print("True")
            break
    else:
        x = int(input("Masukkan Angka : "))
