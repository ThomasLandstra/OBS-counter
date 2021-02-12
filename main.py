import keyboard, time
from win10toast import ToastNotifier

template = input("What are you counting? ")
print("")
countI = int(input("What is the increment value? "))
countD = int(input("What is the decrement value? "))
print("")
notify = input("Would you like a notification to appear when you increment or decrement the value? ")
print("")
keybindUp = input("Please enter a keybind to increment: ")
keybindDown = input("Please enter a keybind to decrement: ")

if notify.lower() == "yes" or notify.lower() == "y":
    notify = True
    print("a")
else:
    notify = False

value = 0

while True:
    if keyboard.is_pressed(keybindUp):
        value += countI
        file = open("counter.txt", "w")
        file.write(template + ": " + str(value))
        file.close()
        if notify:
            ToastNotifier().show_toast("Added", "Total is: " + str(value), duration=1)
        else:
            time.sleep(1)
    
    if keyboard.is_pressed(keybindDown):
        value -= countD
        file = open("counter.txt", "w")
        file.write(template + ": " + str(value))
        file.close()
        if notify:
            ToastNotifier().show_toast("Added", "Total is: " + str(value), duration=1)
        else:
            time.sleep(1)
