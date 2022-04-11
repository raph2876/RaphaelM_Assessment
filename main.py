# The name function is meant to ask the user for a name and store the name.

def welcome():
  print("Hello!")
# this checks if the input is a name with only letters and no spaces. If it is not then it will ask for it to be entered again. If it is a name with only letters, then it will store the name as a variable and continue
  while True:
    n = input(" \n Please enter your name: \n --> ")
    if n.isalpha():
      break
    else:
#Error message
      print("|!"*26 + "|")
      print("Please enter a name with only letters and no spaces")
      print("|!"*26 + "|")
#Welcome message
  print("|+-" *28 + "|")
  print("\n Hello, {}! \n Welcome to Raphael's math quiz! \n This is a basic facts quiz that is on a time limit! \n The goal of this is for you to answer questions as quickly as posible! \n Please answer only in integers (whole numbers). \n (disclaimer: This quiz is not intended to offend anyone knowingly or unknowingly) \n".format(n))
  print("|+-" *28 + "|")

welcome()
