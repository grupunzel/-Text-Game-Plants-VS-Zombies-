import random

print('Добро пожаловать в игру "Plants VS Zombies"! Здесь Вам придется сражаться с зомби. У вас есть собственный арсенал, содержащий разные виды растений, которые помогут Вам избавиться от зомби. С увеличением Вашего уровня Вам будут открываться новые виды растений. Начнем!')

class Zombie:
    hp = random.randint(50, 100)
    damage = 50

    def display(self):
        print(f'Hp : {self.hp}   Damage : {self.damage}')

class Grohostrel:
    hp = 100
    damage = 25

    def display(self):
        print(f'Hp : {self.hp}   Damage : {self.damage}')

class Povtoritel:
    hp = 100
    damage = 50

    def display(self):
        print(f'Hp : {self.hp}   Damage : {self.damage}')

class Sunflower:
    hp = 50
    heal = 25

    def display(self):
        print(f'Hp : {self.hp}   Heal : {self.heal}')

class Cherry_bomb:
    hp = 0
    damage = 100

    def display(self):
        print(f'Hp : {self.hp}   Damage : {self.damage}')

army = 0
level = 0
groh_count = 0
povt_count = 0
sunflower_count = 0
cherry_count = 0
Army = {
    'Grohostrel' : groh_count,
    'Povtoritel' : povt_count,
    'Sunflower' : sunflower_count,
    'Cherry bomb' : cherry_count
}

def new_plant(level):
    global army
    global groh_count
    global povt_count
    global sunflower_count
    global cherry_count
    global Army
    print('Добавить растение? \n1. Да \n2. Нет')
    choice1 = int(input('Ваш выбор: '))
    if choice1 == 1:
        if level < 5:
            print("Так как у Вас низкий уровень, Вы можете добавить только Грохострел или Подсолнух. \nКого добавить? \n1. Грохострел \n2. Подсолнух")
            choice2 = int(input('Ваш выбор: '))
            if choice2 == 1:
                if groh_count == 0:
                    army += 1
                    groh_count += 1
                    Army['Grohostrel'] += 1
                    global groh1
                    groh1 = Grohostrel
                    print('Данные о Грохостреле: ', groh1.display)
                    print('Ваша армия: ', Army)
                    menu()
                else:
                    print('У Вас уже есть Грохострел. Вы не можете добавить другого.')
                    print('Ваша армия: ', Army)
                    menu()
            elif choice2 == 2:
                if sunflower_count == 0:
                    army += 1
                    sunflower_count += 1
                    global sunflower1
                    sunflower1 = Sunflower
                    print('Данные о Подсолнухе: (Подсолнух хилит только Вишневую Бомбу) ', sunflower1.display)
                    print('Ваша армия: ', Army)
                    menu()
                else:
                    print('У Вас уже есть Подсолнух. Вы не можете добавить другого.')
                    print('Ваша армия: ', Army)
                    menu()
            else:
                print('Ошибка ввода.')
                menu()
        elif level >= 5 and level < 7:
            print(
                f'Ваш уровень: {level}, поэтому Вам доступно новое растение Повторитель. \nДобавить его? \n1. Да \n2. Нет')
            choice2 = int(input('Ваш выбор: '))
            if choice2 == 1:
                if povt_count == 0:
                    army += 1
                    povt_count += 1
                    global povt1
                    povt1 = Povtoritel
                    print('Данные о Повторителе: ', povt1.display)
                    print('Ваша армия: ', Army)
                    menu()
                else:
                    print('У Вас уже есть Повторитель. Вы не можете добавить другого.')
                    print('Ваша армия: ', Army)
                    menu()
            elif choice2 == 2:
                print('Вы не добавили Повторитель.')
                print('Ваша армия: ', Army)
                menu()
            else:
                print('Ошибка ввода.')
                menu()
        else:
            print(
                f'Ваш уровень: {level}, поэтому Вам доступно новое растение Вишневая Бомба. \nДобавить его? \n1. Да \n2. Нет')
            choice2 = int(input('Ваш выбор: '))
            if choice2 == 1:
                if cherry_count == 0:
                    army += 1
                    cherry_count += 1
                    global cherry1
                    cherry1 = Cherry_bomb
                    print('Данные о Вишневой Бомбе: ', cherry1.display)
                    print('Ваша армия: ', Army)
                    menu()
                else:
                    print('У Вас уже есть Вишневая Бомба. Вы не можете добавить другую.')
                    print('Ваша армия: ', Army)
                    menu()
            elif choice2 == 2:
                print('Вы не добавили Вишневую Бомбу.')
                print('Ваша армия: ', Army)
                menu()
            else:
                print('Ошибка ввода.')
                menu()
    elif choice1 == 2:
        print('Вы не добавили растение.')
        print('Ваша армия: ', Army)
        menu()
    else:
        print('Ошибка ввода.')
        menu()

