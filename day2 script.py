import random   # to pick random characters
import string   # to use ready-made sets of letters, numbers, and symbols

# Run the program again and again until user decides to exit
while True:
    # ---- Step 1: Take password length from user ----
    length = int(input("\n👉 Enter the length of your password (minimum 4): "))

    # ---- Step 2: Check if length is valid ----
    if length < 4:
        print("❌ Password length must be at least 4 to make it strong.")
        continue   # Go back to the beginning of the loop

    # ---- Step 3: Define character sets ----
    uppercase = string.ascii_uppercase   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    lowercase = string.ascii_lowercase   # abcdefghijklmnopqrstuvwxyz
    digits = string.digits               # 0123456789
    symbols = string.punctuation         # !@#$%^&*()_+ and many more

    # ---- Step 4: Put all characters together ----
    all_characters = uppercase + lowercase + digits + symbols

    # ---- Step 5: Start building the password ----
    # First, we add at least 1 uppercase, 1 lowercase, 1 digit, and 1 symbol
    password = [
        random.choice(uppercase),  
        random.choice(lowercase),  
        random.choice(digits),     
        random.choice(symbols)     
    ]

    # ---- Step 6: Fill the rest of the password ----
    # Example: If user wants 10 characters, 4 are already added above,
    # now we add the remaining 6 from all characters
    for i in range(length - 4):
        password.append(random.choice(all_characters))

    # ---- Step 7: Shuffle the characters ----
    # This makes sure the password is not in a fixed order (like always UPPER → lower → digit → symbol)
    random.shuffle(password)

    # ---- Step 8: Convert list into a string ----
    final_password = "".join(password)

    # ---- Step 9: Show the generated password ----
    print("✅ Your Strong Password is:", final_password)

    # ---- Step 10: Ask if the user wants another password ----
    choice = input("\nDo you want to generate another password? (yes/no): ").lower()

    # If the answer is "no", "n", "exit" or "quit", then stop the loop
    if choice in ["no", "n", "exit", "quit"]:
        print("👋 Exiting... Stay safe and protect your accounts with strong passwords!")
        break   # End the program
