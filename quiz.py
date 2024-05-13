# 4. The Quiz Game

#Objective:
#The aim of this assignment is to create a quiz game that asks questions and checks answers.

#Task 1: Develop a list of questions and answers.
#Task 2: Write a function that quizzes the user and takes their answers.
#Task 3: Score the quiz and give the user feedback on their performance.

# Task 1 Quiz questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest mammal?": "Blue whale",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "How many continents are there?": "7"
}

# Task 2  Function to quiz the user
def quiz():
    score = 0
    total_questions = len(quiz_questions)

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    for question, answer in quiz_questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
# Task 3 Scoring quiz and giving feedback
    print("\nQuiz completed!")
    print("You scored {} out of {}.".format(score, total_questions))
    percentage = (score / total_questions) * 100
    print("Your score percentage is: {:.2f}%".format(percentage))
    if percentage >= 70:
        print("Congratulations! You passed the quiz.")
    else:
        print("Sorry, you did not pass the quiz. Better luck next time!")

# Main function
def main():
    quiz()

# Entry point of the program
if __name__ == "__main__":
    main()
