print("Welcome to my quiz game")

Playing = input("Do you wanna PLay?  ")
Score = 0

if Playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")    

q1 = input("what does cpu stands for?    " )
if q1.lower() == "central processing unit":
    print("Correct")
    Score += 1
else: 
    print("Incorrect")    

q2 = input("what does gpu stands for?    " )
if q2.lower() == "graphical processing unit":
    print("Correct")
    Score += 1
else: 
    print("Incorrect") 

q3 = input("what does RAM stands for?    " )
if q3.lower() == "random access memory":
    print("Correct")
    Score += 1
else: 
    print("Incorrect") 

q4 = input("what does k8s stands for?    " )
if q4.lower() == "kubernetes":
    print("Correct")
    Score += 1
else: 
    print("Incorrect") 

q5 = input("what does LB stands for?    " )
if q5.lower() == "load balancer":
    print("Correct")
    Score += 1
else: 
    print("Incorrect")  

print("You got " + str(Score) + " points")    
print("You got " + str((Score/5)*100) + "%")    
