from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#guesses
def check_answer(guess,answer,turns):
  """checks answer against guess & returns remaining. """
    
  if guess > answer:
    print("Too high")
    return turns -1
  
  elif guess < answer:
    print("Too low")
    return turns -1
  else:
    print("You've guessed {answer} right!!")
 
 #dificulty_levels   
def set_dificulty():
  level = input("Chose a level;'easy' or 'hard':")
  
  if level == 'easy':
    return EASY_LEVEL_TURNS
    
  elif level == 'hard':
    return HARD_LEVEL_TURNS
    
  else:
      print("Choose a valid level")

#game 
def game(): 
 print("Welcome to the Number Guessing Game!")
 print("Guess a number between 1 and 100")
 answer = randint(1,100)
     #test
     #print(f"The correct answer is {answer}")

 turns = set_dificulty()           

#attempts
 guess = 0
 while guess != answer:
  print(f"You have {turns} attempts remaining!")
  guess = int(input("Make a guess: "))

#guess_count  
  turns = check_answer(guess,answer,turns)
  if turns == 0:
    print("You've run out of guesses you loose!")
    return
  elif guess != answer:
      print("Guess again!")
game()
            
