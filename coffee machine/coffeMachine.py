from main import MENU,resources

player = True
while player:
    def printResource():
        global player
        user_input = input('What would you like "espresso" ,"latte","cappuccino"? ')
        if user_input == 'off':
            print('power off')
            player = False
        elif user_input == 'report':
            print(f'Water: {resources['water']}ml')
            print(f'Milk: {resources['milk']}ml')
            print(f'Coffee bean: {resources['coffee']}ml')
        elif user_input == 'espresso':
            moneyInp = float(input(F"This is going to cost {MENU['espresso']['cost']} please slot in your cash: $"))
            if moneyInp == MENU['espresso']['cost']:
                if resources['water'] >= MENU['espresso']['ingredients']['water']:
                    resources['water'] -= 50
                    if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                        resources['coffee'] -= 18
                        print("here is your coffe, have a nice day")
                    else:
                        print('no coffee')
                else:
                    print('no water')
            else:
                print('money incomplete heres your refund')
        elif user_input == 'latte':
            moneyInp = float(input(F"This is going to cost {MENU['latte']['cost']} please slot in your cash: $"))
            if moneyInp == MENU['latte']['cost']:
                if resources['water'] >= MENU['latte']['ingredients']['water']:
                    resources['water'] -= 200
                    if resources['milk'] >= MENU['latte']['ingredients']['milk']:
                        resources['milk'] -= 150
                        if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                            resources['coffee'] -= 24
                            print("here is your coffe, have a nice day")
                        else:
                            print('no coffee')
                    else:
                        print('no milk')
                else:
                    print('no water')

            else:
                print('money incomplete heres your refund')
        elif user_input == 'cappuccino':
            moneyInp = float(input(F"This is going to cost {MENU['cappuccino']['cost']} please slot in your cash: $"))
            if moneyInp == MENU['cappuccino']['cost']:
                if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
                    resources['water'] -= 200
                    if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
                        resources['milk'] -= 100
                        if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                            resources['coffee'] -= 24
                            print("here is your coffe, have a nice day")
                        else:
                            print('no coffee')
                    else:
                        print('no milk')
                else:
                    print('no water')
            else:
                print('money incomplete heres your refund')
                player = False


    printResource()
    