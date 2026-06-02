# Why use match?

# For simple conditions, if-elif-else is often clearer. The real strength of match appears when matching more complex structures such as:
point = (3, 0)

match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"On x-axis at {x}")
    case (0, y):
        print(f"On y-axis at {y}")
    case (x, y):
        print(f"Point at ({x}, {y})")