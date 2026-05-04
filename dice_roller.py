import random

def roll_dice(sides=6):
    """Returns a random integer between 1 and the number of sides."""
    return random.randint(1, sides)

# Example usage:
print(f"You rolled a {roll_dice()}")
