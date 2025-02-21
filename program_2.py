# Logan H's Random Math Quiz Program (2/21/25)

# 1st, import the random module, will use this in a second.
import random

# 2nd, use def function to make the math quiz use 2 random numbers (integers) using the
#      random that we imported before
def math_quiz():
    n1 = random.randint(100, 600)
    n2 = random.randint(100, 600)

# 3rd, with those random numbers generated, we put those into a math problem
    print(" ",n1)
    print("+",n2)
    print("-------")

# 4th, Then we ask for the answer, asking it as an integer
    user_answer = int(input("What is your final answer: "))

# 5th, We get those two numbers, add them, then use an if and else statement to see
#      if the number we got is the same as their inputted number (and emojis for fun)
    correct_answer = n1 + n2
    if user_answer == correct_answer:
        print("Congrats! That is correct. 🎉🎉🎉")
    else:
        print("NOPE! The correct answer is:", correct_answer, "❌❌❌")

math_quiz()
