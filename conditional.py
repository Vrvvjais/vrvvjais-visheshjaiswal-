a=int(input("Enter your age: "))

if(a>=18):
    print("your now a adult ")
    print("Now make a document by Goverment")
elif(a<0):
    print("your are entering a invalid age")
elif(a==0):
    print("Your are entering 0 which is a invalid age")
else:
    print("Your are below the age of adult")

a1=int(input("enter number 1: "))
a2=int(input("enter number 2: "))
a3=int(input("enter number 3: "))
a4=int(input("enter number 4: "))

a1= int(input("Enter your number: "))
a2= int(input("Enter your number: "))
a3= int(input("Enter your number: "))
a4= int(input("Enter your number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1: ", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2: ", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3: ", a3)
elif(a4>a2 and a4>a3 and a4>a1):
    print("Greatest number is a4: ", a4)

marks1=int(input("Enter the marks 1:"))
marks2=int(input("Enter the marks 2:"))
marks3=int(input("Enter the marks 3:"))

total_percentage=(100*(marks1 + marks2 + marks3))/300
print(total_percentage)

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed", total_percentage)

else:
    print("You are failed, try again next year.", total_percentage)
P1 = "Make a lot of money"
P2= "buy now"
P3="subscribe this"
P4="click this"

message= input("Enter your comment: ")

if((P1 in message) or (P2 in message) or (P3 in message) or (P4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a span")

username= input("Enter your name")

if(len(username)<10):
    print("your username contians less than ten number. ")

else:
    print("your username contains good amounnt of characters.")

Lists= ["Vishesh", "Vijay", "Rinku", "Vanshika"]

name = input("Enter your name: ")

if(name in Lists):
    print("your name is in the lists")
    
else: 
    print("Your name is not in the lists")

marks= int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade= "A++"
if(marks<=90 and marks>=80):
    grade= "A+"
if(marks<=80 and marks>=70):
    grade= "A"
if(marks<=70 and marks>=60):
    grade= "B"
if(marks<=60 and marks>=50):
    grade= "C"
if(marks<=50 and marks>=40):
    grade= "D"

print("Your grade is :", grade)

post = input('Enter your post: ')

if("Vishesh" in post):
    print("The psot is talking about Vishesh")

else:
    print("this post is not talking about Vishesh")