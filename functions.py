# Sign Up
def signup(usernames, passwords):
  username = input('Enter the Name:')
  password = input('Enter the Password:')

  usernames.append(username)
  passwords.append(password)

  print('-- SignUp Successfully--')

# Login
def login(usernames, passwords):
  user_name = input('Enter the Username:')
  pass_word = input('Enter the password')

  if user_name in usernames and pass_word in passwords:
    print("--- Login Successfully ---")
  else:
    print("-- Try Again --")