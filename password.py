
import random
print("Create a random password\n")


alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q","r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [1, 2, 3, 4, 5, 6, 7,8 , 9 , 0]
symbols = ["!", "@", "#", "$", "%", "^", "&","*", "(", ")", ",", ".","/", "[", "]","{", "}"]
bigAlphabets = []
for alphabet in alphabets:
    bigAlphabet = alphabet.upper()
    bigAlphabets.append(bigAlphabet)

num_alphabets = int(input("amount of small letters you want in password: "))
num_bigAlphabets = int(input("amount of big alphabets you want in password: "))
num_numbers = int(input("amount numbers you want in password: "))
num_symbols = int(input("amount symbols you want in password: "))


def created_pass():
    from_alphabet = random.choices(alphabets, k=num_alphabets)
    from_numbers = random.choices(numbers, k=num_numbers)
    from_symbols = random.choices(symbols, k=num_symbols)
    from_bigAlphabets = random.choices(bigAlphabets, k=num_bigAlphabets)
    
    initially_generated_password = from_alphabet + from_numbers + from_symbols + from_bigAlphabets
    
    random_initial_password = random.choices(initially_generated_password, k=len(initially_generated_password))
    
    string_password = [str(element) for element in random_initial_password]
    
    final_password = ''.join(string_password)
    print(final_password)
    print(f"Total length = {len(final_password)}")

confirmation = input("\nEnter y to continue: ")

if confirmation.lower() == "y":
    created_pass()

else:
    print("Cannot generate password")