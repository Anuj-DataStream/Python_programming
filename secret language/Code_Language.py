from random import randint

#rules if length of word is equal to 3 or less just reverse it 
#else remove first alphabet and append it in end and add 3 random alphabet in start and end 

print('''
            THIS PROGRAM HELPS YOU TO COVERT YOUR MESSAGE IN SECRET LANGUAGE
''')
a="asdascasdvasdvarubgiqewgbdjsvlsqdasdasdvsnaldsnfkh"

message = input("ENTER YOUR MESSAGE  : ")

task = input("coding/decoding  : ")
list = message.split(" ")
if task.lower() == "coding":
    rev_list = []
    for i in list:
        if len(i) <= 3:
            rev_word=i[::-1]
            rev_list.append(rev_word)
        else:
            b=randint(1,25)
            c=randint(1,25)
            rev_word2 =a[b:b+3]+i[1::]+i[0]+a[c:c+3]
            rev_list.append(rev_word2)
    rev_message = " ".join(rev_list)

    print('''
                    HERE IS YOUR MESSAGE IN SECRET LANGUAGE :)
    ''')
    print("->",rev_message)

elif task.lower() == "decoding":
    nor_list=[]
    for k in list:
        if len(k) <=3 :
            nor_word=k[::-1]
            nor_list.append(nor_word)
        else:
            nor_word2 = k[len(k)-4]+k[3:len(k)-4]
            nor_list.append(nor_word2)

    nor_message = " ".join(nor_list)
    print('''
                    HERE IS YOUR MESSAGE IN NORMAL LANGUAGE :)
    ''')
    print("->",nor_message)