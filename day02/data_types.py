"""
Day 2 - Data Types Explorer
Demonstrates Python's four core data types with examples.
"""

# --- Integers ---
user_age = 25
temperature = -10
year = 2026

print("=== INTEGERS ===")
print(f"User age: {user_age}, Type: {type(user_age)}")
print(f"Temperature: {temperature}, Type: {type(temperature)}")

# --- Floats ---
product_price = 19.99
pi_value = 3.14159
discount_rate = 0.15

print("\n=== FLOATS ===")
print(f"Product price: {product_price}, Type: {type(product_price)}")
print(f"Float precision issue: {0.1 + 0.2}")

# --- Booleans ---
is_logged_in = True
has_permission = False
is_active = True

print("\n=== BOOLEANS ===")
print(f"Is logged in: {is_logged_in}, Type: {type(is_logged_in)}")
print(f"Bool of 0: {bool(0)}, Bool of 1: {bool(1)}")
print(f"Bool of empty string: {bool('')}")
print(f"Bool of 'hello': {bool('hello')}")

# --- Strings ---
user_name = "Mian Khan"
city = "Lahore"
empty_string = ""

print("\n=== STRINGS ===")
print(f"User name: {user_name}, Type: {type(user_name)}")
print(f"Is empty string falsy? {not bool(empty_string)}")

# --- Type Conversion ---
print("\n=== TYPE CONVERSION ===")
age_as_string = "25"
age_as_int = int(age_as_string)
print(f"Before: {age_as_string} ({type(age_as_string)})")
print(f"After: {age_as_int} ({type(age_as_int)})")

price_as_string = "19.99"
price_as_float = float(price_as_string)
print(f"String to float: {price_as_float} ({type(price_as_float)})")

number = 42
number_as_string = str(number)
print(f"Int to string: {number_as_string} ({type(number_as_string)})")