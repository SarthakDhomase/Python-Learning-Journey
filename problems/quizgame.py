# Problem: Create a quiz game
# Approach: 

questions = ("What is the capital of India?",
             "How many days are there in a week?",
             "Which planet is known as the Red Planet?",
             "How many legs does a spider have?",
             "What is 5 + 3?",)

options =  (("A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"),
            ("A) 5", "B) 6", "C) 7", "D) 8"),
            ("A) Earth","B) Mars","C) Jupiter","D) Venus"),
            ("A) 6","B) 8","C) 10","D) 12"),
            ("A) 6","B) 7","C) 8","D) 9"))

answers = (("B"),("C"),("B"),("B"),("C"))
guesses = []
score = 0

question_num = 0

for question in questions:
    print("____________________________")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A,B,C,D) to answer :").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")



    question_num += 1

print("_______________________________________")
print("               RESULT                  ")
print("_______________________________________")

print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()


print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()


score = int(score / len(questions) * 100)
print(f"Your score is {score}%")