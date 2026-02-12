# Multi-Class Planned Design Recipe: Coach & Student Management

## 1. Describe the Problem

As a **Coach**, I want to manage a class by being able to:
1.  **Add** new **Student** objects to my roster.
2.  Get a **total count** of all challenge **submissions** made by all students in my class.
3.  **Print a formatted list** of all the student names.
4.  **Upload a new submission** for every student in the class simultaneously.

As a **Student**, I need to be able to:
1.  **Record** a new challenge **submission**.
2.  **Report** my personal **count** of submissions.

---

## 2. Design the Class System

The `Coach` class **has a list of** `Student` objects (composition/aggregation), where the `Coach` delegates the submission counting and submission adding tasks to the `Student` objects.

```
┌────────────────────────────┐
│ Coach(name)                │
│                            │
│ - name                     │
│ - students                 │
│ - add_student(student)     │
│ - count_submissions()      │
│   => total submission count│
│ - print_student_names()    │
│   => "Name1, Name2, ..."   │
│ - upload_submission_for... │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌────────────────────────────┐
│ Student(name)              │
│                            │
│ - name                     │
│ - submissions              │
│ - add_submission(sub)      │
│ - count_submissions()      │
│   => count of submissions  │
└────────────────────────────┘
```
```python
class Student:
    # User-facing properties:
    #   name: string
    #   submissions: list of strings (submission names)

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side-effects:
        #   Sets the name property and initializes submissions to an empty list
        pass

    def add_submission(self, submission):
        # Parameters:
        #   submission: string (name of the assignment/challenge)
        # Side-effects:
        #   Adds the submission to the submissions property
        pass

    def count_submissions(self):
        # Returns:
        #   The integer count of all submissions made by the student.
        pass

class Coach:
    # User-facing properties:
    #   name: string
    #   students: list of instances of Student

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side-effects:
        #   Sets the name property and initializes students to an empty list
        pass

    def add_student(self, student):
        # Parameters:
        #   student: an instance of Student
        # Side-effects:
        #   Adds the student to the students property
        pass

    def count_submissions(self):
        # Returns:
        #   The integer sum of submissions from all students the coach manages. (Delegation)
        pass

    def print_student_names(self):
        # Returns:
        #   A string of all student names, separated by ", "
        pass
    
    def upload_submission_for_students(self, submission):
        # Parameters:
        #   submission: string (name of the assignment/challenge)
        # Side-effects:
        #   Calls student.add_submission(submission) on every student the coach manages. (Delegation)
        pass
```