from chatbot import ask_chatbot

print("Simple Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    reply = ask_chatbot(user_input)
    print("Bot:", reply)
