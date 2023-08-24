from modir.modular import Student
from modir.modular import Manager
from modir.modular import Developer

student = Student('James', 'Shakes', 6000)
student2 = Student('Kofi', 'Bright', 700)

print(student.email)
Student.set_raise_amount(300)
print(student.apply_raise())

manager = Manager('Mr', 'Sampson', 70_000, [student])
manager.add_std(student2)
manager.print_std()

dev = Developer('Miss', 'Joyce', 7_302_002, 'Python')
Developer.set_raise_amount(78788)
print(dev.apply_raise())
