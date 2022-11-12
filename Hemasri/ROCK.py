user_input = input("rock")
possible_actions = ("rock","paper","scissors")
computer_action = random.choice(possible_actions)
if user_input == computer_action:
    print("Tie")
elif user_input == "rock":
   if computer_action =="paper":
    print("computer wins")    
