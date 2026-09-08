# Name: [Han Rui]
# Assignment One
# dd1 is 22/9/2026 23:59pm

def simple_calculator():
    """Task A: Simple Calculator"""
    print("\n===== Simple Calculator =====")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")


def qa_bot():
    """Task B: QA Bot"""
    print("\n===== Question Answering Bot =====")
    question = input("Ask me something: ")

    if question == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif question == "python":
        print("Bot: Python is a language.")
    elif question == "jetson":
        print("Bot: Jetson Nano is an AI computer.")
    elif question == "ai":
        print("Bot: AI means Artificial Intelligence.")
    elif question == "name":
        print("Bot: My name is Python Bot.")
    else:
        print("Bot: Sorry, I don't understand.")


def turtle_drawing():
    """Task C: Turtle Drawing (Bonus)，可选择 square / triangle / star"""
    import turtle
    print("\n===== Turtle Drawing =====")
    choice = input("Please choose shape: square / triangle / star: ").strip().lower()
    t = turtle.Turtle()
    t.color("blue")

    if choice == "square":
        for _ in range(4):
            t.forward(100)
            t.left(90)
    elif choice == "triangle":
        for _ in range(3):
            t.forward(100)
            t.left(120)
    elif choice == "star":
        for _ in range(5):
            t.forward(120)
            t.right(144)
    else:
        print("Unknown shape, draw square as default")
        for _ in range(4):
            t.forward(100)
            t.left(90)

    turtle.done()


if __name__ == "__main__":
    print("Please select task: A(Calculator), B(QA Bot), C(Turtle Drawing)")
    select = input("Input A/B/C: ").strip().upper()

    if select == "A":
        simple_calculator()
    elif select == "B":
        qa_bot()
    elif select == "C":
        turtle_drawing()
    else:
        print("Invalid input, please enter A, B or C")
