class Person:
    # 属性：性别、性别、年龄、存款
    name: str = None
    age: int = 0
    gender: str = "男"
    __money: float = 0

    def __init__(self, name, age, gender, money):
        self.name = name
        self.age = age
        self.gender = gender
        # 私有属性
        self.__money = money

    # 方法：吃、睡、跑
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print("sleeping")

    @classmethod
    def run(self):
        print("running")


class FunnyMan(Person):
    skill: str = ""

    def __init__(self, skill, name, age, gender, money):
        self.skill = skill
        super().__init__(name, age, gender, money)  # 对父类的属性重新赋值，省去了写self.name=name这些的操作了

    def fun(self):
        print(f"{self.name} is funny,his skill is {self.skill}")


st = FunnyMan("单口相声", "ST", 30, "男", 100000)
print(st.name)
st.fun()

# 通过实例化对象去调用实例化的方法
# p_ls=Person("李四",20,"男",1000)
# print(p_ls.name)
# #p_ls.eat()
# #print(p_ls.__money)
# print(dir(p_ls))
# print(p_ls.age)
# p_ls.name="王五"
# print(p_ls.name)
#
# Person.name="defaultname"


# p_zs=Person()
# print(p_zs.name)
# print(p_zs.run)
#
# print(Person.name)
# Person.run()
