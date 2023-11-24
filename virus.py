import os

name = input("Enter name: ")
file = open(name+".py","a")
all = (file+".py")

file.write('''
import os
os.system("start")
''')

os.system("pip install pyinstaller")
os.system(f"pyinstaller --onefile -w {all}")
print("Created virus!")
print("The exe version and py version of your virus are in the directory!")
