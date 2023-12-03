import persistent

class Course(persistent.Persistent):
    def __init__(self, id, name = "", credit = 0, grading=[]):
        self.id = id
        self.name = name
        self.credit = credit
        self.gradeScheme = grading

    def __str__(self):
        return "ID: %8s Course Name: %s, Credit: %d" % (str(self.id), self.name, self.credit)
    
    def setName(self, name):
        self.name = name
    
    def scoreGrading(self, score):
        for g in self.gradeScheme:
            if g["min"] <= score <= g["max"]:
                return g["Grade"]
        return "F"
    
    def setGradeScheme(self, grading):
        for grade_range in grading:
            if not all(key in grade_range for key in ["min", "max", "Grade"]):
                print("Error: Grading scheme format is incorrect.")
                return 
        self.gradeScheme = grading

    def printDetail(self):
        print(self.__str__())

class Student(persistent.Persistent):
    def __init__(self, enrolls = [], id="", name = "", password=""):
        self.enrolls = enrolls
        self.id = id
        self.name = name
        self.password = password

    def login(self, id, password):
        if self.id == id and self.password == password:
            return True
        return False
    
    def enrollCourse(self, course):
        self.enrolls.append(course)

    def getEnrollment(self, course):
        return self.enrolls
    
    def getGPA(self):
        total_points = 0
        total_credits = 0
        for e in self.enrolls:
            credit = e.course.credit
            grade = e.course.scoreGrading(e.score)
            if grade == "A":
                total_points += 4 * credit
            elif grade == "B":
                total_points += 3 * credit
            elif grade == "C":
                total_points += 2 * credit
            elif grade == "D":
                total_points += 1 * credit
            total_credits += credit
        if total_credits == 0:
            return 0
        return total_points / total_credits
    
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
    def __init__(self, course, student, score):
        self.course = course
        self.student = student
        self.score = score

    def __str__(self):
        return "ID: %8s Course: %-32s, Credit: %2s Score: %2s Grade: %2s" % (str(self.course.id) , self.course.name, self.course.credit, self.score, self.course.scoreGrading(self.score))

    def getCourse(self):
        return self.course

    def printDetail(self):
        print(self.__str__())

    def getScore(self):
        return self.score
    
    def getGrade(self):
        return self.course.scoreGrading(self.score)
    
    def setScore(self, score):
        self.score = score
