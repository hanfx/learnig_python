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
    print("welcome to calculator pythagoras!")
    pilihan_hitung = str(input("ingin menghitung sisi apa? [A, B, atau C]"))
    
    while pilihan_hitung == "C || c":
        side_a = int(input("Side A = "))
        side_b = int(input("Side B = "))
        x  = (side_a ** 2) + (side_b ** 2)
        square_root = x ** (0.5)
        print("Jadi sisi C =", round(square_root,2))
        hitung_ulang1 = input("Ingin menghitung ulang?: [Y/N]")
        if hitung_ulang1 == "y":
            calc_pythagorean()
        else:
            print("thank you!")
            exit()

    while pilihan_hitung == "A" or "a":
        side_b = int(input("Side B = "))
        side_c = int(input("Side C = "))
        x  = (side_b ** 2) - (side_c ** 2)
        square_root = x ** (0.5)
        print("Jadi sisi A =", round(square_root,2))

    while pilihan_hitung == "B" or "b":
        side_a = int(input("Side a = "))
        side_c = int(input("Side c = "))
        x  = (side_b ** 2) - (side_c ** 2)
        square_root = x ** (0.5)
        print("Jadi sisi B =", round(square_root,2))

    else:
        hitung_ulang = input("Ingin menghitung ulang1?: [Y/N]")
        if hitung_ulang == "y":
            calc_pythagorean()
        else:
            print("thank you!")
            exit()
        
calc_pythagorean()