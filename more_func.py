#create func
def print_x_times(parameter = 'loop', loop_amount = 5):
    counter = 0
    print(global_var)
    while counter < loop_amount:
        print(counter, parameter)
        counter += 1
    return 'jumlah counter adalah', loop_amount

# global_var = 'global variable'
# test = print_x_times('something', 4)
# print(test)

def hypotenuse_calc(side_a = 1, side_b = 1):
    hypotenuse = (side_a ** 2 + side_b ** 2) ** (1/2)
    return round(hypotenuse,2)

print(hypotenuse_calc(side_a = 1, side_b= 2))


#exercise
def shout(output_string, repetition_amount):
    if repetition_amount <= 10:
        for i in range(repetition_amount):
            print(output_string.upper())
    else:
        print("you're too loud")


    return 'done'

status = shout('test',5)
print(status)