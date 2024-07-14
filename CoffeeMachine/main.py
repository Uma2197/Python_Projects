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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
espresso_cost = MENU["espresso"]["cost"]
latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_cost = MENU["latte"]["cost"]
cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_cost = MENU["cappuccino"]["cost"]


def order():
    user_input = input("What would you like? (espresso/latte/cappuccino):").lower()
    def print_report():
            print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}gms\n")


    def check_resources():
        if user_input == "espresso":
            if resources["water"] <= espresso_water:
                return "Sorry there is not enough water"
            elif resources["coffee"] <= espresso_coffee:
                return "Sorry there is not enough coffee"
            else:
                resources["water"] -= espresso_water
                resources["coffee"] -= espresso_coffee
                return True

        elif user_input == "latte":
            if resources["water"] <= latte_water:
                return "Sorry there is not enough water"
            elif resources["milk"] <= latte_milk:
                return "Sorry there is not enough milk"
            elif resources["coffee"] <= latte_coffee:
                return "Sorry there is not enough coffee"
            else:
                resources["water"] -= latte_water
                resources["milk"] -= latte_milk
                resources["coffee"] -= latte_coffee
                return True


        elif user_input == "cappuccino":
            if resources["water"] <= cappuccino_water:
                return "Sorry there is not enough water"
            if resources["milk"] <= cappuccino_milk:
               return "Sorry there is not enough milk"
            if resources["coffee"] <= cappuccino_coffee:
                return "Sorry there is not enough coffee"
            else:
                resources["water"] -= cappuccino_water
                resources["milk"] -= cappuccino_milk
                resources["coffee"] -= cappuccino_coffee
                return True
        elif user_input == "report":
            return print_report()

    def process_coins():
        quarters = int(input("How many quarters?")) * 0.25
        dimes = int(input("How many dimes?")) * 0.10
        nickles = int(input("How many nickles?")) * 0.05
        pennies = int(input("How many pennies?")) * 0.01
        coins = [quarters, dimes, nickles, pennies]
        amount_entered = sum(coins)
        return amount_entered

    def is_transaction_successful():
        user_amount = process_coins()
        while check_resources():
            if user_input == "espresso" and user_amount == espresso_cost:
                print("Enjoy your drink!")

                return
            elif user_amount > espresso_cost:
                print(f"Enjoy your Drink! Here is your change of ${user_amount - espresso_cost}")

                return
            elif user_input == "latte" and user_amount == latte_cost:
                print("Enjoy your drink!")

                return
            elif user_amount > latte_cost:
                print(f"Enjoy your Drink! Here is your change of ${user_amount - latte_cost}")
                return
            elif user_input == "cappuccino" and user_amount == cappuccino_cost:
                print("Enjoy your drink!")
                return
            elif user_amount > cappuccino_cost:
                print(f"Enjoy your Drink! Here is your change of ${user_amount - cappuccino_cost}")

                return
            else:
                print("Sorry! That's not enough money! Here is your refund")
                return
        print(check_resources())

    check_resources()
    is_transaction_successful()
    order_again = input("Do you want another drink? Type 'Yes' or 'no'").lower()
    if order_again == "yes":
        order()
    else:
        return


order()
