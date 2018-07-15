class Student(object):
    """docstring for Student."""
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school, *args, **kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        # Gotta initialize the superclass
        super().__init__(name, school)
        self.salary = salary

    # @classmethod
    # def friend(cls, friend_name):
    #     return cls(friend_name, self.school)



anna = WorkingStudent("Anna", "Oxford", 20.0, "Business Analyst")
print(anna.salary)
friend = WorkingStudent.friend(anna, "Greg", 17.5 job_title="Software Developer")
print(friend.name)
print(friend.school)
print(friend.salary)
