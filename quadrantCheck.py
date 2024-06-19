def find_quadrant(x1, y1):
    if x1 == 0 and y1 == 0:
        return 0  # Origin
    elif x1 == 0 and y1 > 0:
        return 12  # Positive y-axis
    elif x1 == 0 and y1 < 0:
        return 34  # Negative y-axis
    elif y1 == 0 and x1 > 0:
        return 41  # Positive x-axis
    elif y1 == 0 and x1 < 0:
        return 23  # Negative x-axis
    elif x1 > 0 and y1 > 0:
        return 1  # First quadrant
    elif x1 < 0 and y1 > 0:
        return 2  # Second quadrant
    elif x1 < 0 and y1 < 0:
        return 3  # Third quadrant
    elif x1 > 0 and y1 < 0:
        return 4  # Fourth quadrant

# Example usage
print(find_quadrant(0, 0))    # Output: 0
print(find_quadrant(1, 1))    # Output: 1
print(find_quadrant(-1, 1))   # Output: 2
print(find_quadrant(-1, -1))  # Output: 3
print(find_quadrant(1, -1))   # Output: 4
print(find_quadrant(0, 5))    # Output: 12
print(find_quadrant(-5, 0))   # Output: 23
print(find_quadrant(0, -5))   # Output: 34
print(find_quadrant(5, 0))    # Output: 41
