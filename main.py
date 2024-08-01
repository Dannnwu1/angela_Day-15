MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "water": 30000,
    "milk": 200,
    "coffee": 100,
}

money = 0


def get_report():
    return (f"Water: {resources["water"]}ml\n"
            f"Milk: {resources["milk"]}ml\n"
            f"Coffee: {resources["coffee"]}ml\n"
            f"Money: ${money}")


QUARTER = 0.25
DIME = 0.10
NIKEL = 0.05
PENNY = 0.01


#TODO 1.print report
# on = True
# while on:
def get_user_choice():
    user_choice = (input("What would you like? (espresso/latte/cappuccino): ")).lower()
    #check user what to do next:
    if user_choice == "espresso":
        return "espresso"
    elif user_choice == "latte":
        return "latte"
    elif user_choice == "cappuccino":
        return "cappuccino"
        #when user input off the machin shutdown
    elif user_choice == "off":
        global on
        on = False
        return on
    elif user_choice == "report":
        print(get_report())
    else:
        print("Invalid input")


#
#     #TODO 2 .Check resources sufficient?
def check_resources_sufficient():
    user_choice_ingredient = MENU[user_choice]["ingredients"]
    for ingredient in user_choice_ingredient:
        if resources[ingredient] >= user_choice_ingredient[ingredient]:
            return True
        else:
            print(f"Sorry there is not enough {ingredient}")


#
#         #TODO 3.Process coins.
#         # if resources_is_sufficient():
def insert_coins():
    print("Please insert coins: ")
    qua_count = int(input("How many quarters?: "))
    dim_count = int(input("How many dimes?: "))
    nick_count = int(input("How many nickles?: "))
    pen_count = int(input("How many pennies?: "))
    return QUARTER * qua_count + DIME * dim_count + NIKEL * nick_count + PENNY * pen_count

    #
    #         #TODO 4.Check transaction successful?


def check_transaction_successful(money_received):
    global money
    if money_received >= MENU[user_choice]["cost"]:
        if money_received != MENU[user_choice]["cost"]:
            change = money_received - MENU[user_choice]["cost"]
            money += MENU[user_choice]["cost"]
            print(f"Received ${money_received}\n"
                  f"Here is the the change ${round(change, 2)}")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")


#TODO 5.Make coffee


def make_coffee(user_selection):
    for ingredient in MENU[user_selection]["ingredients"]:
        resources[ingredient] -= MENU[user_selection]["ingredients"][ingredient]
        resources.update({ingredient: resources[ingredient]})
    print(f"Here is your {user_selection}, enjoy! ")


""" Coffe machine logic """
on = True
while on:
    user_choice = get_user_choice()
    for coffee in MENU:
        if user_choice == coffee:
            if check_resources_sufficient():
                money_get = insert_coins()
                if check_transaction_successful(money_get):
                    make_coffee(user_choice)
