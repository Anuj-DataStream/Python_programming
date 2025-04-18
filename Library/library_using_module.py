from Library_module import *

print('''
           __________________________________________________________
                         HELLO WELCOME TO LIBRARY
            PROGRAM CAN ADD AND COUNT THE NUMBER OF BOOKS IN LIBRARY
           __________________________________________________________
''')
num_books=int(input("HOW MANY BOOKS YOU WANT TO ADD IN LIBRARY"))
library_inter=library()
for i in range(num_books):
    c=input("ENTER THE BOOK :  ")
    library_inter.add(c)
print("\n")
a=input('''
        IF YOU WANT TO SEE HOW MANY ARE THERE IN YOUR LIBRARY TYPE     :  count
        IF YOU WANT TO SEE THE NAME OF THE BOOK IN YOUR LIBRARY TYPE   :  show 
                                                                       :  ''')

if a.lower() == "show":
    library_inter.show()

elif a.lower() == "count":
    print(f'''
      NUMBER OF BOOKS IN YOUR LIBRARY ARE {library_inter.count()}''')

else:
    print("ENTER VALID WORK")

if library_inter.count() == num_books:
    print("\n\n\n\n              PROGRAM IS PERFECT")
    library_inter.addlib()
else:
    print("THERE IS SOMETHING WRONG")

