from lib.coach import *
from lib.student import Student
from unittest.mock import patch, Mock

from pytest import raises, mark, fixture

@fixture
def valid_coach():
    return Coach("Martin")

class TestInit:
    valid_coach
    @mark.it("Sets the name property for the coach object")
    def test_init(self, valid_coach):
        assert valid_coach.name == "Martin"
    
    @mark.it("Sets the empty list for students")
    def test_init_students(self, valid_coach):
        assert valid_coach.students == []
    

    @mark.it("Raises error against invalid args")
    def test_raises_type_err(self):
        name = None
        
        with raises(TypeError, match="Name must be a string!"):
            Coach(name)


@fixture
def valid_student():
    return Student("Daniel")

class TestAddStudent:
    @mark.it("Appends student to students")
    def test_adds_students(self, valid_coach, valid_student):
        valid_coach.add_student(valid_student)

        assert valid_coach.students == [valid_student]

    @mark.it("Raises TypeError if student not Student Object")
    def test_raises_type_err(self, valid_coach):
        with raises(TypeError, match="Student must be a Student object!"):
            valid_coach.add_student("")


class TestCountSubmissions:
    @mark.it("Calls the count_submissions method all students")
    @patch("lib.coach.isinstance", return_value=True)
    def test_some_func(self, mock_is_instance):
        mock_student = Mock()
        mock_student.count_submissions.return_value = 100

        coach = Coach("Randy Orton")

        coach.add_student(mock_student)
        coach.count_submissions()

        mock_student.count_submissions.assert_called_once()
    

    @mark.it("Counts the submissions of each student")
    @patch("lib.coach.isinstance", return_value=True)
    def test_func2(self, type_ignore):
        mock_student_1 = Mock()
        mock_student_2 = Mock()

        mock_student_1.count_submissions.return_value = 100
        mock_student_2.count_submissions.return_value = 100

        coach = Coach("Gregg")

        coach.add_student(mock_student_1)
        coach.add_student(mock_student_2)

        result = coach.count_submissions()

        assert result == 200
    
@fixture
def valid_students():
    return [
        Student("blahblahblah"),
        Student("whatever"),
        Student("John Coltrane"),
    ]

class TestPrintStudentNames:
    @mark.it("Returns single name if one student")
    # mocking name
    def test_print_student_name(self, valid_coach, valid_student):
        valid_coach.add_student(valid_student)

        expected_result = "Daniel"

        actual_result = valid_coach.print_student_names()
        assert actual_result == expected_result

        
    @mark.it("Returns joined names if multiples students") 
    def test_print_student_name_multiple(self, valid_coach, valid_students):
        for student in valid_students:
            valid_coach.add_student(student)

        expected_result = "blahblahblah, whatever, John Coltrane"
        actual_result = valid_coach.print_student_names()

        assert actual_result == expected_result
        
        
    
class TestUploadSubmissionForStudents:
    @mark.it("Adds submission to students submissions if one student")
    def test_upload_submission_for_student_single(self, valid_coach, valid_student):
        valid_coach.add_student(valid_student)
        valid_coach.upload_submission_for_students("Vinyl Connesieur")

        assert valid_student.submissions == ["Vinyl Connesieur"]
        
    @mark.it("Adds submission to students submissions for multiple students")
    def test_upload_submission_for_student_multiple(self, valid_coach, valid_students):
        for student in valid_students:
            valid_coach.add_student(student)
        

        valid_coach.upload_submission_for_students("Vinyl Connesieur")

        for student in valid_students:
            assert student.submissions == ["Vinyl Connesieur"]
        

    @mark.it("Calls student add submission method with submission argument")
    @patch("lib.coach.isinstance", return_value=True)
    def test_upload_submission_for_student_mock(self, type_ignore, valid_coach):
        mock_student = Mock()
        valid_coach.add_student(mock_student)

        valid_coach.upload_submission_for_students("Mock Testing")
        mock_student.add_submission.assert_called_once_with("Mock Testing")


    @mark.it("Raises TypeError if submission not string")
    def test_upload_submission_for_student_raises_type_err(self, valid_coach):
        with raises(TypeError, match="Please provide a string!"):
            valid_coach.upload_submission_for_students({})
        
    
