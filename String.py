str='HasanAli'
a=str[7]
print(a)

b=str[0:9]
print(b)

c=str[::-1]
print(c)

str="".join(reversed(str))
print(str)

#convert str into list and update character
list1=list(str)
list1[2]='m'
print(list1)
str2=''.join(list1)
print(str2)

str3='qwertyuiop'
list3=list(str3)
print(list3)
list3[6]='X'
print(list3)
str4=''.join(list3)
print(str4)

#del a character from string
a='PUCIT.EDU.PK'
print(a)
b=a[0:4]+a[5::]
print(b)


#formatting of string
x="{} {} {}".format("PUCIT" , "EDU" , "PK")
print(x)

y="{1} {0} {2}".format("PUCIT" , "EDU" , "PK")
print(y)

z="{l} {g} {h}".format(l="PUCIT" , g="EDU" , h="PK")
print(z)

q="{0:b}".format(100)  #binary conversion
print(q)
w="{0:e}".format(123.647) #exponentional conversion
print(w)
e="{0:.2f}".format(2/55)  #round_off
print(e)
