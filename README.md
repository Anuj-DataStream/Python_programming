
# Python Programming Collection

A collection of Python programs demonstrating various concepts such as games, libraries, and other mini-projects. The repository includes games, a library management system, secret language conversion, and more.

## 🚀 What's Inside?

| Category        | Projects Included |
|----------------|-------------------|
| 🎮 **Games**        | [Guess the Number](#guess-the-number), [Stone Paper Scissors](#stone-paper-scissors), [KBC Game](#kbc-game) |
| 📚 **Library**        | [Library Management System](#library-management-system) |
| 🧠 **Mini Projects** | [Secret Language](#secret-language) |
| 🛠️ **Basic Concepts** | Loops, Conditionals, Functions, etc. |

Each script is written in pure Python and can be executed directly from the terminal or any Python IDE.

---

## 🎮 **Guess the Number Game**

### Description:
A simple game where the player must guess a randomly chosen number between 0 and 100. The program gives feedback on whether the guess is too high or too low and tracks the number of attempts.

### Code:

```python
import random
c = 1
a = random.randint(0, 100)
while a > -1:
    num = int(input("GUESS THE NUMBER : "))
    if a != num:
        if num < a:
            print("SELECT A GREATER NUMBER")
            c += 1
        elif num > a:
            print("SELECT A SMALLER NUMBER")
            c += 1
    else:
        print("YOU GUESSED THE RIGHT NUMBER ")
        print(f"YOU TOOK {c} ATTEMPTS ")
        print(f"NUMBER IS {a}")
        break
```

### How to Run:
1. Download the Python script (`guess_the_number.py`).
2. Open your terminal or Python IDE.
3. Run the script with `python guess_the_number.py`.
4. Follow the on-screen prompts to play!

---

## 🎮 **KBC Game (Who Wants to Be a Millionaire)**

### Description:
A simulation of the popular game show "Who Wants to Be a Millionaire?" with 15 multiple-choice questions. Correct answers lead to increasing prize amounts, and the game ends when a wrong answer is given.

### Code:

```python
prize = [0, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000, 70000000]
corr_answer = ["a", "c", "b", "d", "b", "b", "c", "d", "c", "d", "c", "b", "c", "a", "c"]
answer = ['''
...  # All questions here
''']

print('''
      ____________________________________________
                    WELCOME TO KBC 
               HERE YOU GET 15 QUESTION 
          PRIZE MONEY IS MENTIONED WITH QUESTION
      ____________________________________________
''')
c = 0
for i in range(0, 15):
    print(answer[i])
    a = input("ENTER YOUR ANSWER (A,B,C,D) : ")
    if (a.lower()) == corr_answer[i]:
        print("YOUR ANSWER IS CORRECT : " , corr_answer[i].upper())
        print("
")
        print("CONGRATULATIONS YOU WON : ", prize[i+1])
        c += 1
    else:
        print("you entered the wrong answer : ", a.upper())
        print("
")
        print("UNFORTUNATY YOU LOST THE GAME")
        break

print(f'''
      __________________
      THANKS FOR PLAYING
      YOU WON {prize[c]}
      __________________
''')
```

### How to Run:
1. Download the Python script (`kbc_game.py`).
2. Open your terminal or Python IDE.
3. Run the script with `python kbc_game.py`.
4. Answer the questions and enjoy!

---

## 📚 **Library Management System**

### Description:
A simple Python program that manages a collection of books. You can add books, view them, and count the total number of books in the library. The system can also store the list in a text file.

### Code:

```python
class Library:
    def __init__(self):
        self.list_books = []

    def add(self, inbooks):
        self.list_books.append(inbooks)

    def show(self):
        x = 0
        if len(self.list_books) == 0:
            print("Library is empty")
        for i in self.list_books:
            x += 1
            print(f"{x}.) {i}")

    def count(self):
        return len(self.list_books)

    def addlib(self):
        with open("library.txt", "a+") as file:
            for index, items in enumerate(self.list_books, 1):
                file.write(f"{index}. {items}
")

if __name__ == "__main__":
    print("This will only run if Library_module.py is executed directly.")
```

### How to Run:
1. Download the Python script (`library_module.py`).
2. Add books using the `add()` method.
3. View the list of books with `show()`, or get the total count with `count()`.

---

## 🧠 **Secret Language Conversion**

### Description:
This program encodes and decodes messages using a secret language. Words are either reversed (if their length is less than or equal to 3) or transformed using a random encoding scheme.

### Code:

```python
from random import randint

a = "asdascasdvasdvarubgiqewgbdjsvlsqdasdasdvsnaldsnfkh"
message = input("ENTER YOUR MESSAGE  : ")
task = input("coding/decoding  : ")

list = message.split(" ")
if task.lower() == "coding":
    rev_list = []
    for i in list:
        if len(i) <= 3:
            rev_word = i[::-1]
            rev_list.append(rev_word)
        else:
            b = randint(1, 25)
            c = randint(1, 25)
            rev_word2 = a[b:b+3] + i[1::] + i[0] + a[c:c+3]
            rev_list.append(rev_word2)
    rev_message = " ".join(rev_list)

    print("HERE IS YOUR MESSAGE IN SECRET LANGUAGE :)")
    print("->", rev_message)

elif task.lower() == "decoding":
    nor_list = []
    for k in list:
        if len(k) <= 3:
            nor_word = k[::-1]
            nor_list.append(nor_word)
        else:
            nor_word2 = k[len(k)-4] + k[3:len(k)-4]
            nor_list.append(nor_word2)

    nor_message = " ".join(nor_list)
    print("HERE IS YOUR MESSAGE IN NORMAL LANGUAGE :)")
    print("->", nor_message)
```

### How to Run:
1. Download the Python script (`secret_language.py`).
2. Choose whether you want to **encode** or **decode** a message.
3. Follow the prompts to input the message and the desired task.

---

## 🛠️ Requirements

Most projects don't require external libraries.  
Just make sure you have **Python 3.x** installed.

Run any script using:

```bash
python <filename>.py
```

---

## 🧠 What I Learned

- Python basics: variables, conditionals, loops, functions
- Object-oriented programming with classes
- Working with user input and error handling
- Writing clean, readable code
- File handling (reading and writing to text files)
- Game development and basic algorithms

---

### Contribution
Feel free to fork the repository, make changes, and submit pull requests!
