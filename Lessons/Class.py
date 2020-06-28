class Student:
    weight = 0
    height = 0
    name = ""
    relative = None

    def change_name(self, newname):
        self.name = newname

    def swap_students(s1, s2):
        s1.name, s2.name = s2.name, s1.name
        s1.weight, s2.weight = s2.weight, s1.weight
        s1.height, s2.height = s2.height, s1.height

    def show(self):
        print(self.name, self.weight, self.height)

    def __init__(self, w, h, name):
        self.weight = w
        self.height = h
        self.name = name


w1 = 60  # int(input("Введите вес:"))
h1 = 180  # int(input("Введите рост:"))
name1 = "Misha"  # input("Введите имя:")

m = Student(w1, h1, name1)
t = Student(71, 150, "Tima")
x = Student(100, 200, "Akakii")

Student.swap_students(m, t)


dic = {m.name: m, t.name: t, x.name: x}
n = input("Enter name:")
# dic[n].show()

m.relative, t.relative = t, m
dic[n].show()
if dic[n].relative is not None:
    dic[n].relative.show()
else:
    print("All dead")

