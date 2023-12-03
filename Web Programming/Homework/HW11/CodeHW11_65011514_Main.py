import ZODB, ZODB.FileStorage
import BTrees._OOBTree
from CodesHW11_65011514 import *

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()

root = connection.root

root.course = BTrees.OOBTree.BTree()
root.student = BTrees.OOBTree.BTree()

grading=[
    {"Grade": "A", "min": 80, "max": 100},
    {"Grade": "B", "min": 70, "max": 79},
    {"Grade": "C", "min": 60, "max": 69},
    {"Grade": "D", "min": 50, "max": 59},
    {"Grade": "F", "min": 0, "max": 49}
]

root.course[101] = Course(101, 'Computer Programming', 4, grading)
root.course[201] = Course(201, 'Web Programming', 4, grading)
root.course[202] = Course(202, 'Software Engineering Principle', 5, grading)
root.course[301] = Course(301, 'Artificial Intelligence', 3, grading)

root.student[1] = Student([], id=1101, name='Mr. Name ForExample')
root.student[1].enrollCourse(Enrollment(root.course[101], root.student[1], 75))
root.student[1].enrollCourse(Enrollment(root.course[201], root.student[1], 81))
root.student[1].enrollCourse(Enrollment(root.course[202], root.student[1], 81))
root.student[1].enrollCourse(Enrollment(root.course[301], root.student[1], 57))

def retrieveCourse(id):
    return root.course[id]

if __name__ == '__main__':
    course = root.course
    for c in course:
        courses = course[c]
        courses.printDetail()
    print()

    student = root.student
    for s in student:
        students = student[s]
        students.printTranscript()
    print()
