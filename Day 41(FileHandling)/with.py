# # w mode 
# with open('pythonE18.txt','w') as file:
#     file.write('we are using with statement')

# # r mode
# with open('pythonE18.txt','r') as file:
#     display=file.read()
#     print(display)

# # readline
# with open('pythonE18.txt','r') as file:
#     display=file.readline()
#     print(display)

# # readlines
# with open('pythonE18.txt','r') as file:
#     display=file.readlines()
#     print(display)

# with open('pythonE18.txt','r') as file:
#     display=file.readlines()[2]
#     print(display)

# # append
# with open('pythonE18.txt','a') as file:
#     file.write('adding new content using append and with statement')

# # w+
# with open('pythonE18.txt','w+') as file:
#     file.write('New data using with statement')
#     file.seek(0)
#     display=file.read()
#     print(display)

# # r+
# with open('pythonE18.txt','r+') as file:
#     display=file.read()
#     print(display)
#     file.write('using with statement for r+ mode')
#     file.seek(0)
#     display2=file.read()
#     print(display2)

# a+
with open('pythonE18.txt','a+') as file:
    file.write('Using a+ mode')
    file.seek(0)
    display=file.read()
    print(display)