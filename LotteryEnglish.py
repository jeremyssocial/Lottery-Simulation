import random

correct = 0
total = 0
run = 1


howmany = int(input("How many correct guesses should there be? (0-6) "))
if howmany < 0:
    print("That was below 0.")
    quit()
elif howmany > 6:
    print("That was over 6.")
    quit()

runs = int(input("How many runs should there be? "))
if runs < 1:
    print("There has to be at least one run.")
    quit()


while run <= runs:
    correct = 0
    howoften = 0
    while correct != howmany:
        correct = 0
        guess = []
        drawing = []

        while len(guess) < 6:
            if len(guess) < 6:
                number = random.randint(1, 49)
                if not number in guess:
                    guess.append(number)
        while len(drawing) < 6:
            if len(drawing) < 6:
                number2 = random.randint(1, 49)
                if not number2 in drawing:
                    drawing.append(number2)

        y = 0
        while y < len(guess):
            x = 0
            while x < len(guess):
                if guess[x] == drawing[y]:
                    correct += 1
                x += 1
            y += 1
        howoften += 1
        print("run", (run), "| draw ",
              howoften, "| correct", correct)
    total += howoften
    run += 1


average = round((total / runs), 2)


print("To get", howmany, "correct guesses", runs, "times, there had to be a total of", total, "tries. That's an average of ", average, "tries per run. (so the chance is 1:" + str(average) + ")")
input("Hit Enter to exit")
