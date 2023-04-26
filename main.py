class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def get_rate_avg(self):
        avg_per_course = [sum(x) / len(x) for x in self.grades.values()]
        avg = sum(avg_per_course) / len(avg_per_course)
        return avg    

    def __lt__(self, other):
        if isinstance(other, Student):
            if self.get_rate_avg() < other.get_rate_avg():
                return True
            else:
                return False
        
    def __str__(self):
        str_in_progress = ', '.join(self.courses_in_progress)
        str_finished = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_rate_avg()}\nКурсы в процессе изучения: {str_in_progress}\nЗавершенные курсы: {str_finished}"
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_rate_avg(self):
        avg_per_course = [sum(x) / len(x) for x in self.grades.values()]
        avg = sum(avg_per_course) / len(avg_per_course)
        return avg 

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self.get_rate_avg() < other.get_rate_avg():
                return True
            else:
                return False

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_rate_avg()}"

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

# функции avg_students_rate и avg_lecturers_rate выполняют одни и те же действия
# можно создать только одну функцию, представленную ниже и передавать в нее списки
# с объектами разных типов, но оставлю вариант с двумя функциями как и сказанно в задании
# 
# 
# def avg_students_rate(obj_list, course):
#     grades = []
#     for obj in obj_list:
#         if not obj.grades.get(course) is None:
#             grades += obj.grades.get(course)
#     if len(grades) == 0:
#         return 0
#     else:
#         return sum(grades) / len(grades)

def avg_lecturers_rate(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if not lecturer.grades.get(course) is None:
            grades += lecturer.grades.get(course)
    if len(grades) == 0:
        return 0
    else:
        return sum(grades) / len(grades)

def avg_students_rate(students, course):
    grades = []
    for student in students:
        if not student.grades.get(course) is None:
            grades += student.grades.get(course)
    if len(grades) == 0:
        return 0
    else:
        return sum(grades) / len(grades)

mentor1 = Mentor("Name", "Surname")
mentor2 = Mentor("Name1", "Surname1")

lect1 = Lecturer("Petr", "Petrov")
lect1.courses_attached = ["Python", "Git", "C#"]

lect2 = Lecturer("Ivan", "Ivanov")
lect2.courses_attached = ["SQL", "Java", "Java-Script"]

stud1 = Student("Victor", "Sidorov", "M")
stud1.finished_courses = ["Python"]
stud1.courses_in_progress = ["Git", "C#", "Java"]
stud1.rate_lecturer(lect1, "Python", 7)
stud1.rate_lecturer(lect2, "Java", 6)

stud2 = Student("Pavel", "Pavlov", "M")
stud2.finished_courses = ["SQL"]
stud2.courses_in_progress = ["Java", "Java-Script"]
stud2.rate_lecturer(lect2, "Java", 8)
stud2.rate_lecturer(lect2, "SQL", 9)

rev1 = Reviewer("Alexander", "Smirnov")
rev1.courses_attached = ["Git", "Java", "SQL"]
rev1.rate_hw(stud1, "Git", 6)
rev1.rate_hw(stud1, "Java", 7)
rev1.rate_hw(stud2, "Java", 6)

rev2 = Reviewer("Alexey", "Fedorov")
rev2.courses_attached = ["Java-Script", "C#", "Python"]
rev2.rate_hw(stud1, "Python", 8)
rev2.rate_hw(stud2, "Java-Script", 5)
rev2.rate_hw(stud2, "Java-Script", 9)

print(lect1)
print(lect2)
print(f"lect1 < lect2: {lect1 < lect2}")

print(stud1)
print(stud2)
print(f"stud1 < stud2: {stud1 < stud2}")

print(rev1)
print(rev2)

print(avg_students_rate([stud1, stud2], "Java-Script"))
print(avg_lecturers_rate([lect1, lect2], "Java"))