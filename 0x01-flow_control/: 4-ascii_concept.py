def check(char):
    while True:
        if len(char) > 1:
            print("Not more than one character at a time, try again")
            char = input("Enter a character: ")
        elif not char.isalpha():
            print("Non alphabetical character is not allowed, please try again")
            char = input("Enter a character: ")
        else:
            if ord(char) >= 97 and ord(char) <= 122:
                print(f"The input {char} is a lower case character")
                break
            elif ord(char) >= 65 and ord(char) <= 90:
                print(f"The input {char} is an upper case character")
                break
  
char = input("Enter a character: ")
check(char)
