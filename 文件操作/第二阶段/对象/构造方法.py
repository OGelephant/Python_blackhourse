class Student:
    name = None
    gender = None
    age = None
    def __init__(self,name,gender,age):
        self.name =name
        self.gender =gender
        self.age=age

    def sayhai (self):
        print(f"姓名是：{self.name}")
stu1 = Student("zhanghao","male","18")

# stu1.name = "zhanghao"
# stu1.gender = "male"
# stu1.age = "18"
print(stu1.age)
print(stu1.gender)
print(stu1.name)

stu1.sayhai()