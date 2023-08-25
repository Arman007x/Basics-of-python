
##---------Types of vlaue-----------------

int(21)
str("Arman")
float(3.1416)
bool()

##----------------------------------------

##---------sum of int---------------------

a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
sum = a + b 
print("The sum is :" , sum)

##----------------------------------------
##----------------------------------------
name = "Arman"

print(name)
print(name.upper())
print(name.lower())
print(name.find('n'))
print(name.replace("Arman","Avengers"))
print(name.replace("n","s"))
##---------------------------------------
##----------------Short cuts-----------------------

i =5  
i = i+2 # =7
i += 2 # =7
i -= 2
i *= 2 # =14 # i = i*2

##--------operators precedence---------

result = 2 + 3 * 5 ## 3*5={}+2
print(result)

##----------Comparison Operators--------

print(3>2) # true
print(3<2) # false
print(3>=2)
print(3<=2) #(< + =)
print(3==2)
print(3!=2) # (! + =)

##-------Logical Opertors--------------

print(2 > 3 or 2 > 1) # true
print(2 > 3 and 2 > 1) # f
print(2 < 3 and 2 > 1) # t 
print(not 2 < 3) #f
print(not 2 > 3) #t

##-------If - Else-----------------------

age = 19

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
    
print("Thank You")

#-------
#You are an adult.
#You can vote.
#Thank You
#-------

age = 16

if age >= 18:
    print("You are an adult.")
    print("You can vote.")

elif age < 18 and age > 3:
    print("You are in school.")

else:
    print("You are a Child.")
print("Thank You")

#----
You are in school.
Thank You
#----

#--------Mini Project Calculator--------------

first = int(input("Enter the first number :"))
operator = input("Enter operator(+,-,*,/,%) :")
second = int(input("Enter the second number :"))

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second) 
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")
    
    
##---------Range-------------
numbers = range(5)
print(numbers)

##---------------Loops---------------------
#------While-------
i = 1
while i <=100:
    print(i)  # print(i * "*")
    i = i+1
#------Reverse---------  
i = 5
while i >= 0:
    print(i)  # print(i * "*")
    i = i-1  
    
    
#------for-------------
for i in range(5):
    print(i + 1)  # print(i) = 0 1 2 3 4
    
##------------------List---------------------------

marks = [93,87,77, "Arman"]
print(marks)  # print(marks[0]) # print(marks[-1]) {Reverce count} # print(marks[0:2]) 

#--------For loop in list-----------

marks = [93,87,77, "Arman"]
for score in marks:
    print(score) 
    
# Append

marks.append(68)
print(marks)

# insert

marks.insert(0,97)
print(marks)

# check

marks.insert(0,97)
print(93 in marks)

# How much elements

print(len(marks))

#--------while in list --------

marks = [93,87,77, "Arman"]

i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1
    
# clear list

marks.clear()
print(marks)


##--------------------Break & Continue------------------
# Break
students = ["Arman","Jubeyar","Istiak","Israt","Ikra","joly"]

for student in students:
    if student == "Israt":
        break;
    print(student)
    
# Continue

students = ["Arman","Jubeyar","Istiak","Israt","Ikra","joly"]

for student in students:
    if student == "Israt":
        continue;
    print(student)    
    
## ------------------Tuple (Unchangable) ---------------------

# Error!
marks = (95,98,97)
marks[0]=99     # Error!

# Count same 
print(marks.count(97)) # = 3 

# Index
print(index.count(97)) # = 2

# set

marks = {95,98,97,97,97}
print(marks)

# Index doesn't works in set.

marks = {95,98,97,97,97}
for score in marks:
    print(score) 

#---------------Dictionary--------------------

marks = {"Chemistry" : 93,"Biology" : 87}
print(marks["Chemistry"])

# Add
marks["Physics"] = 77;
print(marks)

# Change value
marks["Physics"] = 78;
print(marks)


#-------------------FUNCTIONS--------------------------

1. In-Built Functions = int , str 
2. Module Functions = math 
3. User-Defined Functions


# 2 
import math
a = math.sqrt(16)
print(a)







