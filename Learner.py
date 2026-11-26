import customtkinter as ctk

# Configure the appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# 1. Create the window
app = ctk.CTk()
app.title("My First Modern App")
app.geometry("4000x3000")

# 2. Create widgets
title = ctk.CTkLabel(
    app,
    text="Hello!",
    font=("ALGERIAN", 28, "bold")
)

button = ctk.CTkButton(
    app,
    text="Konnichiwa"
)

# 3. Place widgets inside the window
title.pack(pady=70)
button.pack(pady=60)

# 4. Run the application
app.mainloop()