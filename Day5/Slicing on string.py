#slicing on string
#Step value
msg='education'
print(msg[::])
print(msg[::1])
print(msg[::2])
print(msg[::3])
print(msg[::4])

#start & end index
msg='education'
print(msg[1:6:1])
print(msg[4:20:1])

#empty string
msg='education'
print(msg[6:2:1])

#even digit characters in forward direction
msg='education'
print(msg[0::2])

#odd digit characters in forward direction
msg='education'
print(msg[1::2])

#reverse of string
msg='python'
print(msg[::-1])
#or
msg='python'
print(msg[-1:-9:-1])

#even digit characters in backward direction
msg='education'
print(msg[-2::-2])

#odd digit characters in backward direction
msg='education'
print(msg[-1::-2])


string='welcome to python class'
#-----------------------------------
#Part 1:Positive Slicing
#-----------------------------------
print(string[0:7])       #welcome
print(string[8:10])      #to
print(string[11:17])     #python
print(string[18:23])     #class
print(string[0:11])      #welcome to
print(string[11:23])     #python class
print(string[3:9])       #come t
print(string[5:15])      #me to pyth
print(string[:7])        #welcome
print(string[8:])        #to python class

#------------------------------------
#Part 2:Negative Slicing
#------------------------------------
string='welcome to python class'
print(string[-5::])         #class
print(string[-12:-6:])      #python
print(string[-23:-16])      #welcome
print(string[-15:-13])      #to
print(string[-11:-7])       #ytho
print(string[-23:-1])       #welcome to python clas
print(string[:-6])          #welcome to python
print(string[-6:])          # class
print(string[-10:-5])       #thon

#-------------------------------------
#Part 3: Reversing
#-------------------------------------
string='welcome to python class'
print(string[::-1])        #ssalc nohtyp ot emoclew
print(string[22::-1])      #ssalc nohtyp ot emoclew
print(string[16:10:-1])    #nohtyp
print(string[-1:-6:-1])    #ssalc
print(string[9::-1])       #ot emoclew