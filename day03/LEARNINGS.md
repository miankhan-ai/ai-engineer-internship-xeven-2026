# Conditional Style Readability: A Practical Guide

## The Core Claim

No single style is universally most readable. Readability is context-dependent.
The most readable code is the code that most clearly expresses **intent** for its
specific situation. That said, some styles are objectively better in specific
contexts, and some are almost always wrong.

---

## Style Rankings by Context

### 1. Validation Chains → Guard Clauses Win

**Most readable:** Guard clauses (early returns)

```python
# Hard to read — intent buried in nesting
def process(user, order):
    if user:
        if user["active"]:
            if order:
                if order["paid"]:
                    return ship(order)
                else:
                    return "Unpaid"
            else:
                return "No order"
        else:
            return "Inactive"
    else:
        return "No user"

# Easy to read — each line answers one question and exits
def process(user, order):
    if not user:             return "No user"
    if not user["active"]:   return "Inactive"
    if not order:            return "No order"
    if not order["paid"]:    return "Unpaid"
    return ship(order)
```

**Why it's more readable:**

- Reads top-to-bottom like a checklist
- Each guard handles one failure; the reader processes them independently
- The happy path is at the bottom, unindented — visually obvious as the intended outcome
- Adding a new check means one new line at the top, not finding the correct nesting level
- Indentation depth no longer encodes logic — reducing the chance of misalignment bugs

**When it breaks down:** When branches diverge into parallel outcomes at each
level with no single "failure" to exit on. A three-way split (positive/negative/zero)
has no meaningful guard clause structure.

---

### 2. Value-to-Value Mapping → Dict Dispatch Wins

**Most readable:** Dictionary lookup

```python
# Gets unwieldy — data disguised as logic
def get_tax_rate(country):
    if country == "US":   return 0.07
    elif country == "UK": return 0.20
    elif country == "DE": return 0.19
    elif country == "PK": return 0.17
    else:                 return 0.0

# Clean — data is data, logic is logic
TAX_RATES = {"US": 0.07, "UK": 0.20, "DE": 0.19, "PK": 0.17}

def get_tax_rate(country):
    return TAX_RATES.get(country, 0.0)
```

**Why it's more readable:**

- The mapping is immediately visible as a table, not disguised as control flow
- Adding a new case is one dict entry, not editing a function
- `TAX_RATES` is independently testable and exportable
- Scales to 50 entries without degrading readability

**When it breaks down:** When branches have different logic per case, not just
different values. If each branch calls different functions with different
arguments, a dict of lambdas becomes harder to read than a clean `if/elif` chain.

---

### 3. Simple Inline Assignment → Ternary Wins

**Most readable:** Ternary expression

```python
# Four lines for a binary choice
if score >= 50:
    result = "Pass"
else:
    result = "Fail"

# One line — reads like English
result = "Pass" if score >= 50 else "Fail"
```

**Why it's more readable:**

- Assignment intent is clear: `result =` something
- The condition and both outcomes are visible at once
- Works naturally inside function calls and f-strings

**When it breaks down:** The moment you nest it.

```python
# Never do this — unreadable
label = "A" if s >= 90 else "B" if s >= 80 else "C" if s >= 70 else "F"
```

Nested ternaries violate the one rule that makes ternaries readable: at-a-glance
comprehension. Use `if/elif` for anything with more than two outcomes.

---

### 4. Uncertain Data Access → EAFP Wins

**Most readable:** Try/except (EAFP — Easier to Ask Forgiveness than Permission)

```python
# LBYL — four levels of checking to access one value
def get_city(data):
    if "user" in data:
        if "address" in data["user"]:
            if "city" in data["user"]["address"]:
                return data["user"]["address"]["city"]
    return None

# EAFP — states the intent directly
def get_city(data):
    try:
        return data["user"]["address"]["city"]
    except (KeyError, TypeError):
        return None
```

**Why it's more readable:**

- The first line of the try block states exactly what you want
- Exception handling separates the "what I want" from "what can go wrong"
- LBYL forces the reader to track all guard conditions before understanding
  what the function actually does
- Eliminates race conditions where state changes between check and use

**When LBYL wins:** Pre-validation before write or commit operations, where you
want to fail loudly before making any changes, not after.

---

### 5. Conditions on Collections → `any()`/`all()` Wins

**Most readable:** Built-in `any()` / `all()`

```python
# Explicit loop — mechanism, not intent
found = False
for item in items:
    if item > 0:
        found = True
        break

# any() — states the question directly
found = any(item > 0 for item in items)
```

**Why it's more readable:**

- `any(condition for item in collection)` reads like English
- Short-circuits automatically — no manual `break`
- Intent is the whole expression; no surrounding state variables

---

## The Universal Rules

Regardless of which style fits the context, these apply everywhere:

**1. Name complex conditions**

```python
# Unreadable condition
if user["age"] >= 18 and user["country"] in ALLOWED and not user["banned"]:
    ...

# Named condition — documents intent
is_eligible = (
    user["age"] >= 18
    and user["country"] in ALLOWED
    and not user["banned"]
)
if is_eligible:
    ...
```

**2. Never return a wrapped boolean**

```python
# Redundant
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

# Direct
def is_adult(age):
    return age >= 18
```

**3. Always handle the unexpected case**

```python
# Silent failure — new status added, no coverage, no error
def get_label(status):
    if status == "active":   return "Active"
    elif status == "banned": return "Banned"
    # Unknown status? Returns None silently.

# Loud failure — bugs surface immediately
def get_label(status):
    if status == "active":   return "Active"
    elif status == "banned": return "Banned"
    else: raise ValueError(f"Unknown status: {status}")
```

**4. Test `is None` explicitly when `0` or `False` are valid values**

```python
# Bug — score of 0 is valid but falsy
if not score:
    return "No score"

# Correct
if score is None:
    return "No score"
```

---

## Quick Reference

| Situation                              | Most Readable Style    |
| -------------------------------------- | ---------------------- |
| Chain of requirements, any can fail    | Guard clauses          |
| Value maps to value, 3+ cases          | Dict dispatch          |
| Binary inline assignment               | Ternary                |
| Accessing uncertain nested data        | EAFP (try/except)      |
| Parallel outcomes with different logic | `if/elif/else`         |
| Any/all condition over a collection    | `any()` / `all()`      |
| Complex multi-part condition           | Named boolean variable |

---

## The Actual Rule

Pick the style that makes the **intent** obvious in one pass.

If a reader has to trace execution to understand what the code is _trying to do_,
the style is wrong for that context — regardless of whether the logic is correct.
Correct and readable are separate bars. Always clear both.
