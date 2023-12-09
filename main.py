import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import os


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        # Set background image
        image_path = os.path.join(os.path.dirname(__file__),
                                  "background.png")  # Replace "background.jpg" with your image file
        if os.path.exists(image_path):
            background_image = Image.open(image_path)
            background_image = background_image.resize((1024, 1024))  # Set the desired width and height
            background_photo = ImageTk.PhotoImage(background_image)
            background_label = tk.Label(master, image=background_photo)
            background_label.image = background_photo
            background_label.place(relwidth=1, relheight=1)
        # Apply a style for buttons
        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12, 'bold'))

        # Welcome label
        self.welcome_label = tk.Label(master, text="Welcome to Number Guessing Game!", font=('Helvetica', 16, 'bold'),
                                      bg='#b3e0ff')
        self.welcome_label.pack(pady=10)

        # Name label and entry
        self.name_label = tk.Label(master, text="Enter your name:", font=('Helvetica', 12), bg='#b3e0ff')
        self.name_label.pack()

        self.name_entry = tk.Entry(master, font=('Helvetica', 12))
        self.name_entry.pack(pady=10)

        # Start button
        self.start_button = ttk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

        # Quit button
        self.quit_button = ttk.Button(master, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

        self.random_number = 0
        self.attempts_left = 3
        self.game_over = False

    def start_game(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showinfo("Error", "Please enter your name.")
            return

        # Forget the previous widgets
        self.welcome_label.pack_forget()
        self.name_label.pack_forget()
        self.name_entry.pack_forget()
        self.start_button.pack_forget()
        self.quit_button.pack_forget()

        # Generate a random number
        self.random_number = random.randint(0, 6)
        self.attempts_left = 3
        self.game_over = False

        # Display the guessing widgets
        self.guess_label = tk.Label(self.master, text=f"{self.player_name}, Guess the number (0-6):",
                                    font=('Helvetica', 14), bg='#b3e0ff')
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.master, font=('Helvetica', 12))
        self.guess_entry.pack(pady=10)

        self.submit_button = ttk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

    def check_guess(self):
        if not self.game_over:
            try:
                user_guess = int(self.guess_entry.get())
                self.attempts_left -= 1

                if user_guess == self.random_number:
                    messagebox.showinfo("Congratulations!",
                                        f"Correct! You guessed the number in {10 - self.attempts_left} attempts.")
                    self.play_again()
                elif self.attempts_left == 0:
                    messagebox.showinfo("Game Over",
                                        f"Sorry, {self.player_name}! You've run out of attempts. The correct number was {self.random_number}.")
                    self.play_again()
                elif user_guess < self.random_number:
                    messagebox.showinfo("Incorrect", "Try again.")
                else:
                    messagebox.showinfo("Incorrect", "Try again.")

            except ValueError:
                messagebox.showinfo("Error", "Please enter a valid number.")
        else:
            messagebox.showinfo("Game Over", "The game is over. Start a new game.")

    def play_again(self):
        # Forget the previous widgets
        self.guess_label.pack_forget()
        self.guess_entry.pack_forget()
        self.submit_button.pack_forget()

        # Play again button
        self.play_again_button = ttk.Button(self.master, text="Play Again", command=self.start_game)
        self.play_again_button.pack()

        # Quit button
        self.quit_button = ttk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

        self.game_over = True


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")  # Adjust the window size as needed
    game = NumberGuessingGame(root)
    root.mainloop()
