def safe_divide(a, b):
    try:
        result = a / b
        print(f"Success: {a} / {b} = {result}")    
    except ZeroDivisionError:
        print(f"Error: You cannot divide {a} by zero!")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    finally:
        print("--- Division attempt finished ---\n")
safe_divide(10, 2)
safe_divide(10, 0)
safe_divide(10, "five")