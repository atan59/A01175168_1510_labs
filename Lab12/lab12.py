"""Create a student class. Done by: Michelle and Amy Set E"""


class Student:
    students = "A00000000"

    def __init__(self, first_name, last_name, list_of_classes, middle_name=""):
        self.__first_name = first_name.title()
        self.__middle_name = middle_name.title()
        self.__last_name = last_name.title()
        self.__student_number = Student.students
        self.__list_of_classes = list_of_classes
        length_number = len(Student.students[1:]) - len(str(int(Student.students[1:]) + 1))
        Student.students = "A" + Student.students[1:length_number] + str(int(Student.students[length_number:]) + 1)

    def get_gpa(self):
        """Calculate the student's gpa."""
        gpa = 0
        for course in self.__list_of_classes.keys():
            gpa += self.__list_of_classes[course]
        gpa = gpa / len(self.__list_of_classes)
        return round(gpa, 1)

    def get_student_info(self):
        """Format the student's information."""
        if self.__middle_name == "":
            return (str(self.__first_name) + " " + str(self.__last_name) + " (" + str(self.__student_number) + ") has taken "
                    + str(len(self.__list_of_classes)) + " courses and has a gpa of " + str(self.get_gpa()) + ".")
        else:
            return (str(self.__first_name) + " " + str(self.__middle_name) + " " + str(self.__last_name) + " ("
                    + str(self.__student_number) + ") has taken " + str(len(self.__list_of_classes))
                    + " courses and has a gpa of " + str(self.get_gpa()) + ".")

    def change_last_name(self, new_last_name):
        """Change student's last name."""
        self.__last_name = new_last_name

    def add_course(self, course_name, gpa_earned):
        """Add a single course to list_of_classes."""
        self.__list_of_classes[course_name] = gpa_earned


def main():
    """Instantiate students"""
    student1 = Student("Nicole", "Brooks", {"COMP 1510": 95, "COMP 1113": 87, "COMP 1536": 94},
                       middle_name="Paige")
    student2 = Student("Cornelius", "Smith", {"COMM1116": 45, "COMP 1930": 65, "COMP 1712": 75})
    student3 = Student("Harold", "Finch", {"COMP 1510": 37, "COMP 1712": 40, "COMM 1116": 0})

    """Test get_gpa method"""
    print(student1.get_gpa())
    print(student2.get_gpa())
    print(student3.get_gpa())

    """Test get_student_info"""
    print(student1.get_student_info())
    print(student2.get_student_info())
    print(student3.get_student_info())

    """Test change_last_name"""
    student1.change_last_name("Wang")
    student2.change_last_name("Brooks")
    student3.change_last_name("Doe")
    print(student1.get_student_info())
    print(student2.get_student_info())
    print(student3.get_student_info())

    """Test add_course"""
    student1.add_course("COMP 1100", 100)
    student2.add_course("COMP 1100", 100)
    student3.add_course("COMP 1100", 0)
    print(student1.get_student_info())
    print(student2.get_student_info())
    print(student3.get_student_info())


if __name__ == "__main__":
    main()
