#The following lines are dedicated to imports
import random
import time

# The Welcome function is meant to ask the user for a name and store the name, then I welcome the player and give them instructions.
def welcome():
  global n
  print("Welcome!")
# This checks if the input is a name with only letters and no spaces. If it is not then it will ask for it to be entered again. If it is a name with only letters, then it will store the name as a variable and continue
  while True:
    n = input(" \n Please enter your name: \n --> ")
    if n.replace(" ", "").isalpha():
      break
    else:
#Error message
      print ("\n")
      print("|!"*18 + "|")
      print("Please enter a name with only letters")
      print("|!"*18 + "|")
#Welcome message
  print("|+-" *19 + "|")
  print("\n Why Hello There, {}! \n Welcome to Raphael's math quiz! \n This is a basic facts quiz that will time you! \n The goal is to answer questions as quickly as posible! \n Please answer the quiz only in integers (whole numbers). \n (disclaimer: This quiz is not intended to offend anyone \n knowingly or unknowingly) \n".format(n))
  print("|+-" *19 + "|")

def start():
#The dictionary of questions
  global questions
  questions = {}
#Sets the scores to 0
  global score
  score = 0
  global high_score
  high_score = 99999999999999999999999999999999999999999
#This generates the questions
  while len(questions) < 20:
#Picks a random integer for both the numbers for the equation
    operators = ["+", "-", "*", "/"]
#Sets the operator to a random operator from the list above
    operator_value = random.choice(operators)
#If the operator is divide, then the program will make sure that the answer is not a recurring number.
    if operator_value == "/":
      int_b = random.randint (1, 12)
      int_a = int_b * random.randint (1, 12)
      question = str(int_a) + " " + str(operator_value) + " " + str(int_b)
    else:
#puts together the non-division question
      int_a = random.randint (1, 12)
      int_b = random.randint (1, 12)
      question = str(int_a) + " " + str(operator_value) + " " + str(int_b)
#Creates the answer to the question
    answer = round(eval(question))
#Adds a question mark to the question the player will read
    question += "? "
#Adds the questions to the dictionary and assigns the answer to it
    questions.update({question : str(answer)})

def quiz():
#Asks the player if they want to start the quiz. All they need to do it press enter
  input ("\n Please press enter when you are ready! ")
  #Measures time since epoch
  start_time = time.time()
#Repeats for the number of keys in the dictionary
  global questions
  for q in questions.keys():
    user_answer = input("\n What is " + q + "\n --> ")
#If the answer to the question is equal to the user answer, then add a point and say that the user is correct. If not, then tell them they are incorrect and give the correct answer.
    if questions.get(q) == str(user_answer).replace(" ", ""):
      global score
      score += 1
      print ("\n")
      print ("|+" *7 + "|")
      print ("You are correct!")
      print ("|+" *7 + "|")
    else:
      print ("\n")
      print ("|-" * 18 + "|")
      print("Incorrect. The correct answer was {}".format(questions.get(q)))
      print ("|-" * 18 + "|")
#measures time since epoch again
  end_time = time.time()
#subtracts the start time from the end time to measure how long the player took to complete the quiz
  final_time = round(end_time - start_time)
#If the player scored something, then their score will be shown
  if score > 0:
    final_score = round(final_time / score)
    print("\n" + "|+-" *16 + "|")
    print("Congratulations, " + str(n) + "! \nYou got " + str(score) + " right!")
    print ("You took " + str(final_time) + " seconds to get " + str(score) + " questions correct!")
    print ("On average, you took " + str(final_score) + " seconds per correct answer!")
#If the player achieved a new high score, then it will update
    global high_score
    if final_score < high_score:
      high_score = final_score
      print("You got a new high score!")
    else:
      print("Your current high score is " + str(high_score) + " seconds per correct answer!")
    print("|+-" *16 + "|")
#If the player got 0 points they will recieve a different message
  else:
    print("\n" + str(n) + ", you did not get anything correct... \n Don't worry about it though! \n You can always do this quiz again! \n I know you will do better next time!")

def customize():
  while True:
    try:
#Ask the user to enter a difficulty
      difficulty = input("\nWhat would you like the difficulty set to? \n(the number you enter will be the the maximum number \nthat is added, subtracted from or multiplied by in the quiz) \nMinimum number is 4 \n--> ")
#If the difficulty is larger than 0, there will be an error message, and if the difficulty is not an integer, there will also be an error message
      difficulty = int(difficulty)
      if difficulty > 4:
        break
      else:
        print("\n")
        print("|!" * 21 + "|")
        print("Please answer with a number larger than 4")
        print("|!" * 21 + "|")

    except ValueError:
      print("\n")
      print("|!" * 21 + "|")
      print("Please enter a valid integer (full  number)")
      print("|!" * 21 + "|")
  print("Great!")
  #The dictionary of questions
  global questions
  questions = {}
  score = 0
#This generates the questions
  while len(questions) < 20:
#Picks a random integer for both the numbers for the equation
    operators = ["+", "-", "*", "/"]
#Sets the operator to a random operator from the list above
    operator_value = random.choice(operators)
#If the operator is divide, then the program will make sure that the answer is not a recurring number.
    if operator_value == "/":
      int_b = random.randint (1, int(difficulty))
      int_a = int_b * random.randint (1, int(difficulty))
      question = str(int_a) + " " + str(operator_value) + " " + str(int_b)
    else:
#puts together the non-division question
      int_a = random.randint (1, int(difficulty))
      int_b = random.randint (1, int(difficulty))
      question = str(int_a) + " " + str(operator_value) + " " + str(int_b)
#Creates the answer to the question
    answer = round(eval(question))
#Adds a question mark to the question the player will read
    question += "? "
#Adds the questions to the dictionary and assigns the answer to it
    questions.update({question : str(answer)})
#do the quiz again
  quiz()
#do the customisation phase again
  customize()
    
welcome()
start()
quiz()
customize()