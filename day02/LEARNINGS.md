````markdown
# LEARNINGS.md

## Python Memory Management and Data Types

---

## 1. Everything in Python is an Object

- Every value in Python is an object stored in memory (heap).
- Variables do not store values directly; they store references to objects.
- Each object contains:
  - Type
  - Value
  - Reference count (CPython implementation detail)

### Key Insight

> Python variables are labels pointing to objects, not containers holding data.

---

## 2. Python Data Types Are Unified Under One Model

Python does not treat data types differently in memory allocation. Instead, all types follow the same object model.

### Core Built-in Types

- int
- float
- bool
- str

### Collection Types

- list
- tuple
- dict
- set

---

## 3. Mutable vs Immutable Types (Most Important Concept)

### Immutable Types

Examples:

- int, float, bool
- str, tuple

Behavior:

- Cannot be modified after creation
- Any modification creates a new object in memory

```python
x = "hello"
x = x + " world"  # new object created
```
````

### Mutable Types

Examples:

- list, dict, set

Behavior:

- Can be modified in place
- Memory address remains unchanged

```python
lst = [1, 2, 3]
lst.append(4)  # same object updated
```

### Key Insight

> Mutability defines whether Python updates an object or creates a new one.

---

## 4. Memory Model: Stack vs Heap

### Heap

- Stores actual objects
- Managed by Python memory manager

### Stack

- Stores references (variable bindings)
- Stores function call frames

### Key Insight

> Objects live in heap, references live in stack.

---

## 5. Reference Counting (Primary Memory Mechanism in CPython)

- Python tracks how many references point to an object.
- When reference count reaches 0, memory is freed.

```python
a = [1, 2, 3]
b = a  # reference count increases
del a
del b  # object deleted
```

### Key Insight

> Memory is automatically freed when no references remain.

---

## 6. Garbage Collection (Cycle Detection)

Reference counting alone cannot handle circular references.

```python
a = []
a.append(a)
```

- Object refers to itself
- Reference count never reaches zero

### Solution:

- Python Garbage Collector detects and removes cyclic references
- Uses generational approach (0, 1, 2)

---

## 7. Object Interning (Memory Optimization)

Python reuses some immutable objects to save memory.

### Examples:

- Small integers (typically -5 to 256)
- Some strings

```python
a = 100
b = 100
a is b  # often True
```

### Key Insight

> Python avoids creating duplicate objects for commonly used immutable values.

---

## 8. Identity vs Equality

- `==` → compares values
- `is` → compares memory identity

```python
a = [1, 2]
b = a

a == b  # True
a is b  # True
```

---

## 9. Assignment Does Not Copy Data

```python
a = [1, 2, 3]
b = a
```

- Both variables point to same object
- No duplication occurs

### Copying Methods:

- Shallow copy: `copy()`, slicing
- Deep copy: `copy.deepcopy()`

---

## 10. Common Pitfall: Mutable Default Arguments

```python
def func(lst=[]):
    lst.append(1)
    return lst
```

### Problem:

- Default list is created once
- Shared across function calls

### Correct Approach:

```python
def func(lst=None):
    if lst is None:
        lst = []
```

---

## 11. Performance Insights

### String Concatenation

- Strings are immutable → repeated concatenation creates new objects
- Inefficient in loops

Better:

```python
"".join(list_of_strings)
```

---

### Lookup Efficiency

- list → O(n)
- set/dict → O(1) average

---

## 12. Type Checking Best Practice

Avoid:

```python
type(x) == int
```

Prefer:

```python
isinstance(x, int)
```

---

## 13. Naming Conventions (PEP 8)

- snake_case → variables/functions
- PascalCase → classes
- UPPER_CASE → constants

### Key Insight

> Clean naming improves readability and reduces cognitive load.

---

## 14. Key Mental Model

### Final Mental Model of Python Memory

- Variables = references
- Objects = stored in heap
- Memory managed automatically
- Mutability controls whether objects are modified or replaced
- GC handles cycles
- Interning improves efficiency

---

## 15. Most Important Takeaways

- Python is fully object-based
- Memory is abstracted away but follows predictable rules
- Mutability is the most critical concept for real-world behavior
- Reference vs value distinction explains most Python bugs
- Understanding memory model improves debugging and performance design
