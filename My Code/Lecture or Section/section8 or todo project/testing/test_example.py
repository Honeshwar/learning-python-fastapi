import pytest

# def test_equal_or_not():
#     assert 3==3
#     assert 3==1
#     assert 4>3

#     assert isinstance('sd',str)
#     assert not isinstance('3',int)
#     assert type('int' is str)
#     assert ('4'==4 ) is False

#     num_list = [1,2,3]
#     assert 1 in num_list
#     assert 8 not in num_list
#     assert all(num_list)
#     assert not any(num_list)


class Student:


    def __init__(self,name,age,mobile) -> None:
        self.name =name
        self.age=age
        self.mobile= mobile




@pytest.fixture
def default_student():
    return Student("Honeshwar",'23','8580543245')



def test_initialization_of_student(default_student):
    assert default_student.name == 'Honeshwar'
    assert default_student.age == '23'
    assert default_student.mobile == '8580543245'