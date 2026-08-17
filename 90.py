# 90	Create a quiz application using OOP.
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        print("\n" + self.question)

        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("===== QUIZ APPLICATION =====")

        for question in self.questions:
            question.display()

            try:
                choice = int(input("Enter your answer (1-4): "))

                if question.options[choice - 1] == question.answer:
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Wrong! Correct answer: {question.answer}")

            except (ValueError, IndexError):
                print("Invalid choice!")

        self.show_result()

    def show_result(self):
        print("\n===== QUIZ RESULT =====")
        print(f"Score: {self.score}/{len(self.questions)}")

        percentage = (self.score / len(self.questions)) * 100
        print(f"Percentage: {percentage:.2f}%")


# Creating questions
questions = [
    Question(
        "Which language is used for Python programming?",
        ["Python", "HTML", "CSS", "SQL"],
        "Python"
    ),

    Question(
        "Which keyword is used to create a class in Python?",
        ["function", "class", "object", "define"],
        "class"
    ),

    Question(
        "Which concept allows a child class to use properties of a parent class?",
        ["Encapsulation", "Inheritance", "Abstraction", "Compilation"],
        "Inheritance"
    ),

    Question(
        "Which symbol is used for comments in Python?",
        ["//", "#", "/*", "--"],
        "#"
    )
]


# Create quiz object
quiz = Quiz(questions)

# Start quiz
quiz.start()