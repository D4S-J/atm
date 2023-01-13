import os.path

file_exists = os.path.exists('balance.txt')

if file_exists:
    with open('balance.txt', 'w') as balance:
       balance.write("100")


