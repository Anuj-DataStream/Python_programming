import random
    
g=int(input("HOW MANY ROUND YOU WANT TO PLAY"))
k=0
l=0
m=0
while g>k:
    a=[1,2,3]
    b=int(input('''
                ___________________________________
                BASIC INTRUCTIONS
                ___________________________________
                PLEASE SELECT STONE ,PAPER ,SCISSOR
                for stone   : press 1
                for paper   : press 2
                for scissor : press 3
                ___________________________________
                SELECT AS PER INTRUCTIONS:'''))
    comp = random.randint(0,2)
    comp1=a[comp]
    d={1:"stone",2:"paper",3:"scissor"}
    e=d.get(comp1)
    if b==comp1 :
        print(f"\nCOMPUTER SELECTED {e} \nITS A TIE")
    elif (comp1==1 and b==3) or (comp1==2 and b==1) or (comp1==3 and b==2):
        print(f"\nCOMPUTER SELECTED {e} \nYOU LOST ")
        l+=1

    elif(comp1==1 and b==2) or (comp1==2 and b==3) or (comp1==3 and b==1):
        print(f"\nCOMPUTER SELECTED {e} \nYOU WON")
        m+=1
    else:
        print("DUMB HUMAN SEE INTRUCTIONS")
        g+=1
    k+=1

print(f'''
      

      TOTAL ROUNDS             :{g}
      NUMBERS OF TIES          :{g-l-m}
      PLAYER         :SCORE
      COMPUTER       :{l}
      YOU            :{m}
''')
if l>m:
    print("COMPUTER WON\nYOU LOSE")
elif l==m:
    print("NOBODY WON\nITS A DRAW")
else:
    print("COMPUTER LOSE\nYOU WON")


