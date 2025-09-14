class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        return(round(sum(self.marks)/(len(self.marks)),2))
students_data = {"John": [85, 78, 92],"Alice": [88, 79, 95],"Bob": [70, 75, 80]}
students=[Student(name,marks) for name,marks in students_data.items()]
averages={s.name:s.average() for s in students}
top_student = max(students, key=lambda s: s.average()).name
print("Average Marks:", averages)
print("Top Performer:", top_student)