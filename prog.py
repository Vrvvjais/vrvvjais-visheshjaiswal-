import time

timestamp= time.strftime("%H:%M:%S")
print(timestamp)

h=int(time.strftime("%H"))
n=input("Enter your name: ")

if(4>=h<12):
    print("Good Morning",n.capitalize(),"its",timestamp)
elif(12>=h<17):
    print("Good Afternoon",n.capitalize(),"its",timestamp)
elif(17>=h<19):
    print("Good Evening",n.capitalize(),"its",timestamp)
else:
    print("Good Night",n.capitalize(),"its",timestamp)

