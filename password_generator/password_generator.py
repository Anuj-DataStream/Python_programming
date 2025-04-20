from string import *
from random import randint,sample
# c=0
while True:  
    try:
        num = int(input("Enter The Size of The Password     :"))
        special_char = "!@#$%^&*()-_=+" #used this for making password strong and usable not use punctuation because it has all special character which create issues
        unq_num = sample(range(0,num),num)
        def get_unqiue_number():
            if unq_num:
                return unq_num.pop()
            else:
                return None
        if num<8:
            print("\nFor a Strong Password Minimum 8 Characters\n")
        else:
            password = []

            for i in range(0,num-int(num/2)-2):
                password.insert((2*i+1),ascii_lowercase[randint(0,25)])
                password.insert(2*i,ascii_uppercase[randint(0,25)])
            for j in range(num-int(num/2)+3,num):
                password.insert(2*j+1,randint(0,4))
                password.insert(2*j,randint(5,9))   

            for k in range(num-1,num):
                password.insert(k,special_char[randint(0,len(special_char))])
            final_password_list = []
            for l in range(0,num+1):
                a=get_unqiue_number()
                if a==None:
                    break
                else:
                    final_password_list.insert(l,str(password[int(a)]))
            print(f"Your Strong Password is            :{''.join(final_password_list)}")
    except Exception as e:
        print('''
              ENTER VALID INPUT
              ''')
