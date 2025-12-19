# # Shopping cart program

# # foods = []
# # prices = []
# # total = 0

# # while True:
# #   food = input("What would you like to eat (q to quit): ")
# #   if food.lower() == "q":
# #     break
# #   else:
# #     price = float(input(f"What is the price of {food}$: "))
# #     foods.append(food)
# #     prices.append(price)

# # print("------Your Cart-------")

# # for food in foods:
# #   print(food, end=" ")

# # for price in prices:
# #   total += price

# # print()
# # print(f"Your total is: $ ({total:.2f})")

# #_____________________________________________________________________________

# # day 7 keypad program

# # num_pad = ((1,2,3),
# #            (4,5,6),
# #            (7,8,9),
# #            ("*",0,"#"))

# # for row in num_pad:
# #   for num in row:
# #     print(num, end=" ")
# #   print()

# #_____________________________________________________________________________

# # day 7 Python quiz game

# questions = (("What is the prettiest girl in the earth? "),
#              ("What color is the sun: "),
#              ("What is the sum of 3+4: "),
#              ("What does mean TU? "),
#              ("How many ears are in human body: "))

# options = (("A. Queen", "B. Baby", "C. PTK", "D. Princess"),
#            ("A. Red+Yello", "B. Green", "C. Pink", "D. Blak"),
#            ("A. 5", "B. 11", "C. 34", "D. 7"),
#            ("A. ThaningGyan", "B. Techanical University", "C. That That", "D. Taung Gyi"),
#            ("A. 5", "B. 1", "C. 2", "D. 0"))

# answers = ("B", "A", "D", "B", "C")

# guesses = []

# score = 0

# question_num = 0

# for question in questions:
#   print("----------------------------------")
#   print(question)
#   for option in options[question_num]:                #<<<<<<< 2d array so we can do options[*****]
#     print(option)

#   guess = input("Enter (A,B,C,D): ").upper()
#   guesses.append(guess)
#   if guess == answers[question_num]:
#     score += 1
#     print("Correct")
#   else:
#     print(f"{guesses[question_num]} is Incorrect")
#     print(f"{answers[question_num]} is the correct answer.")
#   question_num += 1

# print("-------------------")
# print("      RESULT       ")
# print("-------------------")

# print("answers: ", end=" ")
# for answer in answers:
#   print(answer, end=" ")
# print()

# print("guesses: ", end=" ")
# for guess in guesses:
#   print(guess, end=" ")
# print()

# score = (score / len(questions) * 100)
# print(f"Your score is {score}%")

# #_____________________________________________________________________________

# day 8 week 4

# menu = {"apple": 1000,
#         "orange": 1500,
#         "banana": 2000,
#         "coconut": 4000,
#         "pineapple": 3500}

# cart = []

# total = 0

# print("----- MENU -----")

# for key, value in menu.items():
#     print(f"{key:10}: {value:.2f}")

# print()

# while True:
#     foods = input("Select your food (q to quit): ").lower()
#     if foods == "q":
#         break
#     elif menu.get(foods) is not None:
#         cart.append(foods)


# print()
# print("----- Your Food -----")

# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Your total is {total:.2f}")


#_______________________________________________________________________________________

#week 4 day 8 
# number guessing game

# import random

# highest_value = 100
# lowest_value = 1

# answer = random.randint(lowest_value, highest_value)

# guesses = 0
# is_running = True

# print("Welcome Number guessing game.")
# print(f"Select between {lowest_value} and {highest_value}")



# while is_running:
#   guess = input("Enter your number: ")

#   if guess.isdigit():
#     guess = int(guess)
#     guesses += 1

#     if guess < lowest_value or guess > highest_value:
#       print("That number is out of range")
#       print(f"Pls enter the {lowest_value} and {highest_value} again.")
#     elif guess < answer:
#       print("too low.")
#     elif guess > answer:
#       print("too high")
#     else:
#       print("Correct")
#       print("Number of guesses", guesses)
#       print("The answer is ", answer)
#       is_running = False
#   else:
#     print("Invalid typing.")
#     print(f"Pls enter the {lowest_value} and {highest_value} again.")


#_______________________________________________________________________________________

#week 4 day 8
# rock paper scissors game

import random

options = ("rock", "paper", "scissors")
score = 0


running = True


while running:
  player = None
  computer = random.choice(options)
  while player not in options:
    player = input("Enter your guess (rock,paper,scissors): ")

    print("Player:", player)
    print("Computer:", computer)

    if player == computer:
      print("It is a tie.")
    elif player == "rock" and computer == "scissors":
      print("You win")
      score += 1
    elif player == "paper" and computer == "rock":
      print("You win")
      score += 1
    elif player == "scissors" and computer == "paper":
      print("You win")
      score += 1
    else:
      print("You lose")
      score -= 1

    if not input("Wanna play again? (y/n): ").lower() == "y":
      running = False
      
print("Thanks for playing")
print("Your score is:", score)
  