def game():
    my_hp = 1000
    my_power = 200
    enemy_hp = 1200
    enemy_power = 199

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        print(my_hp)
        print(enemy_hp)
        if my_hp <= 0:
            print("我输了")
            break
        if enemy_hp <= 0:
            print("我赢了")
            break


game()
