Class Student:
def__init__(self,name,program):
    self.name=name
    self.program=program

Class Registration:
    def__init__(self)
        self.students=[]


    def register(self,name,program)
        student=Student(name,program)
        self.students.append(student)


    def sort_by_program(self)
    self.students.sort(key=lambda s: s.program)

    def dispaly(self)
        for student in self.students:
            print(f"name{student.name},program{student.program}")
