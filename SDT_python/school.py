class Student:
    def __init__(self, name, cls, id):
        self.name = name
        self.cls = cls
        self.id = id

    def __repr__(self):
        return f'Student with name: {self.name}, class: {self.cls}, id: {self.id}'
    

class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f'Teacher: {self.name}, Subject: {self.subject}'


class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'not enough'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money {fee - 6500}'

    def __repr__(self):
        print('Welcome to', self.name)

        print('-----Our Teachers------')
        for teacher in self.teachers:
            print(teacher)

        print('-----Our Students------')
        for student in self.students:
            print(student)

        return 'All Done' # must return a string

school1 = School('Phitron')
school1.enroll('alia', 5200)
school1.enroll('koba', 8200)
school1.enroll('sikder', 6500)
school1.enroll('swarup', 6500)
school1.add_teacher('Tom', 'SDT')
school1.add_teacher('JM', 'Python')
school1.add_teacher('Pias', 'Django')

print(school1)