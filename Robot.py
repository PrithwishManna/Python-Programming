import math

# Initialize coordinates (x, y) starting at the origin (0, 0)
x_position = 0
y_position = 0

print("Enter robot movements (e.g., UP 5, DOWN 3).")
print("Enter '!' to stop the input.")
print("-" * 30)

while True:
    # Get user input for the movement command
    command = input()

    # Check for the stop condition
    if command == '!':
        break

    try:
        # Split the command into direction and steps
        parts = command.split()

        # Input validation: check if there are exactly two parts (Direction and Steps)
        if len(parts) != 2:
            print("Invalid command format. Please use 'DIRECTION STEP' (e.g., UP 5).")
            continue

        direction = parts[0].upper() # Convert direction to uppercase for robust matching
        steps = int(parts[1])       # Convert steps to an integer

        # Update coordinates based on the direction
        if direction == 'UP':
            y_position += steps
        elif direction == 'DOWN':
            y_position -= steps
        elif direction == 'LEFT':
            x_position -= steps
        elif direction == 'RIGHT':
            x_position += steps
        else:
            print(f"Unknown direction: {direction}. Use UP, DOWN, LEFT, or RIGHT.")

    except ValueError:
        print("Invalid steps entered. Steps must be an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Calculation Phase ---

# Final displacement from the origin (0, 0) is (x_position, y_position).
# The Euclidean distance (d) is calculated using the Pythagorean theorem: 
# d = sqrt(x² + y²)
distance = math.sqrt(x_position**2 + y_position**2)

# The problem asks to print the nearest integer if the distance is a float.
# The round() function in Python handles rounding to the nearest integer.
final_distance = round(distance)

print("-" * 30)
print(f"Final coordinates: ({x_position}, {y_position})")
print(f"Calculated distance from origin: {distance:.2f}")
print(f"Output:")
print(final_distance)