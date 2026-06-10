"""
Day 3 - Grade Calculator
Accepts a numeric grade (0-100) and prints the letter grade,
an encouraging message, and a short interpretation.
"""


def get_grade():
    """Prompt until a valid numeric grade in [0, 100] is entered."""
    while True:
        raw = input("Enter grade (0-100): ").strip()
        try:
            # float() handles both "85" and "85.5". Use int() instead if decimals shouldn't be allowed.
            grade = float(raw)
        except ValueError:
            print(f"'{raw}' is not a number. Try again.")
            continue

        # Range check happens after parsing — separate "is it a number?" from "is it in range?"
        if 0 <= grade <= 100:
            return grade
        print("Grade must be between 0 and 100.")


def classify_grade(grade):
    """Return (letter, message, interpretation) for a grade in [0, 100]."""
    # Ordered high to low. Each elif only runs if previous checks failed,
    # so `grade >= 80` implicitly means 80 <= grade < 90.
    if grade >= 90:
        return "A", "Excellent work!", "Outstanding mastery of the material."
    elif grade >= 80:
        return "B", "Good job!", "Solid understanding with room to push further."
    elif grade >= 70:
        return "C", "Fair effort.", "Average — the fundamentals are there, depth is missing."
    elif grade >= 60:
        return "D", "You passed, but barely.", "Significant gaps. Revisit the core concepts."
    else:
        return "F", "Failed this time.", "Restart from the basics — no shortcut around it."


if __name__ == "__main__":
    grade = get_grade()
    letter, message, interpretation = classify_grade(grade)
    print(f"\nGrade: {grade}  →  {letter}")
    print(f"{message} {interpretation}")