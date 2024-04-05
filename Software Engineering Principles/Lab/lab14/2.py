class University:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.programs = []

class Program:
    def __init__(self, level, name, start):
        self.level = level
        self.name = name
        self.start = start
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)

    def getCourse(self, name):
        for course in self.courses:
            if course.name == name:
                return course
        return None

class Lecture:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def getCourse(self):
        return self.courses
        
class Student:
    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.takes = []

class Course:
    def __init__(self, credit, id, lecturer, name, semester, student_list):
        self.credit = credit
        self.id = id
        self.lecturer = lecturer
        self.name = name
        self.semester = semester
        self.student_list = []
        self.takes = []

    def enroll(self, student):
        self.student_list.append(student)
        self.takes.append(Takes())

    def getCredit(self):
        return self.credit

    def getLecturer(self):
        return self.lecturer

    def getStudents(self):
        return self.student_list

class Takes:
    def __init__(self, grade, scores, student, course):
        self.grade = grade
        self.scores = scores
        self.student = student
        self.course = course

class Transcript:
    def __init__(self, complete, issue_date):
        self.complete = complete
        self.issue_date = issue_date
        self.takes = []

    def printTranscript(self):
        print("Transcript")
        print("Issue Date: " + self.issue_date)
        print("Complete: " + self.complete)
        for take in self.takes:
            print("Course: " + take.course.name)
            print("Grade: " + take.grade)
            print("Scores: " + take.scores)