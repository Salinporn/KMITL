import ZODB, ZODB.FileStorage
import persistent
import transaction
import BTrees._OOBTree
from z_enrollment import *

storage = ZODB.FileStorage.FileStorage('mydata.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

root.course = BTrees.OOBTree.BTree()
root.student = BTrees.OOBTree.BTree()

root.course[101] = Course(101, 'Computer Programming', 4)
root.course[201] = Course(201, 'Web Programming', 4)
root.course[202] = Course(202, 'Software Engineering Principle', 5)
root.course[301] = Course(301, 'Artificial Intelligence', 3)

root.student[1] = Student([], id=1101, name='John')
root.student[1].enrollCourse(Enrollment(root.course[101], root.student[1], 'B'))
root.student[1].enrollCourse(Enrollment(root.course[201], root.student[1], 'B'))
root.student[1].enrollCourse(Enrollment(root.course[301], root.student[1], 'C'))

root.student[2] = Student([], id=1102, name='Mary')
root.student[2].enrollCourse(Enrollment(root.course[101], root.student[2], 'A'))
root.student[2].enrollCourse(Enrollment(root.course[201], root.student[2], 'B'))
root.student[2].enrollCourse(Enrollment(root.course[202], root.student[2], 'D'))

root.student[3] = Student([], id=1103, name='Peter')
root.student[3].enrollCourse(Enrollment(root.course[101], root.student[3], 'C'))
root.student[3].enrollCourse(Enrollment(root.course[201], root.student[3], 'A'))
root.student[3].enrollCourse(Enrollment(root.course[202], root.student[3], 'B'))
root.student[3].enrollCourse(Enrollment(root.course[301], root.student[3], 'C'))

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

