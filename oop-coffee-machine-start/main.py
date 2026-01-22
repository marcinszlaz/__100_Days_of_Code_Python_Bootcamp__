# wersja obdżektowa

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()

coffee_over = True
while coffee_over:
    choice = input(f'Please choose a drink {menu.get_items()}: ')
    if choice == 'report':
        coffee.report()
        money.report()
    elif choice == 'off':
        coffee_over = False
        # break
    else:
        if menu.find_drink(choice):
            if coffee.is_resource_sufficient(menu.find_drink(choice)):
                if money.make_payment(menu.find_drink(choice).cost): # find_drink zwraca cały obiekt z Menu self.menu
                    # i należy dobrać się do niego .ką nie indeksami
                    coffee.make_coffee(menu.find_drink(choice))