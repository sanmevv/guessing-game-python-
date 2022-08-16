from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer):
  if guess > answer:
    print("Too high")
  
  elif guess < answer:
    print("Too low")
    
  else guess = answer:
    print("You've guessed {answer} right!!")
    
def set_dificulty():
  level = input("Chose a level;'easy' or 'hard'.")
  
  if level == 'easy':
    return EASY_LEVEL_TURNS
    
  else level == 'hard':
    return HARD_LEVEL_TURNS
    
print("Number Guessing Game!")
print("Guessing a number between 1 and 100")

answer = randint(1,100)
print(f"The correct answer is {answer}")

guess = int(input("Make a guess: ")
turns = set_dificulty()           
print(f"You have {turns} attempts remaining!")
            
