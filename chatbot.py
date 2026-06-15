def get_response(message):

    message = message.lower()

    if message == "hi":
        return "Hello! Welcome."

    elif message == "hello":
        return "Hi there!"

    elif message == "how are you":
        return "I am fine."

    elif message == "services":
        return "We provide cloud services."

    elif message == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."