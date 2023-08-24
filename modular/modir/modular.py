class Student:
    raise_amount = 104
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Student.num_of_emp += 1

    @property
    def email(self):
        return 'mike{}@gmail.com'.format(self.last)

    # @fullname.setter
    # def fullname(self, name):
    #     first, last = name.split

    def __repr__(self):
        return "Student('{}, {}, {}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def fullname(self):
        fullname = self.last+' '+self.first
        return fullname

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def string_sep(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Student):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language


class Manager(Student):
    def __init__(self, first, last, pay, students=None):
        super().__init__(first, last, pay)
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_std(self, std):
        if std not in self.students:
            self.students.append(self)

    def print_std(self):
        for s in self.students:
            print('-->', s)

