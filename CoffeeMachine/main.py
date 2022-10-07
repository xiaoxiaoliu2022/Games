MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# def your_option():
#     coffee = input("what would you like?(espresso/latte/cappuccino): ")
#     if coffee == "report":
#         print(resources, current_money)
#         return resources, current_money
#     else:
#         return coffee


def calculate_your_pay():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    pay = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return pay


def check_resources(your_choice):
    if resources["water"] < your_choice["ingredients"]["water"]:
        print("there is not enough water")
        return False
    if resources["milk"] < your_choice["ingredients"]["milk"]:
        print("there is not enough milk")
        return False
    if resources["coffee"] < your_choice["ingredients"]["coffee"]:
        print("there is not enough coffee")
        return False
    else:
        return True


def machine_take_money(your_coins, coffee_cost):
    if your_coins > coffee_cost:
        change = your_coins - coffee_cost
        print(f"your change is {change}")
        return True
    elif your_coins == coffee_cost:
        print("enjoy your coffee")
        return True
    else:
        print(" not enough money, here is your refund")
        return False


def machine_make_coffee(your_choice, your_choice_needs):
    resources["water"] -= your_choice_needs["water"]
    # print(resources["water"])
    resources["milk"] -= your_choice_needs["milk"]
    # print(resources["milk"])
    resources["coffee"] -= your_choice_needs["coffee"]
    print(f"here is your {your_choice}")


use_coffee_machine = True
current_money = 0
while use_coffee_machine:
    your_coffee = input("what would you like?(espresso/latte/cappuccino): ")
    if your_coffee == "report":
        print(resources, current_money)
    else:
        check_result = check_resources(MENU[your_coffee])
        if check_result:
           you_pay = calculate_your_pay()
           charge = MENU[your_coffee]["cost"]
           if machine_take_money(you_pay, charge):
            current_money += charge
            machine_make_coffee(your_coffee, MENU[your_coffee]["ingredients"])

