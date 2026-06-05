# Adventure Quiz Game

print("\n================================")
print("     WELCOME TO QUIZ QUEST")
print("================================\n")

name = input("Enter your name: ").strip().title()

print(f"\nHello {name}!")

score = 0

while True:

    print("\n----- MAIN MENU -----")
    print("1. Start Quiz")
    print("2. View Name Details")
    print("3. Exit")

    choice = input("\nEnter choice: ")

    match choice:

        case "1":

            print("\nQuiz Started!\n")

            questions = 0

            # Question 1
            answer = input(
                "1. What keyword is used for loops that repeat a fixed number of times?\n"
                "(for / loop / repeat): "
            ).lower()

            questions += 1

            if answer == "for":
                print("Correct!\n")
                score += 10
            else:
                print("Wrong!\n")

            # Question 2
            answer = input(
                "2. What data type is used for whole numbers?\n"
                "(int / float / string): "
            ).lower()

            questions += 1

            if answer == "int":
                print("Correct!\n")
                score += 10
            else:
                print("Wrong!\n")

            # Question 3
            answer = input(
                "3. Which method converts text to lowercase?\n"
                "(lower / uppercase / small): "
            ).lower()

            questions += 1

            if answer == "lower":
                print("Correct!\n")
                score += 10
            else:
                print("Wrong!\n")

            percentage = (score / (questions * 10)) * 100

            print("\n===== RESULTS =====")
            print(f"Score: {score}")

            if percentage >= 80:
                print("Grade: A")
            elif percentage >= 50:
                print("Grade: B")
            else:
                print("Grade: C")

        case "2":

            print("\n===== NAME DETAILS =====")

            print("Original Name:", name)

            print("First 3 letters:", name[:3])

            print("Last 3 letters:", name[-3:])

            print("Uppercase:", name.upper())

            print("Lowercase:", name.lower())

            print("Length:", len(name))

        case "3":

            print("\nThank you for playing!")
            break

        case _:

            print("\nInvalid choice!")
            continue
'''
Challenge Version (Try Without Looking at Solution)

Build a Banking System with:

Create account
Check balance
Deposit money
Withdraw money
Exit
'''