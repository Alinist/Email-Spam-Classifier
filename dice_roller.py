import random
import tkinter as tk
from tkinter import messagebox

class DiceRoller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dice Roller")
        self.roll_history = []

        self.dice_type_label = tk.Label(self.root, text="Select a dice type:")
        self.dice_type_label.pack()

        self.dice_type_var = tk.StringVar(self.root)
        self.dice_type_var.set("6-sided")  # default value

        self.dice_type_option = tk.OptionMenu(self.root, self.dice_type_var, "4-sided", "6-sided", "8-sided", "10-sided", "12-sided", "20-sided")
        self.dice_type_option.pack()

        self.num_dice_label = tk.Label(self.root, text="Number of dice to roll:")
        self.num_dice_label.pack()

        self.num_dice_var = tk.IntVar(self.root)
        self.num_dice_var.set(1)  # default value

        self.num_dice_option = tk.OptionMenu(self.root, self.num_dice_var, 1, 2, 3, 4, 5)
        self.num_dice_option.pack()

        self.roll_button = tk.Button(self.root, text="Roll", command=self.roll_dice)
        self.roll_button.pack()

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        self.reset_button.pack()

        self.roll_history_label = tk.Label(self.root, text="Roll History:")
        self.roll_history_label.pack()

        self.roll_history_text = tk.Text(self.root, height=10, width=40)
        self.roll_history_text.pack()

    def roll_dice(self):
        dice_type = self.dice_type_var.get()
        num_dice = self.num_dice_var.get()

        if dice_type == "4-sided":
            sides = 4
        elif dice_type == "6-sided":
            sides = 6
        elif dice_type == "8-sided":
            sides = 8
        elif dice_type == "10-sided":
            sides = 10
        elif dice_type == "12-sided":
            sides = 12
        elif dice_type == "20-sided":
            sides = 20

        rolls = [random.randint(1, sides) for _ in range(num_dice)]

        self.roll_history.append(rolls)
        self.roll_history_text.insert(tk.END, f"Rolled {num_dice} {dice_type} dice: {rolls}\n")

    def reset(self):
        self.roll_history = []
        self.roll_history_text.delete(1.0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    dice_roller = DiceRoller()
    dice_roller.run()