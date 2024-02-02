#containers
a_tuple   = (1,2,3, 'a_string') #tuple cannot be changed the value
a_list  = [1,2,3, 'a_string',3,4,5,3,3,3] #list can be change the value
a_set = {1,2,3, 'a_string', 2,1,3,4} #set cannot double the same value
user_list = ['lisa','bob','alex','anna','john','fred','miftah']

# print(list(set(a_list))) #cannot print list bcause of double value
#dictionary examples
a_dictionary = {'key': 'addresses', 
                123: [1,2,3]}
a_dictionary['new key'] = 1.3

warna_buah = dict(jeruk='orange', 
                  apel='merah', 
                  pisang='kuning') #dictionary with constructor

new_list = [1,2,3,4,5,6,7,8,9,10]

# print("key berisi %s" % a_dictionary[123]) #calling value from dictionary
# print("warna buah jeruk adalah", warna_buah.get('jeruk')) #dengan method get

<<<<<<< HEAD
print(user_list[::-2])
=======
# print(user_list[0:3:2])
# reversed_list = new_list[0:8:1] # [start:end:step]
# print(reversed_list[::-2]) #output 8,6,4,2

#or
print(new_list[7::-2])
>>>>>>> 73e80ee25a90861a70965a1bf7dec3675846eff3
