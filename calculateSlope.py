def calculate_slope_and_intercept(x1, y1, x2, y2):
    # Check if the line is vertical
    if x1 == x2:
        # For a vertical line, the slope is undefined
        # Return a special indicator ("Vertical line") and the x-coordinate (x1)
        return ("Vertical line", x1)
    
    # Check if the line is horizontal
    elif y1 == y2:
        # For a horizontal line, the slope is 0
        slope = 0
        # The y-intercept is simply y1 (since y = mx + b and m = 0, y = b)
        intercept = y1
        return (slope, intercept)
    
    else:
        # Calculate the slope (m) using the formula: m = (y2 - y1) / (x2 - x1)
        slope = (y2 - y1) / (x2 - x1)
        # Calculate the y-intercept (b) using the formula: b = y1 - m * x1
        intercept = y1 - slope * x1
        return (slope, intercept)

# Example usage
# Prompt the user to enter the coordinates of two points
x1, y1, x2, y2 = map(float, input("Enter coordinates (x1, y1, x2, y2): ").split())

# Call the function to calculate the slope and intercept
result = calculate_slope_and_intercept(x1, y1, x2, y2)

# Print the result
print(f"Slope and intercept: {result}")
