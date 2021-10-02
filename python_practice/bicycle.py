class Bicycle:
    def run(self, km):
        print(f"普通自行车骑行里程数为：{km}km")


class EBicycle(Bicycle):
    def __init__(self, battery_level):
        # 初始化电量
        self.battery_lever = battery_level

    def fill_charge(self, vol):
        # 总电量
        self.battery_lever = self.battery_lever + vol

    def run(self, km):
        # 用电，脚蹬两种方式
        miles = km - self.battery_lever * 10
        if miles > 0:
            print(f"已经使用电行驶：{self.battery_lever * 10}")
            super().run(miles)
        else:
            print(f"已经使用电行驶：{km}km")


if __name__ == '__main__':  # 入口函数，规范一点
    eb = EBicycle(10)
    eb.run(99)
