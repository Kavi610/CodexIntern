import time

# Function to handle simple tasks like setting reminders
def set_reminder(reminder, delay):
    print(f"Reminder set: '{reminder}' in {delay} seconds.")
    time.sleep(delay)
    print(f"Reminder: {reminder}")

# Main chatbot function
def chatbot():
    print("Hello! I'm your Command-Line Chatbot. How can I assist you today?")
    
    while True:
        user_input = input("> ").lower()

        # Exit condition
        if 'exit' in user_input or 'bye' in user_input:
            print("Goodbye! Have a great day!")
            break
        
        # Greeting responses
        elif 'hello' in user_input or 'hi' in user_input:
            print("Hello! How can I help you?")
        
        # Simple predefined responses
        elif 'how are you' in user_input:
            print("I'm just a program, but thanks for asking! How about you?")
        elif 'what is your name' in user_input:
            print("I'm a simple command-line chatbot. You can call me Bot.")
        
        # Information responses
        elif 'time' in user_input:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(f"The current time is {current_time}.")
        elif 'date' in user_input:
            current_date = time.strftime("%Y-%m-%d", time.localtime())
            print(f"Today's date is {current_date}.")
        
        # Reminder task
        elif 'reminder' in user_input:
            print("What would you like to set a reminder for?")
            reminder = input("Reminder: ")
            print("In how many seconds should I remind you?")
            delay = int(input("Seconds: "))
            set_reminder(reminder, delay)

        # Simple fallback response
        else:
            print("I'm sorry, I don't understand that. Can you ask something else?")

if __name__ == "__main__":
    chatbot()
