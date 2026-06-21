import random

def roll_dice(sides=6):
    """
    Rolls a dice with the specified number of sides.

    Args:
        sides (int): The number of sides on the dice. Defaults to 6.

    Returns:
        int: The result of the roll.
    """
    try:
        # Check if the input is a positive integer
        if not isinstance(sides, int) or sides <= 0:
            raise ValueError("The number of sides must be a positive integer.")

        # Roll the dice
        result = random.randint(1, sides)

        # Display the result
        print(f"You rolled a {result} on a {sides}-sided dice.")

        return result

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
roll_dice(20)