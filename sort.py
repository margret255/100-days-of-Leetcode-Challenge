#Function to capture the student details
def Student_details():
    students=[]
    no_of_students=int(input("Enter the number of students"))
   
    for _ in range(no_of_students):
     student={}
     student['name']=input("Enter the students name")
     student['Reg No']=input("Enter the student registration number")
     student['marks']=input("Enter the students marks")
     students.append(student)
     return students
    #Function to sort students based on the marks in ascending order
    def sort_students_by_marks(students):
       return sorted(students,key=lambda student:student['marks'])
    
    #main fuction to cordinate process of capturing and sorting student details

    def main():
       students=Student_details()
       sorted_students=sort_students_by_marks(students)

       print("\mSorted student details by marks(ascending order):")
       for student in sorted_students:
          print(f"Name:{student['name']},Roll Number:{student['roll_number']},Marks:{student['marks']}")

          if __name__ == "__main__":
             main()


