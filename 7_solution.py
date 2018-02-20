# Basic file processing 
try:
    with open('filename','r') as f:
        print(f.read())
except IOError:
    print("No such file exists")
