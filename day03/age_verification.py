"""
Day 3 - Age Verification System
Classifies a person into an age group, with input validation
for non-numeric, negative, empty, and unrealistic values.
"""

# Upper sanity bound. Oldest verified human lived to 122, so 130 is a
# generous ceiling that still rejects obvious garbage like 9999.
MAX_AGE = 130


def classify_age(user_name, age):
    """Return a greeting based on age group. Assumes age is already validated."""
    # Order matters: each `elif` only runs if all earlier conditions were False,
    # so we check from youngest to oldest and each branch implicitly means
    # "age is greater than the previous cutoff AND <= this one".
    if age <= 12:
        # 0–12: child. Upper bound 12 because 13 is conventionally the start of teen years ("thir-teen").
        return f"Hello {user_name}! As a child, the world is full of wonder for you."
    elif age <= 17:
        # 13–17: teenager. We already know age > 12 from the failed `if` above.
        # Cutoff at 17 because 18 is the typical legal adulthood threshold.
        return f"Hello {user_name}! As a teenager, you are going through many changes."
    elif age <= 64:
        # 18–64: adult. 65 is the conventional retirement/senior threshold in most contexts.
        return f"Hello {user_name}! As an adult, you have many responsibilities."
    else:
        # 65+: senior. `else` catches everything remaining — no need for another condition.
        return f"Hello {user_name}! As a senior, you have a wealth of experience to share."


def get_name():
    """Prompt until a non-empty name is entered."""
    while True:
        # .strip() removes leading/trailing whitespace so " " doesn't count as a valid name.
        name = input("Enter name: ").strip()
        if name:
            # Non-empty string is truthy in Python — accept and return.
            return name
        # Empty string is falsy — fall through, print error, loop re-prompts.
        print("Name cannot be empty. Try again.")


def get_age():
    """Prompt until a valid integer age in [0, MAX_AGE] is entered."""
    while True:
        raw = input("Enter age: ").strip()
        try:
            # int() raises ValueError on non-numeric input like "twenty" or "12.5".
            # We catch it instead of letting the program crash.
            age = int(raw)
        except ValueError:
            print(f"'{raw}' is not a valid number. Enter a whole number.")
            # `continue` skips the rest of the loop body and re-prompts.
            continue

        # At this point `age` is a valid int. Now check it's in a sensible range.
        if age < 0:
            # Negative ages are nonsensical — nobody is -5 years old.
            print("Age cannot be negative. Try again.")
        elif age > MAX_AGE:
            # Anything above MAX_AGE is almost certainly a typo or joke input.
            print(f"Age above {MAX_AGE}? Unlikely. Try again.")
        else:
            # Passed all checks: valid integer within range. Return and exit the loop.
            return age


if __name__ == "__main__":
    # This guard ensures the prompts only run when the file is executed directly,
    # not when it's imported as a module (e.g. for unit testing).
    user_name = get_name()
    user_age = get_age()
    print(classify_age(user_name, user_age))