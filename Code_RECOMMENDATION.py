import tkinter as tk
from tkinter import messagebox

# Sample data for recommendations
recommendations = {
    "Movies": {
        "Action": [
            "Mad Max", "Die Hard", "John Wick", 
            "Tanhaji: The Unsung Warrior", "Shershaah", "Sooryavanshi", 
            "Pathaan", "Jawan", "Bholaa", "Vikram Vedha", 
            "Extraction (Hindi Dubbed)", "Baaghi 3", "Antim: The Final Truth"
        ],
        "Action Thrillers": ["Dabangg", "Singham", "Agneepath", "Ek Tha Tiger", "Race 2", "Bang Bang!", 
            "Kick", "Baby", "Bajirao Mastani", "War"
        ],
        "Comedy": [
            "The Hangover", "Superbad", "Step Brothers", 
            "Hera Pheri", "Chupke Chupke", "Andaz Apna Apna", 
            "Dhamaal", "Welcome", "Gol Maal", "Padosan", 
            "3 Idiots", "Chup Chup Ke", "Bareilly Ki Barfi", 
            "Judwaa 2", "Munna Bhai M.B.B.S.", "Lage Raho Munna Bhai", 
            "Fukrey", "Bhaag Milkha Bhaag", "Tanu Weds Manu", 
            "Khosla Ka Ghosla", "Biwi No. 1", "Housefull", "No Entry"
        ],
        "Drama": ["Kabhi Khushi Kabhie Gham","Taare Zameen Par","Paa","Barfi!","Anand","Munna Bhai M.B.B.S."],
        "Sci-Fi": ["Interstellar", "Inception", "The Matrix","Koi... Mil Gaya","War","Robot","Makkhi","Shankar's 2.0","Ra.One"],
        "Blockbuster": [
            "Mission Kashmir (2000)", "Lakshya (2004)", "Dhoom (2004)", 
            "Dus (2005)", "Krrish (2006)", "Don: The Chase Begins Again (2006)", 
            "Dhoom 2 (2006)", "Shootout at Lokhandwala (2007)", "Ghajini (2008)", 
            "Wanted (2009)"
        ],
    },
    "Books": {
        "Fiction": ["To Kill a Mockingbird", "1984", "The Great Gatsby"],
        "Mystery": ["Gone Girl", "The Girl with the Dragon Tattoo", "Sherlock Holmes"],
        "Fantasy": ["Harry Potter", "The Hobbit", "The Name of the Wind"],
        "Non-Fiction": ["Sapiens", "Educated", "The Wright Brothers"],
    },
    "Products": {
        "Electronics": ["Smartphone", "Laptop", "Smartwatch"," Tablets","Headphones & Earbuds",
                        "Smart Speakers", "Watches", "Computer","Television","Gaming Consoles", "Cameras","Key-Board", "Mouse", "Monitor", "Switches", "Fan"],
        "Home Appliances": ["Vacuum Cleaner","Air Purifiers","Coffee Makers","Air Conditioners","Dishwashers","Juicers & Blenders",
                             "Microwave", "Refrigerator", "Washing-Machine", "Mixer", "Iron", "Grinder"],
        "Sports": ["Football", "Cricket", "Tennis Racket", "Basket-Ball", "Tennis", "Volly-Ball", "Kabaddi", "Kho-Kho"],
            "Adventure Sports": ["Skydiving", "Bungee Jumping", "White Water Rafting", "Rock Climbing", "Mountain Biking"],
            "Individual Sports": ["Tennis", "Swimming", "Boxing", "Cycling", "Badminton"],
            "Team Sports": ["Football", "Cricket", "Basketball", "Volleyball", "Rugby"],
        "Clothing": ["Dress", "Tops", "Skirts", "Sarees", "Blouses", "Leggings","Crop-Tops","Lenghas","Shirts", "Jeans", "T-Shirts", "Jackets", "Suits", "Shorts",
             "Onesies", "Jumpsuits", "Romper", "Pants" ]
    },
}


def recommend_items():
    # Get the user's preferred category and type
    category = category_var.get()
    preference = preference_var.get()

    # Check if both category and type are selected
    if not category or not preference:
        messagebox.showerror("Error", "Please select a category and a type.")
        return

    # Get the recommendations for the selected category and type
    category_data = recommendations.get(category, {})
    recommended = category_data.get(preference, [])

    # Display the recommendations
    if recommended:
        recommendations_label.config(text="\n".join(recommended))
    else:
        recommendations_label.config(text="No recommendations available for this selection.")

# Create the main window
root = tk.Tk()
root.title("PickHub")
root.geometry("600x500")
root.config(bg="#f0f0f0")

# Title label with larger font
title_label = tk.Label(root, text="PickHub - Recommendation System", font=("Helvetica", 20, 'bold'), bg="#f0f0f0")
title_label.pack(pady=20)

# Category selection with smaller font
category_var = tk.StringVar()
category_label = tk.Label(root, text="Select a category:", font=("Helvetica", 14), bg="#f0f0f0")
category_label.pack(pady=5)

# Create Radio buttons with smaller font and horizontal layout
category_frame = tk.Frame(root, bg="#f0f0f0")
category_frame.pack(pady=5)

for category in recommendations.keys():
    category_button = tk.Radiobutton(category_frame, text=category, variable=category_var, value=category, 
                                     font=("Helvetica", 10), bg="#f0f0f0", indicatoron=False, 
                                     width=15, height=2, relief="solid", command=lambda: update_preferences())
    category_button.pack(side="left", padx=10)

def update_preferences():
    # Clear existing preference options
    for widget in preferences_frame.winfo_children():
        widget.destroy()

    # Add preference options based on selected category
    selected_category = category_var.get()
    if selected_category:
        for preference in recommendations[selected_category].keys():
            preference_button = tk.Radiobutton(preferences_frame, text=preference, variable=preference_var, value=preference,
                                               font=("Helvetica", 10), bg="#f0f0f0", indicatoron=False, width=15, height=2)
            preference_button.pack(side="left", padx=10)

# Preference selection with smaller font
preference_var = tk.StringVar()
preferences_label = tk.Label(root, text="Select your preference:", font=("Helvetica", 14), bg="#f0f0f0")
preferences_label.pack(pady=5)

preferences_frame = tk.Frame(root, bg="#f0f0f0")
preferences_frame.pack(pady=5)

# Recommend button with larger font and custom style
recommend_button = tk.Button(root, text="Recommend", command=recommend_items, font=("Helvetica", 14, 'bold'), bg="#4CAF50", fg="white", width=15, height=2)
recommend_button.pack(pady=15)

# Recommendations label with larger font
recommendations_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left", bg="#f0f0f0")
recommendations_label.pack(pady=10)

# Run the application
root.mainloop()
