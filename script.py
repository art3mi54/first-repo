import random 

# Intro 
print("====================================================")
print("               Rock, Paper, Scissors                ")
print("====================================================")
print("")

# Number Key
print("        KEY: ")
print("_______________________ ")
print("")
print("1 is for '' (Rock).")
print("2 is for '' (Paper).")
print("3 is for '' (Scissors).")
print("_______________________ ")
print("")

# Full Game
def game():

  # Choosing time
  player = int(input("Pick a number: "))
  comp_pick = random.randint(1, 3)
  print("")

  # Player Chose 
  if player == 1:
    print("You chose: ")
  elif player == 2:
    print("You chose: ")
  elif player == 3:
    print("You chose: ")
  else: 
    print("Invalid Number")

  # Computer Chose
  if comp_pick == 1:
    print("CPU chose: ")
  elif comp_pick == 2:
    print("CPU chose: ")
  elif comp_pick == 3:
    print("CPU chose: ")
  else: 
    print("Invalid Number")
  print("")

  # Player Chose Rock
  if player == 1:
    if player == 1 and comp_pick == 1:
      print("Tie!")
    elif player == 1 and comp_pick == 2:
      print("CPU Wins!")
    elif player == 1 and comp_pick == 3:
      print("Player Wins!")
    else:
      print("Error.")

  # Player Chose Paper
  if player == 2: 
    if player == 2 and comp_pick == 1:
      print("Player Wins!")
    elif player == 2 and comp_pick == 2:
      print("Tie!")
    elif player == 2 and comp_pick == 3:
      print("CPU Wins!")
    else:
      print("Error.")

  # Player Chose Paper
  if player == 3:
    if player == 3 and comp_pick == 1:
      print("CPU Wins!")
    elif player == 3 and comp_pick == 2:
      print("Player Wins!")
    elif player == 3 and comp_pick == 3:
      print("Tie!")
    else:
      print("Error.")

# Start game
game()
print("")
play_again = input("Play Again (Y or N): ")
print("")

while play_again == "Y":
  game()
else:
  print("Thanks for Playing!")
