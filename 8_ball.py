# Name: wyatt pennington
# This program is to simulate a magic 8 ball

import random

def magic_8_ball():
    responses = [
        "Yes",
        "No",
        "Ask again later",
        "Cannot predict now",
        "Don't count on it",
        "Maybe",
        "Outlook not so good",
        "Most likely",
        "Reply hazy, try again"
    ]

    question = input("Ask the Magic 8-Ball a question: ")
    answer = random.choice(responses)
    print(f"Magic 8-Ball says: {answer}")

if __name__ == "__main__":
    magic_8_ball()
