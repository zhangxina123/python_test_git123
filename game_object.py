class Game:
    my_hp = 1000
    # my_power = 200
    enemy_hp = 1200

    # enemy_power = 199

    # 这时候这些属性（我的血量、敌人的血量）也可以通过初始化实例传递过去,(其他参数也可以进行传递，看个人需求)
    def __init__(self, my_hp, enemy_hp):
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp

    def fight(self):
        while True:
            # 调用类的属性需要加上self
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)
            print(self.enemy_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break


class Houyi(Game):
    def __init__(self, defense, my_hp, enemy_hp):
        self.defense = defense
        super().__init__(my_hp, enemy_hp)

    def fight(self):
        while True:
            # 调用类的属性需要加上self
            self.my_hp = self.my_hp + self.defense - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)
            print(self.enemy_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            if self.enemy_hp <= 0:
                print("我赢了")
                break


# 调用fight方法：需要先实例化一个实例game，然后通过实例方法去调用fight方法
# game=Game(1000,1300)
# game.fight()

houyi = Houyi(200, 1000, 1500)
houyi.fight()
