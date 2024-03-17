#f strings
# user_name   = 'Anna'
# user_age = 10
# user_information = f'{user_name} is {user_age + 10} years old'
# bad_approach = user_name + ' is ' + str(user_age) + ' years old'
# print(user_information)

#sigle line if statement
# user_name = 'Anna'
# user_age = 10
# user_status = 'Adult' if user_age >= 18 else 'Child'
# # if user_age > 18:
# #     user_status = 'Child'
# # else:
# #     user_status = 'Adult'
# # print(user_status)

# print (f'{user_name} is {user_age} years old. The person is a {"adult" if user_age >= 18 else "child"}')

#list comprehension
simple_list = []
for i in range(0, 11, 1):
    simple_list.append(i)
print(simple_list)

simple_list2 = [i * 2 for i in range(0,11,1) for j in ('a','b','c') ]
print(simple_list2)