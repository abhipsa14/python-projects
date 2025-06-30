## import the regular expression module to handle pattern matching
import re
## A dictionary that maps keywords to predined respnses
responses={
    "hello": "Hello! How can I assist you today?",
    "help": "Sure! What do you need help with?",
    "thanks": "You're welcome! If you have any more questions, feel free to ask.",
    "weather": "The weather is always changing! What specific information are you looking for?",
    "name": "I am your friendly chatbot! You can call me Chatbot.",
    "joke": "Why don't scientists trust atoms? Because they make up everything!",
    "time": "I don't have a clock, but I can tell you that it's always a good time to chat!",
    "news": "I don't have real-time news updates, but I can tell you that the world is always full of interesting events!",
    "quote": "Here's a quote for you: 'The only limit to our realization of tomorrow is our doubts of today.",
    "default": "I'm not sure how to respond to that. Can you please rephrase?",
}
## function to find the appropriate response based on the user's input
def chatbot_response(user_input):
    ## convert user input to lowercase to make matching case-insensitive
    user_input = user_input.lower()

    for keyword in responses:
        ## use regular expression to find the keyword in the user input
        if re.search(keyword, user_input):
            return responses[keyword]
        return responses["default" ]

## main function to run the chatbot
def main():
    print("Welcome to the chatbot! Type 'bye' to end the conversation.")
    while True:
        ## user input is taken from the console
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        ## get chatbot's response based on user input
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

## if this script is run directly, execute the main function
if __name__ == "__main__":
    main()
else:
    print("This script is intended to be run directly. Please run it as a standalone program.")
    ## This ensures that the chatbot can be imported without executing the main function
    ## This is useful for testing or if you want to use the chatbot in another script.
    ## If you want to use this chatbot in another script, you can import the chatbot_response
    ## function and use it to get responses based on user input.
    ## For example:
    # from chatbot import chatbot_response
    # response = chatbot_response("Hello, how are you?")
    # print(response)  # This will print the chatbot's response to the input.
    ## This allows for better modularity and reusability of the chatbot code.
    ## You can also add more keywords and responses to the responses dictionary to make the chatbot more