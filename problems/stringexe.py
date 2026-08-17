# Problem: validate user input exercise
# 1. username is not more then 12 characters
# 2. username must not contin spaces
# 3. username must not contain digits

# Approach: Using len(), find(), isalpha(), and if-elif-else statements to validate the user's input.

username =  input("Enter a username:  ")


if len(username) > 12:
    print("Your username can't be more then 12 characters")
elif not username.find(" ") == -1:   #if there is no space then result is -1 but if there is space the reuslt will be something else but not -1 therefore if the reult is not -1 we found a space
    print(f"Your username can't contain spaces")    
elif not username.isalpha(): # .isalspha is only true when there are only alphabets
    print("Your username must not contain digits")
else:
    print(f"Welcome! {username}")
