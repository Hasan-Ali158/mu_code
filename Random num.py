import random

random_num=random.randint(1,10)
attempt=3

for attempt in range(attempt):
    guess = int(input("Guess the number (1-10) (Attempt {attempt + 1}): "))

    if guess==random_num:
        print('winner! You guess the correct num.')
        break

    else:
     print('incorrect! try again')

if guess != random_num:
    print("Sorry, you're out of attempts. The correct num was {random_num}. You're a loser.")









