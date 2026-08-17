# Problem: Create a Mad Libs game by filling in blanks with words provided by the user
# Approach: Using input(), variables, string formatting with f-strings, and user-provided words to create a story.

# Madlibs game
# word game where your create a story by filling the blanks with random words


adjective1 = input("Enter an adjective(description): ")
noun1 = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective(description): ")
verb1 = input("Enter a verb ending with 'ing' :")
adjective3 = input("Enter an adjective(description): ")


print(f"Today I went to a {adjective1} zoo")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

