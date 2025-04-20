from string import *
from random import randint, sample

while True:
    try:
        num = int(input("Enter The Size of The Password     : "))
        special_char = "!@#$%^&*()-_=+"  # Avoid using punctuation for broader compatibility

        if num < 8:
            print("⚠️ For a Strong Password, Minimum 8 Characters Recommended\n")
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

        print(f"\n✅ Your Strong Password is         : {''.join(final_password_list)}\n")

    except Exception as e:
        print("\n🚫 ENTER VALID INPUT\n")
        
    
