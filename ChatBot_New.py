#greet you as per the time 
import datetime
import time

name=input("Enter your name!  :")

presentHour= datetime.datetime.now().hour

if 5<= presentHour <=11:
    print("Good Morning",name)
elif 11<= presentHour <= 17:
    print("Good Afternoon",name)
elif 17<= presentHour <=20:
    print("Good Evening",name)

else :
    print("Good Night",name)

print("Hello! Welcome to your smart digital asistant!")
print("You can ask me anything, I'm here to solve your problems")

# ChatBot memory creation
responses = {
    # Greetings
    "hello": "Hii! How can I help you today?",
    "hi": "Hello! Welcome to AJ Nexus. How can I help you?",
    "hey": "Hey! I'm AJ's Bot. What can I do for you?",
    "good morning": "Good Morning! How can I assist you today?",
    "good afternoon": "Good Afternoon! How can I help you?",
    "good evening": "Good Evening! What can I help you with?",

    # About Bot
    "who are you": "I'm AJ's Bot, your smart digital assistant.",
    "what is your name": "My name is AJ's Bot.",
    "what can you do": "I can help you with website information, services, FAQs, account-related questions and basic technical support.",
    "how can you help me": "You can ask me about our services, website features, account problems, contact information and other common questions.",

    # Website
    "what is this website": "This is AJ Nexus, a smart digital assistance platform designed to help users quickly find information.",
    "how does this website work": "Simply choose a service or ask AJ's Bot your question, and I'll guide you with the available information.",
    "services": "We provide digital assistance, information, FAQs and basic user support through our platform.",

    # Account
    "how to create account": "Click on the Sign Up or Register button and fill in the required information.",
    "how to login": "Click on the Login button and enter your registered email and password.",
    "forgot password": "Click on 'Forgot Password' on the login page and follow the instructions to reset your password.",
    "change password": "You can change your password from your account settings.",

    # Technical Support
    "website not working": "Please refresh the page and check your internet connection. If the problem continues, please contact our support team.",
    "page not loading": "Please check your internet connection, refresh the page and try again.",
    "login problem": "Please check your email and password. If you still cannot log in, try resetting your password.",
    "error": "Please note the error message and try refreshing the page. If the issue continues, contact support.",

    # Contact
    "contact": "You can contact our support team through the Contact Us section of the website.",
    "support": "Our support team can help you with account, website and technical issues.",
    "email": "Please visit the Contact Us section to find our official support email.",

    # Feedback
    "feedback": "We'd love to hear your feedback! Please use the Feedback section to share your experience.",
    "suggestion": "Your suggestions help us improve AJ Nexus. Please share your suggestion through the Feedback section.",

    # General
    "how are you": "I'm doing great! Thanks for asking. How can I help you?",
    "thank you": "You're welcome! I'm always happy to help.",
    "thanks": "You're welcome! 😊",
    "help": "Sure! You can ask me about our website, services, account, login, technical problems or contact support.",

    # Goodbye
    "bye": "Bye! Take care and have a great day!",
    "goodbye": "Goodbye! See you again soon!"
}

# Function to get response from chatbot
def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()

    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I'm not able to answer your question because I'm still in learning mode. Sorry!"

# Take user input
while True:
    userInput = input("Please ask your question: ")

    if "bye" in userInput.lower():
        print("Bot's Response: Bye! Take care ")
        break

    reply = getResponseOfBot(userInput)
    print("Bot's Response:", reply)
