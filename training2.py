class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name):
        return cls(friend_name, origin.school)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent("anna", "Oxford", 1500)
friend = WorkingStudent.friend(anna, "Greg")
print(friend.school)