from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
def greet():
    name = input("Enter ur name: ") #isi nama kamu
    greetings = input("Enter greetings: ")
    print(f"Hi, ", name ," it's ",current_time, greetings)
greet()
