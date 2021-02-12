import keyboard
from win10toast import ToastNotifier

template = input("What are you counting? ")
count = int(input("What is the increment value? "))
value = 0

while True:
    if keyboard.is_pressed("ctrl+l"):
        value += count
        file = open("counter.txt", "w")
        file.write(template + ": " + str(value))
        file.close()
        ToastNotifier().show_toast("Added", "Total is: " + str(value), duration=1)
    