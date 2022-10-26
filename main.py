import random

toprange = input("Gib eine Zahl ein: ")

if toprange.isdigit():
    toprange = int(toprange)

    if toprange <= 0:
        print("bitte gibt eine Zahl an die größer als 0 ist")
        quit()
else:
    print("Bitte schreib eine Zahl")
    quit()
r = random.randint(0,toprange)
guesses = 0
while True:
    user_guess = input("Rate die Zahl. ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Bitte schreib eine Zahl")
        continue

    if user_guess == r:
        print("Das ist die Richtige Zahl!")
        break
    else:
        if user_guess > r:
            print("Du lagst über der Zahl")
            guesses += 1
            print("Du hast schon " + str(guesses) + " mal geraten")
        else:
            print("Du liegst unter der Zahl")
            guesses += 1
            print("Du hast schon " + str(guesses) + " mal geraten")


print("Du hast es mit," + str(guesses) + " Versuchen erraten")



print(r)