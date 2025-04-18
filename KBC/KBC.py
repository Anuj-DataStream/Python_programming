prize = [0,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,30000000,50000000,70000000]
corr_answer = ["a","c","b","d","b","b","c","d","c","d","c","b","c","a","c"]
answer = ['''

1. International Literacy Day is observed on

    A  Sep 8
   
    B  Nov 28

    C  May 2

    D  Sep 22
''','''

2. The language of Lakshadweep, a Union Territory of India, is

    A  Tamil wrong

    B  Hindi wrong

    C  Malayalam right

    D  Telugu wrong

''','''

3. In which group of places the Kumbha Mela is held every twelve years?

    A  Ujjain, Puri, Prayag, Haridwar

    B  Prayag, Haridwar, Ujjain, Nasik

    C  Rameshwaram, Puri, Badrinath, Dwarika

    D  Chittakoot, Ujjain, Prayag, Haridwar

''','''

4. Bahubali festival is related to

    A  Islam

    B  Hinduism

    C  Buddhism

    D  Jainism

''','''


5. Which day is observed as the World Standards Day?

    A  June 26

    B  Oct 14

    C  Nov 15

    D  Dec 2

''','''

6. Which of the following was the theme of the World Red Cross and Red Crescent Day?

    A  'Dignity for all - focus on women'

    B  'Dignity for all - focus on Children'

    C  'Focus on health for all'

    D  'Nourishment for all-focus on children'

''','''
         

7. September 27 is celebrated every year as

    A  Teachers' Day

    B  National Integration Day

    C  World Tourism Day

    D  International Literacy Day

''','''

8. Who is the author of 'Manas Ka-Hans' ?

    A  Khushwant Singh

    B  Prem Chand

    C  Jayashankar Prasad

    D  Amrit Lal Nagar

''','''

9. The death anniversary of which of the following leaders is observed as Martyrs' Day?

    A   Smt. Indira Gandhi

    B   PT. Jawaharlal Nehru

    C   Mahatma Gandhi

    D   Lal Bahadur Shastri

''','''

10. Who is the author of the epic 'Meghdoot"?

    A  Vishakadatta

    B  Valmiki

    C  Banabhatta

    D  Kalidas

''','''

11. 'Good Friday' is observed to commemorate the event of

    A  birth of Jesus Christ

    B  birth of St. Peter

    C  crucification of Jesus Christ

    D  rebirth of Jesus Christ

''','''

12. Who is the author of the book 'Amrit Ki Ore'?

    A  Mukesh Kumar

    B  Narendra Mohan

    C  Upendra Nath

    D  Nirad C. Choudhary

''','''

13. Which of the following is observed as Sports Day every year?

    A  22nd April

    B  26th July

    C  29th August

    D  2nd October

''','''


14. World Health Day is observed on

    A  Apr 7

    B  Mar 6

    C  Mar 15

    D  Apr 28

''','''

15. Pongal is a popular festival of which state?

    A  Karnataka

    B  Kerala

    C  Tamil Nadu

    D  Andhra Pradesh



''',]
print('''
      ____________________________________________
                    WELCOME TO KBC 
               HERE YOU GET 15 QUESTION 
          PRIZE MONEY IS MENTIONED WITH QUESTION
      ____________________________________________
''')
c=0
for i in range(0,15):
    print(answer[i])
    a=input("ENTER YOUR ANSWER (A,B,C,D) : ")
    if (a.lower()) == corr_answer[i]:
        print("YOUR ANSWER IS CORRECT : " ,corr_answer[i].upper())
        print("\n")
        print("CONGRATULATIONS YOU WON : ", prize[i+1])
        c+=1
    else :
        print("you entered the wrong answer : ", a.upper())
        print("\n")
        print("UNFORTUNATY YOU LOST THE GAME")
        break

print(f'''
      __________________
      THANKS FOR PLAYING
      YOU WON {prize[c]}
      __________________
''')