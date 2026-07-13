import random
import string

# Function to generate password
def generate_password(length):
    characters = (
        string.ascii_letters +     
        string.digits +             
        string.punctuation        
    )

    password = "".join(random.choice(characters) for _ in range(length))
    return password

 

print("===== Password Generator ======")

length = int(input("Enter the desired password length: "))

if length <= 0:
    print("Password length must be greater than 0.")

else:
    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)