from lib.student import Student

class Coach:
    # User-facing properties:
    #   name: string
    #   students: list of instances of Student

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side-effects:
        #   Sets the name property and initializes students to an empty list
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        self.name = name
        self.students = []

    def add_student(self, student):
        # Parameters:
        #   student: an instance of Student
        # Side-effects:
        #   Adds the student to the students property
        if not isinstance(student, Student):
            raise TypeError("Student must be a Student object!")
        self.students.append(student)

    def count_submissions(self):
        # Returns:
        #   The integer sum of submissions from all students the coach manages. (Delegation)
        total = sum([student.count_submissions() for student in self.students])

        return total
    def print_student_names(self):
        # Returns:
        #   A string of all student names, separated by ", "
        # return self.students[0].name
        return ", ".join([student.name for student in self.students])
    
    def upload_submission_for_students(self, submission):
        # Parameters:
        #   submission: string (name of the assignment/challenge)
        # Side-effects:
        #   Calls student.add_submission(submission) on every student the coach manages. (Delegation)

        if not isinstance(submission, str):
            raise TypeError("Please provide a string!")
        for student in self.students:
            student.add_submission(submission)
            # mockstudent.add_submission.asssert_called_with(...arg)