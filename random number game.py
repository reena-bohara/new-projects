import random

print("i as computer have thought of a number b/w 1-100")
c = random.randint(1,100)
attempts = 0
lower=1
higher=100

while True:
    print(f"guess a number between {lower} and {higher}:\n")
    guess = int(input())
    if (guess==c):
        print(f"congrats!you got right answer after {attempts} attempts\n")
        break
    elif (guess<c):
        print("try an higher number\n")
        lower=guess
        attempts=attempts+1
    elif (guess>c):
        print("try an lower number\n")
        higher=guess
        attempts=attempts+1
    else:
        print("please enter a valid number\n")
