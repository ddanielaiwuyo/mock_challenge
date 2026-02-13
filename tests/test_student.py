"""
This test suite uses the testdox plugin for pytest,
which provides the mark.it decorator.

Use the --testdox flag, e.g. pytest --testdox [test path]
"""


from pytest import mark, raises, fixture

from lib.student import Student


@fixture
def valid_student():
    return Student("Bill Evans")


class TestInit:
    @mark.it("Sets the name property to the passed arg")
    def test_init_name(self, valid_student):
        assert valid_student.name == "Bill Evans"

    @mark.it("Initializes submissions to an empty list")
    def test_init_empty_submission(self, valid_student):
        assert valid_student.submissions == []

    @mark.it("Raises TypeError if name not str")
    def test_raises_type_err(self):
        student = {'name': 'Bill Evans', 'instrument': 'piano'}

        with raises(TypeError, match="name must be string"):
            Student(student)


class TestAddSubmission:
    @mark.it("Adds the submission to the submissions list")
    def test_adds(self, valid_student):
        valid_student.add_submission("Homework")
        assert valid_student.submissions == ["Homework"]
        valid_student.add_submission("Coursework")
        assert valid_student.submissions == ["Homework", "Coursework"]

    @mark.it("Raises a TypeError('submission must be string') if submission not str")      
    def test_raise_ty_err(self, valid_student):
        with raises(TypeError, match="submission must be string"):
            valid_student.add_submission(None)


class TestCountSubmissions:
    @mark.it("Returns len of .submissions")
    def test_count(self, valid_student):
        valid_student.add_submission("Homework")
        assert valid_student.count_submissions() == 1
        valid_student.add_submission("Coursework")
        assert valid_student.count_submissions() == 2  