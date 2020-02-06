from black_py import *
from __versioninfo__ import version

def shell():
  print('Welcome To Black Python', version + ',')
  print('Type "help()" for help.')
  while 1:
    x = input(">>> ")
    if x == 'exit':
      break

    try:
      y = eval(x)
      if y: print(y)
    except:
      try:
        exec(x)
      except Exception as e:
        print("Error:", e)