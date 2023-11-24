import os

name = input("Enter name: ")
file = open(name+".bat","a")
all = (name+".bat")

file.write('''%0|%0
''')
print("Created in your current directory")