def menu():
    print('\n')
    global level
    global army
    global groh_count
    global povt_count
    global sunflower_count
    global cherry_count
    global Army
    print('Меню: \n1. Посмотреть свою армию \n2. Сразиться с зомби \n3. Посмотреть свой уровень')
    choice = int(input('Ваш выбор: '))
    if choice == 1:
        print('Ваша армия: ', Army)
        print('Хотите добавить растение в свою армию? \n1. Да \n2. Нет')
        choice3 = int(input('Ваш выбор: '))
        if choice3 == 1:
            new_plant(level)
        elif choice3 == 2:
            print('Вы никого не добавили.')
            print('Ваша армия: ', Army)
            menu()
        else:
            print('Ошибка ввода.')
            menu()
    elif choice == 2:
        global zombie
        zombie = Zombie
        print('О, нет! На Вашу армию напал Зомби. Воспользуйтесь своими растениями, чтобы остановить зомби. У Вас есть ровно 4 попытки убить зомби.')
        print('Ваша армия: ', Army)
        if army == 0:
            print('У Вас нет армии, поэтому Вы не можете сражаться!')
        else:
            for i in range(4):
                if zombie.hp > 0:
                    print('Кем хотите воспользоваться? (выбирайте только те растения, которые есть у Вас в армии!) \n1. Грохострел \n2. Повторитель \n3. Подсолнух \n4. Вишневая Бомба')
                    choice4 = int(input('Ваш выбор: '))
                    if choice4 == 1:
                        zombie.hp -= groh1.damage
                        if zombie.hp < 0:
                            zombie.hp = 0
                        print(f'Теперь у Зомби {zombie.hp} hp')
                    elif choice4 == 2:
                        zombie.hp -= povt1.damage
                        if zombie.hp < 0:
                            zombie.hp = 0
                        print(f'Теперь у Зомби {zombie.hp} hp')
                    elif choice4 == 3:
                        cherry1.hp += sunflower1.heal
                        print(f'Теперь у Вишневой Бомбы {cherry1.hp} hp')
                        print(f'А у Зомби {zombie.hp} hp')
                    elif choice4 == 4:
                        print(f'Уровень Вишневой Бомбы: {cherry1.hp}')
                        if cherry1.hp == 75:
                            zombie.hp = 0
                            cherry1.hp = 0
                            print('Вы использовали Вишневую Бомбу! Зомби убит. R.I.P')
                        else:
                            print('Вам не хватает hp для использования Вишневой Бомбы!')
                else:
                    print('Ура! Вы убили Зомби. Продолжим игру.')
                    break
            if zombie.hp > 0:
                print('Увы, Вы проиграли. Но не отчаивайтесь. Продолжим.')
                menu()
            else:
                level += 1
                menu()
    elif choice == 3:
        print(f'Ваш уровень: {level}. Чтобы повысить свой уровень, Вам нужно убивать зомби. За каждого убитого зомби Ваш уровень увеличивается на 1.')
        menu()
    else:
        print('Ошибка ввода!')
        menu()
menu()