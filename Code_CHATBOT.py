import tkinter as tk
from tkinter import messagebox
import datetime
import calendar

# Function to handle user inputs and provide responses
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I assist you today?"
    
    # Date, Time, Year, Day
    elif "date" in user_input:
        return f"Today's date is {datetime.date.today()}."
    
    elif "time" in user_input:
        return f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    
    elif "year" in user_input:
        return f"The current year is {datetime.datetime.now().year}."
    
    elif "day" in user_input:
        return f"Today is {datetime.datetime.now().strftime('%A')}."
    
    # Calendar of the current year
    elif "calendar" in user_input:
        year = datetime.datetime.now().year
        cal = calendar.TextCalendar(calendar.SUNDAY)
        return f"Here is the calendar for {year}:\n\n{cal.pryear(year)}"
    
    # Number of Countries
    elif "countries" in user_input:
        return "There are 195 countries in the world."
    
    # Number of states in India
    elif "states in india" in user_input or "states of india" in user_input:
        return "India has 28 states and 8 Union Territories."
    
    # National symbols of India
    elif "national bird" in user_input:
        return "The national bird of India is the Indian Peafowl (Peacock)."
    
    elif "national animal" in user_input:
        return "The national animal of India is the Bengal Tiger."
    
    elif "color in indian flag" in user_input:
        return "The Indian flag has three colors: Saffron (top), White (middle), and Green (bottom), with a navy blue Ashoka Chakra in the center."

    # Unknown response
    else:
        return "Sorry, I didn't understand that. Can you please ask something else?"

# Function to display response
def get_response():
    user_input = user_input_field.get()
    response = chatbot_response(user_input)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_input}\nBot: {response}\n\n")
    chat_log.config(state=tk.DISABLED)
    user_input_field.delete(0, tk.END)

# Set up the main GUI window
root = tk.Tk()
root.title("Simple Chatbot")
root.geometry("500x400")
root.config(bg="#F0F0F0")

# Create a scrollable chat area
chat_log = tk.Text(root, bg="#FFFFFF", fg="#000000", font=("Arial", 12), wrap=tk.WORD, state=tk.DISABLED, height=15, width=60)
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create a user input field
user_input_field = tk.Entry(root, bg="#E8E8E8", font=("Arial", 12), width=40)
user_input_field.grid(row=1, column=0, padx=10, pady=10)

# Create a send button
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=get_response, bg="#FF5733", fg="white")
send_button.grid(row=1, column=1, padx=10, pady=10)

# Greet the user at the start
chat_log.config(state=tk.NORMAL)
chat_log.insert(tk.END, "Bot: Hello! I'm your assistant. How can I help you today?\n\n")
chat_log.config(state=tk.DISABLED)

# Start the GUI event loop
root.mainloop()
