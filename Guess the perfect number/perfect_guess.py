import random
c=1
a=random.randint(0,100)
while a>-1:
    num=int(input("GUESS THE NUMBER : "))
    if a!=num :
        if num<a:
            print ("SELECT THE GREATER NUMBER")
            c+=1
    
        elif num>a:
            print("SELECT THE SMALLER NUMBER")
            c+=1

    else:   
        print("YOU GUESSED THE RIGHT NUMBER ")
        print(f"YOU TOOK {c} ATTEMPTS ")
        print(f"NUMBER IS {a}")
        break
    




