import random

TYPES = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]


def roll(code):
    """
    Simulates a roll of dice based on a provided code pattern.

    Args:
        code (str): The dice roll pattern, e.g., "2D10+10", "D6", "3D6-2".
                    - `D<number>` indicates the type of dice (e.g., D6 is a six-sided die).
                    - Optional prefix indicates the number of dice rolls (e.g., 2D6 for two rolls of a six-sided die).
                    - An optional suffix can specify a modifier, either positive or negative.

    Returns:
        int: The result of the dice roll, including any modifiers.

    Raises:
        ValueError: If the input format is incorrect or if the specified dice type is not supported.

    Example:
        >>> roll("2D10+10")
        25  # Example output
        >>> roll("D6")
        4   # Example output
    """
    for type in TYPES:
        if type in code:
            try:
                multiply, modifier = code.split(type)
            except ValueError:
                return "Wrong input type"

            type_value = int(type[1:])
            break
    else:
        return "Wrong input type"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong input type"

    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong input type"

    total_roll = sum(random.randint(1, type_value) for _ in range(multiply)) + modifier
    return total_roll

if __name__ == "__main__":
    print(roll("2D10+10"))
    print(roll("D6"))
    print(roll("2D3"))
    print(roll("D12-1"))
    print(roll("DD34"))
    print(roll("4-3D6"))





