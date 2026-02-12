# 🧑‍🏫 Coach & Student Management System

This project demonstrates a simple multi-class system in Python, built with clean Object-Oriented Programming (OOP) principles and comprehensive testing. It is structured for learners to practice class design, composition, and testing strategies.

## 🚀 Learning Objectives

By working through this project and its tests, you will learn to:

1.  **Object-Oriented Design (OOP):** Create and manage two distinct classes, `Student` and `Coach`, each with specific responsibilities.
2.  **Composition (Has-a Relationship):** Understand how one class (`Coach`) can **own** or manage instances of another class (`Student`)—the "has-a" relationship.
3.  **Method Delegation:** See how the `Coach` delegates tasks (like counting submissions) to the `Student` objects it manages.
4.  **Unit vs. Integration Testing:** Differentiate between:
    * **Unit Tests:** Testing a single class in isolation (using `unittest.mock.Mock` to simulate the other class).
    * **Integration Tests:** Testing that the real classes work correctly together.

## 📂 Project Structure
```bash
.
├── lib/
│   ├── coach.py        # Contains the Coach class
│   └── student.py      # Contains the Student class
└── tests/
    ├── test_student.py           # Unit tests focused on the Student class
    ├── test_coach.py             # Unit tests focused on the Coach class (uses Mocks)
    └── test_integration_student_coach.py # Tests the interaction between Student and Coach classes
```
---

## 💻 How to Run the Code

To explore the classes and their methods, you can use the Python interactive shell (REPL) directly from your terminal.

First, navigate to the root of the project directory.

### Step 1: Testing the `Student` Class (Isolation)

The `Student` class is responsible for managing its own name and submissions.

1.  Start the Python shell:

    ```bash
    python # or python3
    ```

2.  Import the class and create an instance:

    ```python
    >>> from lib.student import Student
    >>> student = Student("Asha")
    >>> student.name
    'Asha'
    >>> student.submissions
    []
    ```

3.  Test the core functionality:

    ```python
    >>> student.add_submission("challenge-01-oop")
    >>> student.add_submission("challenge-02-testing")
    >>> student.submissions
    ['challenge-01-oop', 'challenge-02-testing']
    >>> student.count_submissions()
    2
    ```

### Step 2: Testing the `Coach` Class (Composition & Delegation)

The `Coach` class manages a roster of `Student` objects.

1.  Ensure you are still in the Python shell and import the `Coach` class:

    ```python
    >>> from lib.coach import Coach
    >>> coach = Coach("Eddie")
    >>> coach.students
    []
    ```

2.  Add the existing `student` (Asha) and a new one to the roster:

    ```python
    >>> from lib.student import Student
    >>> student2 = Student("Jake")
    >>> coach.add_student(student) # Asha has 2 submissions already
    >>> coach.add_student(student2) # Jake has 0 submissions

    >>> [s.name for s in coach.students]
    ['Asha', 'Jake']
    ```

3.  Test delegated functionality (`count_submissions`):

    The coach asks each student for their count (Asha: 2, Jake: 0) and sums them up.

    ```python
    >>> coach.count_submissions()
    2
    ```

4.  Test batch functionality (`upload_submission_for_students`):

    The coach should add the new submission to *every* student's list.

    ```python
    >>> coach.upload_submission_for_students("new-cohort-submission")

    >>> student.count_submissions() # Asha's count is now 3
    3
    >>> student2.count_submissions() # Jake's count is now 1
    1
    >>> coach.count_submissions() # Total count is now 4
    4
    ```

5.  Test formatting (`print_student_names`):

    This uses a **list comprehension** internally to efficiently gather names.

    ```python
    >>> coach.print_student_names()
    'Asha, Jake'
    ```

---

## 🧪 Running the Tests

The project uses `pytest` for running automated tests.

1.  Run all tests from the project root:

    ```bash
    pytest -xv
    ```

2.  The output will show tests passing for `test_student.py`, `test_coach.py`, and `test_integration_student_coach.py`, confirming all functionality is correct and robustly tested.