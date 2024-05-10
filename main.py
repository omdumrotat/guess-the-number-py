import random
import time

attempt = 0
highscore = 0
realnumber = random.randint(1, 100)

print("Guess the Number")
time.sleep(2)
print("Try to guess the correct number within 20 attempts or fewer")
time.sleep(1)

def announce():
    print("You have used " + str(attempt) + " attempts")

while True:
    if attempt < 20:
        m = input("Input: ")
        if int(m) > realnumber:
            print("Too high")
            attempt += 1
            announce()
        elif int(m) < realnumber:
            print("Too low")
            attempt += 1
            announce()
        elif int(m) == realnumber:
            print("You guessed the right number")
            attempt += 1
            time.sleep(1)
            print("You used " + str(attempt) + " attempts")
            if highscore == 0 or highscore > attempt:
                difference = highscore - attempt
                if difference > 0:
                    print("You've set a new Game record; lesser by " + str(difference) + " attempts")
                else:
                    print("Congratulations! You've set a new Game record")
                highscore = attempt
            else:
                difference = attempt - highscore
                print("You've used more attempts than the record by " + str(difference) + " attempts")
            q = input("Do you want to play again from the beginning? Y or N: ")
            if q == "Y":
                attempt = 0
                realnumber = random.randint(1, 100)
            else:
                break
    else:
        print("You have to start over")
        attempt = 0
        realnumber = random.randint(1, 100)
