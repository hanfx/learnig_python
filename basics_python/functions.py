
# def greet(name, time):
#     print(f"Good {time}, {name}, hope you are well")
# greet("shaun", "morning")

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
def greet(name, current_time, greetings):
    print(f"Hi, {name}, it's {current_time}, {greetings}") 
greet("Farhan", current_time, "Hope u are well")

input()