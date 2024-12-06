print("Welcome to the Quiz Game\n**************************************************")

Question_bank = [
    {"text": "The ability of one class to acquire methods and attributes of another is called____."},
    {"text": "Which of the following is a type of inheritance?"},
    {"text": "What type of inheritance has multiple subclasses to a single superclass?"},
    {"text": "Given below which person does have the large dick?"},
    {"text": "The choice that in option which is small dick?"},
]

options = [
    ["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Objects"],
    ["A. Single", "B. Multiple", "C. Double", "D. Both A and B"],
    ["A. Multiple inheritance", "B. Multilevel inheritance", "C. Hierarchical inheritance", "D. None of these"],
    ["A. Praveen", "B. Abilash", "C. Harsha", "D. Avinash"],
    ["A. Praveen", "B. Abilash", "C. Harsha", "D. Avinash"]
]

correct_answer = ["A", "D", "C", "A", "C"]

score = 0

for question in range(len(Question_bank)):
    print("****************************")
    print(Question_bank[question]["text"])
    for option in options[question]:
        print(option)
    user_answer = input("Enter your answer [A/B/C/D]: ").upper()
    
    if user_answer == correct_answer[question]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")

print(f"Your final score is: {score}/{len(Question_bank)}")
