import termcolor
import pwinput

import hashlib
import shelve
import time
import os

db = shelve.open('db-users')

def exists(username):
  if username in db.keys():
    return True
  return False

def login(username, password):
  user = db[username]
  hash = hashlib.md5(password.encode('utf-8')).hexdigest()
  if hash != user['password']:
    print(f'''
          {termcolor.colored('Error: Incorrect password.', 'red')}
          Returning to login screen in 3 seconds.''')
    time.sleep(3)
    return False
  print(f'''
          {termcolor.colored('Login successful! Loading...', 'green')}
          ''')
  time.sleep(3)
  os.system('clear')
  print(f'''
          ======================
          Welcome, {termcolor.colored(user['username'], 'green')}.
          ======================

          {termcolor.colored('Home Address:', 'cyan')} {user['home_address']}
          {termcolor.colored('Favourite Colour:', 'cyan')} {user['fav_colour']}
          {termcolor.colored('Favourite Animal:', 'cyan')} {user['fav_animal']}
        ''')
  input('''
          Press [ENTER] to logout.''')
  return True

def main():
  os.system('clear')
  quit = False
  while quit != True:
    os.system('clear')
    print('''
          ======================
          Welcome, please login.
          ======================''')
    username = input('''
          Username: ''')
    if username == 'quit':
      db.close()
      print(f'''
          {termcolor.colored('Shutting down. Goodbye.', 'magenta')}
          ''')
      time.sleep(3)
      os.system('clear')
      quit = True
      continue
    if not exists(username):
      print(f'''
          {termcolor.colored('Error: User not found.', 'red')}
          Returning to login screen in 3 seconds.''')
      time.sleep(3)
      continue
    password = pwinput.pwinput(prompt='''
          Password: ''')
    login(username, password)

main()
