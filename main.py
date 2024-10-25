
from functions import login, signup

usernames = []
passwords = []

while True:
  print('1. Sign Up:')
  print('2. Login:')
  option = int(input("Select the Option:"))

  if option == 1:
    signup(usernames, passwords)
    continue
  elif option == 2:
    login(usernames, passwords)
    break
  else:
    print('-- Try Again --')