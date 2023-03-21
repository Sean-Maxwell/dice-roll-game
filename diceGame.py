import tkinter as tk
import random

class DiceGame:
    def __init__(self, master):
        self.master = master
        master.title("Dice Roll Game")
        master.configure(bg='black')

        self.num_rolls = 0

        # Create dice image
        self.dice_icons = [
            # Dice face 1
            """
            ____   
           |    |  
           |  • |  
           |____|  
            """,
            # Dice face 2
            """
            ____   
           |•   |  
           |    |  
           |___•|  
            """,
            # Dice face 3
            """
            ____   
           |•   |  
           | •  |  
           |___•|  
            """,
            # Dice face 4
            """
            ____   
           |• • |  
           |    |  
           |• • |  
            """,
            # Dice face 5
            """
            ____   
           |• • |  
           | •  |  
           |• • |  
            """,
            # Dice face 6
            """
            ____   
           |• • |  
           |• • |  
           |• • |  
            """
        ]
        self.dice_image = tk.StringVar(value=self.dice_icons[0])
        self.dice_label = tk.Label(master, textvariable=self.dice_image, font=("Courier", 36), bg="black", fg="white")
        self.dice_label.pack(pady=10)

        # Create roll button
        self.roll_button = tk.Button(master, text="Roll", command=self.roll_dice, font=("Courier", 18), bg="white", fg="black")
        self.roll_button.pack(pady=10)

        # Create quit button
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_game, font=("Courier", 18), bg="white", fg="black")
        self.quit_button.pack(pady=10)

    def roll_dice(self):
        self.num_rolls += 1

        # Roll the dice animation
        for i in range(5):
            self.dice_image.set(self.dice_icons[random.randint(0, 5)])
            self.master.update()
            self.master.after(100)

        # Print the final result
        roll_result = random.randint(1, 6)
        self.dice_image.set(self.dice_icons[roll_result - 1])
        result_label = tk.Label(self.master, text=f"You rolled a {roll_result}", font=("Courier", 24), bg="black", fg="white")
        result_label.pack(pady=10)

    def quit_game(self):
        # Create thank you message and show number of rolls
        thank_you = tk.Label(self.master, text=f"Thank you for playing! You rolled {self.num_rolls} times.", font=("Courier", 18), bg="black", fg="white")
        thank_you.pack(pady=10)

        # Exit after 2 seconds
        self.master.after(2000, self.master.destroy)

# Create the GUI window
root = tk.Tk()
root.geometry("300x300")

# Create the game instance
game = DiceGame(root)

# Start the GUI event loop
root.mainloop()
