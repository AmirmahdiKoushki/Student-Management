import numpy as np

class Person(object):
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name


    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, new_last_name):
        self._last_name = new_last_name
    
    @property
    def age(self):
        return self._age 
    @age.setter
    def age(self, new_age):
        if new_age < 0 or new_age > 150:
            raise ValueError("age of a person must be positive.")
        self._age = new_age

    def __str__(self):
        return f"First name:{self.name}, Last name:{self.last_name}, Age:{self.age}"

class Student(Person):
    student_number = 0
    def __init__(self, name, last_name, age, student_id, major, term, courses_grades):
        super().__init__(name, last_name, age)
        self.student_id = student_id
        self.major = major
        self.term = term
        self.courses_grades = courses_grades
        Student.student_number += 1

    @staticmethod
    def vaild_grade(grade):
        return isinstance(grade, (int, float)) and (0 <= grade <= 20)

    @property
    def student_id(self):
        return self._student_id
    @student_id.setter
    def student_id(self, new_id):
        if not isinstance(new_id, str):
            raise TypeError("student id must be string")
        if not new_id.isdigit():
            raise ValueError("student id must only have digits")
        if len(new_id) != 8:
            raise ValueError("student id must be 8 digits")
        self._student_id = new_id

    @property
    def major(self):
        return self._major
    @major.setter
    def major(self, new_major):
        if not isinstance(new_major,str):
            raise TypeError("major must be string")
        self._major = new_major
    
    @property
    def term(self):
        return self._term
    @term.setter
    def term(self, new_term):
        if not isinstance(new_term, int):
            raise TypeError("number of term must be integer")
        if new_term <= 0 or new_term > 20:
            raise ValueError("number of term must be positive")
        self._term = new_term

    @property
    def courses_grades(self):
        return self._courses_grades
    @courses_grades.setter
    def courses_grades(self, new_courses_grades):
        if not isinstance(new_courses_grades, dict):
            raise TypeError("courses_grades must be a dict")
        for course, grade in new_courses_grades.items():
            if not isinstance(course, str):
                raise TypeError("course must be a string")
            if not Student.vaild_grade(grade):
                 raise ValueError("grades must be number between 0,20")
        self._courses_grades = new_courses_grades

    def __str__(self):
        return f"First name:{self.name}\n Last name:{self.last_name}\n Age:{self.age}\n student_id:{self.student_id}\n major:{self.major}\n term:{self.term}"
class Course(object):
    def __init__(self, course_name, course_unit, teacher):
        self.course_name = course_name
        self.course_unit = course_unit
        self.teacher = teacher

    @property
    def course_name(self):
        return self._course_name
    @course_name.setter
    def course_name(self, new_course_name):
        if not isinstance(new_course_name, str):
            raise TypeError("course name must be string")
        self._course_name = new_course_name

    @property
    def course_unit(self):
        return self._course_unit
    @course_unit.setter
    def course_unit(self, new_course_unit):
        if not isinstance(new_course_unit, int):
            raise TypeError("course unit must be integer")
        if not (new_course_unit >= 1 and new_course_unit <= 4):
            raise ValueError("min and max for course unit are 1 and 4.")
        self._course_unit = new_course_unit

    @property
    def teacher(self):
        return self._teacher
    @teacher.setter
    def teacher(self, new_teacher):
        if not isinstance(new_teacher, str):
            raise TypeError("teacher's name must be string")
        self._teacher = new_teacher

    def __str__(self):
        return f"course's name:{self.course_name}, course's unit:{self.course_unit}, teacher:{self.teacher}"

