
# Python Programming Collection

A collection of Python programs demonstrating various concepts such as games, libraries, and other mini-projects. The repository includes games, a library management system, secret language conversion, and more.

## 🚀 What's Inside?

| Category        | Projects Included |
|----------------|-------------------|
| 🎮 **Games**        | [Guess the Number](#guess-the-number), [Stone Paper Scissors](#stone-paper-scissors), [KBC Game](#kbc-game) |
| 📚 **Library**        | [Library Management System](#library-management-system) |
| 🧠 **Mini Projects** | [Secret Language](#secret-language), [Password Generator](#password-generator) |
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

## 🧩 **Password Generator**

### Description:
A Python program that generates strong passwords with uppercase and lowercase letters, numbers, and special characters. The password length can be customized, and the program ensures randomness and strength.

### Code:

```python
from string import *
from random import randint, sample

while True:
    try:
        num = int(input("Enter The Size of The Password     : "))
        special_char = "!@#$%^&*()-_=+"  # Avoid using punctuation for broader compatibility

        if num < 8:
            print("⚠️ For a Strong Password, Minimum 8 Characters Recommended
")
            continue

        unq_num = sample(range(0, num), num)  # unique shuffled indexes

        def get_unqiue_number():
            return unq_num.pop() if unq_num else None

        password = []

        # Fill with uppercase and lowercase letters
        for i in range(0, num - int(num / 2) - 2):
            password.insert((2 * i + 1), ascii_lowercase[randint(0, 25)])
            password.insert(2 * i, ascii_uppercase[randint(0, 25)])

        # Fill with numbers
        for j in range(num - int(num / 2) + 3, num):
            password.insert(2 * j + 1, str(randint(0, 4)))  # convert to string
            password.insert(2 * j, str(randint(5, 9)))      # convert to string

        # Add one special character
        for k in range(num - 1, num):
            password.insert(k, special_char[randint(0, len(special_char) - 1)])

        # Build final password using unique indexes
        final_password_list = []
        for l in range(0, num):
            a = get_unqiue_number()
            if a is not None and a < len(password):
                final_password_list.insert(l, str(password[a]))

        print(f"
✅ Your Strong Password is         : {''.join(final_password_list)}
")

    except Exception as e:
        print("
🚫 ENTER VALID INPUT
")
```

### How to Run:
1. Download the Python script (`password_generator.py`).
2. Enter the desired password length when prompted.
3. A strong password will be generated and displayed.

---

## 🧩 Requirements

Most projects don't require external libraries.  
Just make sure you have **Python 3.x** installed.

Run any script using:

```bash
python <filename>.py
```

# 🔳 QR Code Generator

A simple Python script that lets you generate QR codes from any URL or text and save them as PNG files.

## 📦 Features

- Input any URL or text
- Automatically appends `.png` extension if not provided
- Clean black-and-white QR code image generation

## ▶️ How to Run

1. Install the required package:
```bash
pip install qrcode[pil]
```

2. Run the script:
```bash
python QR_code_generator.py
```

3. Follow the prompts to enter the URL/text and file name.

## 🧠 Example

```bash
Enter the URL    : https://github.com/
Enter the file name   : github_qr
QR code is saved in github_qr.png
```

## 💡 Dependencies

- `qrcode` for QR code generation
- `pillow` (automatically installed with `qrcode[pil]`)

## 🧩 About the Script

This Python script uses the `qrcode` library to generate QR codes. It takes a URL or any text input from the user, creates a corresponding QR code, and saves it as a PNG image. If the filename provided by the user does not end with `.png`, the script automatically appends it.

### Example Usage

```python
import qrcode

data = input("Enter the URL    :").strip()
filename = input("Enter the file name   :").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
if not filename.lower().endswith(".png"):
    filename += ".png"
image.save(filename)

print(f"QR code is saved in {filename}")
```

---

## 💻 Requirements

- **Python 3.x**
- **qrcode** library
- **pillow** library (for image processing)

To install all dependencies, run:

```bash
pip install qrcode[pil]
```


## 🧠 What I Learned

- Python basics: variables, conditionals, loops, functions
- Object-oriented programming with classes
- Working with user input and error handling
- Writing clean, readable code
- File handling (reading and writing to text files)
- Game development and basic algorithms
- Python basics: working with libraries, user input, and file handling
- How to generate QR codes with Python
- Error handling and extension management in file names

---

### Contribution
Feel free to fork the repository, make changes, and submit pull requests!
