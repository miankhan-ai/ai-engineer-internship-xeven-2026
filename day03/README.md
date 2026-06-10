# Day 3 — Conditional Statements & Logic

## Morning: Theory

- if/elif/else syntax and structure
- Boolean logic, truthy/falsy values
- Comparison operators
- Practical use cases: auth, validation, flow control
- Nested conditionals, common pitfalls

## Afternoon: Implementation

### Task 1 — Age Verification System (`age_verification.py`)

Classifies user into Child / Teenager / Adult / Senior with input validation
for non-numeric, negative, empty, and unrealistic values.

### Task 2 — Grade Calculator (`grade_calculator.py`)

Accepts numeric grade 0–100, assigns letter grade A–F with
personalized messages and full input validation.

### Task 3 — Flowcharts (`day3_flowcharts.ipynb`)

Jupyter notebook with matplotlib flowcharts for every function
in both programs.

## Edge Cases Tested

- Negative ages / ages above 130
- Non-numeric input (letters, symbols, floats-as-age)
- Grade below 0 / above 100
- Boundary values: 12/13, 17/18, 64/65, 59/60, 69/70, 79/80, 89/90

## Key Concepts Practised

- Guard clauses over nested ifs
- EAFP (try/except) for input parsing
- elif chains vs multiple if statements
- Truthiness checks vs explicit None comparisons
