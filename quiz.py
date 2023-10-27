class Question:
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def is_correct(self, choice):
        return self.correct_choice == choice


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        for question in self.questions:
            print(question.text)
            for i, choice in enumerate(question.choices, 1):
                print(f"{i}. {choice}")

            user_choice = int(input("Enter the number of your choice: ")) - 1

            if question.is_correct(user_choice):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Sorry, the correct answer is: {question.choices[question.correct_choice]}\n")

        print(f"You got {self.score} out of {len(self.questions)} questions correct.")


# Sample questions
question1 = Question("What is the capital of France?", ["London", "Paris", "Madrid", "Rome"], 1)
question2 = Question("Which planet is known as the Red Planet?", ["Venus", "Earth", "Mars", "Jupiter"], 2)
question3 = Question("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 1)

# Create a quiz
quiz = Quiz()
quiz.add_question(question1)
quiz.add_question(question2)
quiz.add_question(question3)

# Run the quiz
quiz.run()
