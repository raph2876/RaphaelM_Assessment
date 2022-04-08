# The name function is meant to ask the user for a name and store the name.

def welcome():
  print("Hello!")
# this checks if the input is a name with only letters and no spaces. If it is not then it will ask for it to be entered again. If it is a name with only letters, then it will store the name as a variable and continue
  while True:
    n = input("Please enter your name: \n > ")
    if n.isalpha():
      break
    else:
      print("Please enter a name with only letters and no spaces")
  print("Hello, {}! \n Welcome to Raphael's math quiz!".format(n))

welcome()
  


