class Course:
    def __init__(self, students, namec, trainer, topics, room):
        self.students = students
        self.namec = namec
        self.trainer = trainer
        self.topics = topics
        self.room = room


x = Course(True, "DATA", "Isabella", "Variables, types, operators", "Flexibility")
print(x.topics)



class Student:
    def __init__(self, name, height, sex, age, background):
        self.name = name
        self.height = height
        self.sex = sex
        self.age = age
        self.background = background



eim = Student("Eimantas", "193", "M", "25", "Maths")
laur = Student("Laura", "172", "F", "26", "Engineering")
iman = Student("Iman", "165", "F", "23", "Maths")
alun = Student("Alun", "178", "M", "28", "Physics")
rigi = Student("Reagan", "198", "M", "24", "Maths")
mar = Student("Mariam", "160", "F", "24", "Maths")

