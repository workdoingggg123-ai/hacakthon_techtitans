import numpy as np

class student:
    def adding_marks(self):
        
        my_marks = []
        S_name = []
        student_no = int(input("give the  number of the student : "))
        subject_no = int(input("give the subject no to enter the marks : "))
        for i in range(student_no):
           student_name = input(f"give the name of the students {i+1}: ")
           S_name.append(student_name)
           
        
        
        for item in (S_name):
             print(f"enter the marks of the {item} : ")
 
        
             student_marks = []
             for l in range(subject_no):

                marks_stu = int(input(f"GIVE THE MAKRS OF THE SUBJECT {l+1} : "))
                student_marks.append(marks_stu)

             my_marks.append(student_marks)


        marks = np.array(my_marks)
        print(marks)


       

enter_marks = student()
enter_marks.adding_marks()
