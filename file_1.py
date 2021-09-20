class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in \
                lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def student_grade(self, grade):
        all_grades = sum(list(self.grades.values()), [])
        average_grade = round(sum(all_grades) / len(all_grades), 1)
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: \
{self.student_grade(self.grades)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\n\
Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.student_grade(self.grades) < other.student_grade(other.grades)


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lecturer_grade(self, grades):
        all_grades = sum(list(self.grades.values()), [])
        average_grade = round(sum(all_grades)/len(all_grades), 1)
        return average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: \
{self.lecturer_grade(self.grades)}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not in Lecturer')
            return
        return self.lecturer_grade(self.grades) < other.lecturer_grade(other.grades)


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


some_student = Student('Ruoy', 'Eman', 'man')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
student_1 = Student('Tom', 'Ford', 'man')
student_1.courses_in_progress += ['Python', 'Git', 'Java']
student_1.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']
lecturer_1 = Lecturer('Ann', 'Hofman')
lecturer_1.courses_attached += ['Python', 'Java']

some_student.rate_lecturer(lecturer_1, 'Python', 4)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Java', 5)
some_student.rate_lecturer(some_lecturer, 'Git', 8)
student_1.rate_lecturer(some_lecturer, 'Git', 7)
some_student.rate_lecturer(some_lecturer, 'Python', 6)
student_1.rate_lecturer(some_lecturer, 'Python', 9)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git', 'Java']
reviewer_1 = Reviewer('Nick', 'Jordan')
reviewer_1.courses_attached += ['Python', 'Java']

some_reviewer.rate_hw(some_student, 'Python', 3)
some_reviewer.rate_hw(student_1, 'Python', 5)
some_reviewer.rate_hw(student_1, 'Java', 9)
some_reviewer.rate_hw(student_1, 'Git', 4)
some_reviewer.rate_hw(some_student, 'Git', 6)
reviewer_1.rate_hw(some_student, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Java', 7)

print(some_reviewer)
print(some_lecturer)
print(some_student)

print(some_student < student_1)
print(some_lecturer < lecturer_1)


list_students = [some_student, student_1]
list_lecturer = [some_lecturer, lecturer_1]


def av_student_grade(student, course):
    all_grades = 0
    count_grades = 0
    for student in list_students:
        for k, v in student.grades.items():
            if k == course:
                for grade in v:
                    all_grades += grade
                    count_grades += 1
    result = round(all_grades / count_grades, 2)
    return result


def av_lecturer_grade(lecturer, course):
    all_grades = 0
    count_grades = 0
    for lecturer in list_lecturer:
        for k, v in lecturer.grades.items():
            if k == course:
                for grade in v:
                    all_grades += grade
                    count_grades += 1
    result = round(all_grades / count_grades, 2)
    return result


print(av_student_grade(list_students, 'Java'))
print(av_lecturer_grade(list_lecturer, 'Python'))
