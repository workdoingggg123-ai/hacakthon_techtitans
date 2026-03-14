import numpy as np

class UniversityResultSystem:

    def __init__(self):
        self.admin_user = "meet"
        self.admin_password = "17072007"

        self.student_names = []
        self.marks = None
        self.subject_no = 0

    # ---------------- LOGIN SYSTEM ----------------

    def login(self):
        print("\n===== UNIVERSITY ADMIN LOGIN =====")

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == self.admin_user and password == self.admin_password:
            print("\nLogin Successful ✅")
            return True
        else:
            print("\nInvalid login ❌")
            return False

    # ---------------- ENTER STUDENT DATA ----------------

    def enter_student_data(self):

        student_no = int(input("\nEnter number of students: "))
        self.subject_no = int(input("Enter number of subjects: "))

        all_marks = []

        for i in range(student_no):

            name = input(f"\nEnter name of student {i+1}: ")
            self.student_names.append(name)

            student_marks = []

            print(f"Enter marks for {name}")

            for j in range(self.subject_no):
                m = int(input(f"Subject {j+1}: "))
                student_marks.append(m)

                all_marks.append(student_marks)

        self.marks = np.array(all_marks)

        print("\nMarks Successfully Entered ✅")

    # ---------------- SHOW RESULT TABLE ----------------

    def show_results(self):

        if self.marks is None:
            print("No data available.")
            return

        print("\n===== RESULT TABLE =====")

        for i, name in enumerate(self.student_names):

            print(f"\nStudent: {name}")
            print("Marks:", self.marks[i])

            total = np.sum(self.marks[i])
            avg = np.mean(self.marks[i])

            print("Total:", total)
            print("Average:", round(avg,2))

            if avg >= 50:
                print("Status: PASS")
            else:
                print("Status: FAIL")

    # ---------------- FIND TOPPER ----------------

    def topper(self):

        if self.marks is None:
            print("No data available.")
            return

        totals = np.sum(self.marks, axis=1)

        topper_index = np.argmax(totals)

        print("\n===== TOPPER =====")
        print("Name:", self.student_names[topper_index])
        print("Total Marks:", totals[topper_index])

    # ---------------- SUBJECT AVERAGE ----------------

    def subject_average(self):

        if self.marks is None:
            print("No data available.")
            return

        print("\n===== SUBJECT AVERAGES =====")

        averages = np.mean(self.marks, axis=0)

        for i, avg in enumerate(averages):
            print(f"Subject {i+1} Average:", round(avg,2))


    def search_student(self):

     name = input("Enter student name: ")

     if name in self.student_names:
        index = self.student_names.index(name)

        print("Marks:", self.marks[index])
        print("Total:", np.sum(self.marks[index]))
        print("Average:", np.mean(self.marks[index]))
     else:
        print("Student not found")       

    # ---------------- MENU SYSTEM ----------------

    def menu(self):

        while True:

            print("\n===== UNIVERSITY RESULT PORTAL =====")
            print("1. Enter Student Marks")
            print("2. View Results")
            print("3. Find Topper")
            print("4. Subject Averages")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.enter_student_data()

            elif choice == "2":
                self.show_results()

            elif choice == "3":
                self.topper()

            elif choice == "4":
                self.subject_average()

            elif choice == "5":
                self.search_student()    

            elif choice == "6":
                print("Exiting system...")
                break

            else:
                print("Invalid option")


# ---------------- MAIN PROGRAM ----------------

system = UniversityResultSystem()

if system.login() == True:
    system.menu()