class EducationSystem(object):
    def __init__(self):
        self.students_list = []
        self.courses_list = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("student must be a Student object")
        for i in self.students_list:
            if i.student_id == student.student_id:
                raise ValueError("student exists")
        self.students_list.append(student)

    def remove_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("student must be a Student object")
        for i in self.students_list:
            if i.student_id == student.student_id:
                self.students_list.remove(i)
                return
        raise ValueError("this student doesnt exist")

    def add_course(self, course):
        if not isinstance(course, Course):
            raise TypeError("course must be a Course object")
        for i in self.courses_list:
            if i.course_name == course.course_name:
                raise ValueError("this course exists")
        self.courses_list.append(course)
    
    def find_student(self, std_id):
        for student in self.students_list:
            if student.student_id == std_id:
                return student
        raise ValueError("this student doesnt exist")

    def find_course(self, crs_name):
        for course in self.courses_list:
            if course.course_name == crs_name:
                return course
        raise ValueError("this course doesnt exist")

    def add_grade(self, std_id, course_name, grade):
        student = self.find_student(std_id)
        course = self.find_course(course_name)
        if not Student.vaild_grade(grade):
            raise ValueError("grades must be number between 0,20")    
        student.courses_grades[course.course_name] = grade

    def calculate_gpa(self, std_id):
        student = self.find_student(std_id)
        total_sum = 0
        sum_units = 0
        for course_name, grade in student.courses_grades.items():
            crs = self.find_course(course_name)
            total_sum += (grade*crs.course_unit)
            sum_units += crs.course_unit
        if sum_units == 0:
            raise ValueError("this student has no course")
        gpa = total_sum / sum_units
        return gpa

    def show_transcript(self, std_id):
        student = self.find_student(std_id)
        print(student)
        for course_name, grade in student.courses_grades.items():
            print(f"{course_name}: {grade}")
        print(f"GPA: {self.calculate_gpa(std_id):.2f}")
    
    def sort_students(self):
        """
        Bubble Sort:

        Time Complexity: O(n²)
        Because the algorithm uses two nested loops.
        """
        
        n = len(self.students_list)
        for i in range(n-1):
            for j in range(n - i -1):
                if self.calculate_gpa(self.students_list[j].student_id) < self.calculate_gpa(self.students_list[j+1].student_id):
                    self.students_list[j], self.students_list[j+1] = self.students_list[j+1], self.students_list[j]
        return self.students_list            
                    
    def students_analys(self):
        grades = []
        for student in self.students_list:
            for _, grade in student.courses_grades.items():
                grades.append(grade)

        grades = np.array(grades)
        class_mean = np.mean(grades)
        max_grade = np.max(grades)
        min_grade = np.min(grades)
        std_grade = np.std(grades)

        gpas = []
        for student in self.students_list:
            gpas.append(self.calculate_gpa(student.student_id))
        
        gpas = np.array(gpas)
        bool_mask = gpas >= 10
        accepted_gpas = gpas[bool_mask]
        pass_students = len(accepted_gpas)
        fail_students = len(gpas) - len(accepted_gpas)

        return class_mean, max_grade, min_grade, std_grade, pass_students, fail_students





#test_cases:

system = EducationSystem()

#Courses
math2 = Course("Mathematics 2", 4, "Zakeri")
physics = Course("Physics", 3, "Afshari")
advanced_programming = Course("Advanced Programming", 4, "Ahmadi")
probability = Course("Probability", 3, "Malekzadeh")
linear_algebra = Course("Linear Algebra", 4, "Haghighi")
thought1 = Course("Islamic Thought 1", 2, "Aghabeigi")

system.add_course(math2)
system.add_course(physics)
system.add_course(advanced_programming)
system.add_course(probability)
system.add_course(linear_algebra)
system.add_course(thought1)

#Students
Ali = Student("Ali", "Mohammadi", 20, "40412345", "Computer Science", 3, {})
Sara = Student("Sara", "Ahmadi", 21, "40412346", "Computer Science", 4, {})
Amirmahdi = Student("Amirmahdi", "Koushki", 20, "40422533", "Computer Science", 3, {})
Zahra = Student("Zahra", "Moradi", 20, "40412348", "Computer Science", 2, {})

system.add_student(Ali)
system.add_student(Sara)
system.add_student(Amirmahdi)
system.add_student(Zahra)

#Ali
system.add_grade("40412345", "Mathematics 2", 17)
system.add_grade("40412345", "Physics", 15)
system.add_grade("40412345", "Advanced Programming", 18)
system.add_grade("40412345", "Probability", 16)
system.add_grade("40412345", "Linear Algebra", 17)
system.add_grade("40412345", "Islamic Thought 1", 19)

#Sara
system.add_grade("40412346", "Mathematics 2", 13)
system.add_grade("40412346", "Physics", 12)
system.add_grade("40412346", "Advanced Programming", 15)
system.add_grade("40412346", "Probability", 14)
system.add_grade("40412346", "Linear Algebra", 11)
system.add_grade("40412346", "Islamic Thought 1", 18)

#Amirmahdi
system.add_grade("40422533", "Mathematics 2", 20)
system.add_grade("40422533", "Physics", 20)
system.add_grade("40422533", "Advanced Programming", 20)
system.add_grade("40422533", "Probability", 20)
system.add_grade("40422533", "Linear Algebra", 20)
system.add_grade("40422533", "Islamic Thought 1", 20)

#Zahra
system.add_grade("40412348", "Mathematics 2", 6)
system.add_grade("40412348", "Physics", 8)
system.add_grade("40412348", "Advanced Programming", 7)
system.add_grade("40412348", "Probability", 9)
system.add_grade("40412348", "Linear Algebra", 8)
system.add_grade("40412348", "Islamic Thought 1", 10)

print("========== TRANSCRIPTS ==========")
for student in system.students_list:
    system.show_transcript(student.student_id)
    print("-" * 40)
       

print("========== SORTED STUDENTS ==========")

system.sort_students()

for student in system.students_list:
    print(f"{student.name} {student.last_name} ===> GPA: {system.calculate_gpa(student.student_id):.2f}")

print("========== CLASS ANALYS ==========")

mean, max_grade, min_grade, std, passed, failed = system.students_analys()

print(f"Class Mean: {mean:.2f}")
print(f"Highest Grade: {max_grade}")
print(f"Lowest Grade: {min_grade}")
print(f"Standard Deviation: {std:.2f}")
print(f"Passed Students: {passed}")
print(f"Failed Students: {failed}")











