class StudentGrades:
    def __init__(self, n, m):
        self.student_name = n
        self.__marks = m

    def add_marks(self, score):
        if(score < 0 or score > 100):
            print("invalid score!")
        else:
            self.__marks = score

    def get_marks(self):
        return self.__marks
    
a = StudentGrades("Hammad", 50)
a.add_marks(75)
print("Updated marks:", a.get_marks())