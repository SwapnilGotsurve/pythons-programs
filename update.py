class Student:
    def __init__(self, marks):
        self.marks = marks
    
    def show_marks(self):
        print(f"Marks: {self.marks}")

    def update_marks(self, new_marks):
        self.marks  += new_marks
        print(f"Updated marks: {self.marks}")

s1 = Student(85)
s1.show_marks()
s1.update_marks(10)