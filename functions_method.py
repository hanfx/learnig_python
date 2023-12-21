#functions
# print('a value')
# print(input('asl for a value: '))

#methods -> functions of datatypes
# print('value'.upper())
# print('value'.lower())
# print('value'.replace())

# input("ask for value = ")
# x = input("isi disini: ")
# print(x.replace('e', '3'))


#new functions
# print(abs(-1.5))
# print(max(11,9))
# print(min(1,8))
# print(len('test'))

#pythagoean theorem fucntion
def calc_pythagorean():
    print("Welcome to pythagoras calculator!")
    pilihan_hitung = input("ingin menghitung sisi apa? \n[A] Sisi Tegak \n[B] Alas Segitiga \n[C] Sisi Miring/Hypotenuse \n[D] Luas Segitiga Siku-siku \n[E] Keliling Segitiga Siku-siku \n: ")
    
    if pilihan_hitung == "C": #hitung sisi miring
        side_a = int(input("Side A = "))
        side_b = int(input("Side B = "))
        sisi_miring  = ((side_a ** 2) + (side_b ** 2)) ** 0.5
        print("Jadi sisi C =", sisi_miring)

    elif pilihan_hitung == "A": #hitung sisi tegak
        side_b = int(input("Side B = "))
        side_c = int(input("Side C = "))
        sisi_tegak  = ((side_b ** 2) - (side_c ** 2)) ** 0.5
        print("Jadi sisi tegak segitiga =", sisi_tegak)

    elif pilihan_hitung == "B": #hitung side B (alas)
        side_a = int(input("Side A = "))
        side_c = int(input("Side C = "))
        alas_segitiga  = ((side_c ** 2) - (side_a ** 2)) ** 0.5
        print("Jadi sisi B =", alas_segitiga)

    elif pilihan_hitung == "D": #hitung luas segitiga siku-siku
        side_b = int(input("Masukkan Alas = "))
        side_a = int(input("Masukkan Tinggi = "))
        luas_segitiga = 0.5 * (side_b * side_a)
        print("Jadi luas segitiga = ", luas_segitiga)

    elif pilihan_hitung == "E":
        sisi_tegak      = int(input("Sisi Tegak = "))
        alas_segitiga   = int(input("Alas Segitiga = "))
        sisi_miring     = int(input("Sisi Miring = "))
        keliling_segitiga = sisi_tegak + alas_segitiga + sisi_miring
        print("Jadi keliling segitiga = ", keliling_segitiga)

    else:
        print("Mohon inputkan salah satu pilihan A hingga E")


    hitung_ulang = input("Ingin menghitung ulang?: [Y/N]")
    if hitung_ulang == "y":
        calc_pythagorean()
    else:
        print("Thank you!")
        exit()
        
calc_pythagorean()