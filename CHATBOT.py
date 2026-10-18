# Simple rule-based chatbot with more options


def chat():
    print("Bot: Hey there! What's your name?")
    user_name = input("You: ").strip()

#Chat conditions
    if user_name:
        print(f"Bot: Nice to meet you, {user_name.capitalize()}! How can I help you today?")
    else:
        print("Bot: Playing it mysterious, huh? No problem!")

    while True:
        msg = input("You: ").lower().strip()

        if msg in ["hello", "hi", "hey"]:
            print("Bot: Hi! How's it going?")
        elif msg in ["how are you", "how are you doing", "what's up"]:
            print("Bot: I'm just a bunch of Python code, but I'm doing great! How about you?")
        elif msg in ["what is your name", "who are you"]:
            print("Bot: I'm a simple rule-based chat bot written in Python.")
        elif msg in ["bye", "goodbye", "exit", "quit"]:
            print("Bot: See ya! Have a good one.")
            break  # Exit the loop
        else:
            print(
                "Bot:I didn't quite get that. Try asking how I am or saying hello!"
            )


# Run the bot
if __name__ == "__main__":
    chat()