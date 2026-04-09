# To write content
file=open('pythonE18.txt','w')
content=file.write('Welcome to python class')
file.close()

# For read
file=open('pythonE18.txt','r')
display=file.read()
print(display)
file.close()

# For append
file=open('pythonE18.txt','a')
content=file.write('\n we are adding new data')
file.close()

# For r+ using seek method
file=open('pythonE18.txt','r+')
content=file.write('we are using r+ mode to add new data')
file.seek(0)
display=file.read()
print(display)
file.close()

# Or without using seek method
file=open('pythonE18.txt','r+')
content=file.write('we are using r+ mode to add new data')
file.close()

file=open('pythonE18.txt','r+')
display=file.read()
print(display)
file.close()

# For w+
file=open('pythonE18.txt','w+')
content=file.write('we are using w+ mode to add new data')
file.seek(0)
display=file.read()
print(display)
file.close()

# For a+
file=open('pythonE18.txt','a+')
content=file.write('\nAppending nwe data using a+ mode')
file.seek(0)
display=file.read()
print(display)
file.close()

# For tell method
file=open('pythone18.txt','r')
display=file.read()
print(display)
position=file.tell()
print(f'Position of cursor is:{position}')
file.close()