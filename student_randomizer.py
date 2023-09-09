# ---------------------------------------------------------
#                          NOTES
# ---------------------------------------------------------
"""
Dieter Steinhauser
EEL3923C Design 1 TA tools
Grading Randomizer


    - Read in students from the class.csv
    - create student dictionary
    - create function to pick X amount of students at random
    - allow to filter by group



"""
# ---------------------------------------------------------
#                         INCLUDES
# ---------------------------------------------------------
from pprint import pprint
import random
from helpers import *


# ---------------------------------------------------------
#                          METHODS
# ---------------------------------------------------------


@dataclass
class StudentData:
    """Class for holding student data"""
    name: str
    group: int

def get_students():
    """Reads the student CSV in the directory and returns a list of student objects."""

    # Read the student CSV 
    student_csv =  current_dir.joinpath('D1_students.csv')
    csv_dict = read_csv_data(student_csv)

    # Remove header data (probably needs to change for different CSV's)
    csv_dict.pop(1)
    csv_dict.pop(2)

    students = []

    # parsing the student name and group
    for student_line in csv_dict.values():

        # read the students name and flip it so it is 'first last'
        parsed_name = student_line[0].split(', ')
        full_name = ' '.join(reversed(parsed_name))

        # Determine the group of the students (probably needs to change for different CSV's)
        group =  1 if "Group1" in student_line[4] else 2
            
        student = StudentData(full_name, group)
        students.append(student)

    return students


def pick_students(stu_list: list, num_students: int, group: int = None):
    """
    Picks X amount of students at random. Can be filtered by group.

    :param stu_list: List of student objects with name and group.
    :type stu_list: list
    :param num_students: Number of students to pick
    :type num_students: int
    :param group: Group number for filtering, defaults to None
    :type group: int, optional
    """
    
    # check if the group is being filtered
    if group is not None:
        stu_list = [student for student in stu_list if student.group == group]


    random_students = []        
    for index in range(num_students):

        # Randomly select the students.    
        student = random.choice(stu_list)
        random_students.append(student)

        # remove the student from the selection pool.
        stu_list.remove(student)

    return random_students





# ---------------------------------------------------------
#                          MAIN
# ---------------------------------------------------------


if __name__ == "__main__":
    print(current_dir)
    students = get_students()


    
    group1 = [stu for stu in students if stu.group == 1]
    group2 = [stu for stu in students if stu.group == 2]

    # pprint(students)
    # print()

    # pprint(group1)
    # pprint(len(group1))
    # print()

    # pprint(group2)
    # pprint(len(group2))
    # print()

    random_students = pick_students(students, num_students=10, group=2)
    pprint(random_students)




# ---------------------------------------------------------
#                       END OF FILE
# ---------------------------------------------------------



