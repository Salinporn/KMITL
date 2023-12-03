import persistent

class Course(persistent.Persistent):
    def __init__(self, id, name = "", credit = 0):
        self.id = id
        self.name = name
        self.credit = credit

    def __str__(self):
        return "ID: %8s Course Name: %s, Credit: %d" % (str(self.id), self.name, self.credit)
    
    def setName(self, name):
        self.name = name

    def printDetail(self):
        print(self.__str__())

class Student(persistent.Persistent):
    def __init__(self, enrolls = [], id="", name = ""):
        self.enrolls = enrolls
        self.id = id
        self.name = name
    
    def enrollCourse(self, course):
        self.enrolls.append(course)

    def getEnrollment(self, course):
        return self.enrolls
    
    def getGPA(self):
        total = 0
        for e in self.enrolls:
            credit = e.course.credit
            if e.grade == "A":
                total += 4 * credit
            elif e.grade == "B":
                total += 3 * credit
            elif e.grade == "C":
                total += 2 * credit
            elif e.grade == "D":
                total += 1 * credit
            else:
                total += 0
        return total / self.getTotalCredit()
    
    def getTotalCredit(self):
        total = 0
        for e in self.enrolls:
            total += e.course.credit
        return total
    
    def printTranscript(self):
        print("Transcript")
        print("Student ID: %s, Name: %s" % (str(self.id), self.name))
        print("Course list")
        for e in self.enrolls:
            print(e)
        print("Total GPA is: %.2f" % self.getGPA())

    def setName(self, name):
        self.name = name

class Enrollment(persistent.Persistent):
    def __init__(self, course, student, grade = ""):
        self.course = course
        self.student = student
        self.grade = grade

    def __str__(self):
        return "ID: %8s Course: %s, Credit: %s, Grade: %s" % (str(self.course.id) , self.course.name, self.course.credit, self.grade)

    def getCourse(self):
        return self.course

    def printDetail(self):
        print(self.__str__())

    def setGrade(self, grade):
        self.grade = grade