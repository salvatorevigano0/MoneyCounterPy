import json, os

# Define dictionaries for coins and banknotes
coins = {
    '1c': 0.01,
    '2c': 0.02,
    '5c': 0.05,
    '10c': 0.10,
    '20c': 0.20,
    '50c': 0.50,
    '1': 1,
    '2': 2,
}

banknotes = {
    '5': 5,
    '10': 10,
    '20': 20,
    '50': 50,
    '100': 100,
    '200': 200,
    '500': 500,
}

JSON_FILENAME = 'moneycounter.json'

# If the JSON file does not exist, initialize it
if not os.path.exists(JSON_FILENAME):
    with open(JSON_FILENAME, 'w') as f:
        json.dump({}, f)

def check_input(money_type, money_quantity):
    """
    Check if the coin/banknote type is valid and if the quantity is a non-negative integer.
    """
    if money_type not in coins.keys() and money_type not in banknotes.keys():
        print(f"Error: Invalid coin or banknote type. Try again.")
        return False

    try:
        money_quantity = int(money_quantity)
    except ValueError:
        print(f"Error: The quantity must be an integer. Try again.")
        return False
    
    if money_quantity < 0:
        print(f"Error: The quantity must be a non-negative integer. Try again.")
        return False

    return True

def count_coins(coins_to_insert):
    """
    Add the coins inserted to the JSON file.
    """
    with open(JSON_FILENAME, 'r+') as f:
        data = json.load(f)
        for coin in coins_to_insert:
            if coin in coins:
                if coin not in data:
                    data[coin] = 0
                data[coin] += coins_to_insert[coin]
    with open(JSON_FILENAME, 'w') as f:
        json.dump(data, f)

def remove_coins(coins_to_remove):
    """
    Remove the coins from the JSON file.
    """
    with open(JSON_FILENAME, 'r+') as f:
        data = json.load(f)
        for coin in coins_to_remove:
            if coin in coins:
                if coin in data:
                    data[coin] -= coins_to_remove[coin]
                    if data[coin] < 0:
                        data[coin] = 0
    with open(JSON_FILENAME, 'w') as f:
        json.dump(data, f)

def count_banknotes(banknotes_to_insert):
    """
    Add the banknotes inserted to the JSON file.
    """
    with open(JSON_FILENAME, 'r+') as f:
        data = json.load(f)
        for banknote in banknotes_to_insert:
            if banknote in banknotes:
                if banknote not in data:
                    data[banknote] = 0
                data[banknote] += banknotes_to_insert[banknote]
    with open(JSON_FILENAME, 'w') as f:
        json.dump(data, f)

def remove_banknotes(banknotes_to_remove):
    """
    Remove the banknotes from the JSON file.
    """
    with open(JSON_FILENAME, 'r+') as f:
        data = json.load(f)
        for banknote in banknotes_to_remove:
            if banknote in banknotes:
                if banknote in data:
                    data[banknote] -= banknotes_to_remove[banknote]
                    if data[banknote] < 0:
                        data[banknote] = 0
    with open(JSON_FILENAME, 'w') as f:
        json.dump(data, f)

def print_total_banknotes_coins():
    """
    Print the total number of banknotes and coins inserted in the JSON file.
    """
    with open(JSON_FILENAME, 'r') as f:
        data = json.load(f)
        num_banknotes = sum(data.get(b, 0) for b in banknotes)
        num_coins = sum(data.get(c, 0) for c in coins)
        print(f"Total number of banknotes: {num_banknotes}")
        print(f"Total number of coins: {num_coins}")

def print_total_balance():
    """
    Print the total balance of the banknotes and coins inserted in the JSON file.
    """
    with open(JSON_FILENAME, 'r') as f:
        data = json.load(f)
        total_balance = sum(data.get(b, 0) * banknotes[b] for b in banknotes) + sum(data.get(c, 0) * coins[c] for c in coins)
        print(f"Total balance: {total_balance:.2f}")

# Input of the total amount of money
total_money = 0
coins_to_insert = {}
coins_to_remove = {}
banknotes_to_insert = {}
banknotes_to_remove = {}

while True:
    print("1. Insert coins")
    print("2. Remove coins")
    print("3. Insert banknotes")
    print("4. Remove banknotes")
    print("5. See total number of banknotes and coins inserted")
    print("6. See total balance")
    print("7. Exit")
    choice = input("Choice: ")
    
    if choice == "7":
        break
    
    if choice == "1":
        coins_to_insert = {}
        coin = input("Enter the type of coin (empty to finish): ")
        while coin:
            quantity = input("Enter the quantity: ")
            if check_input(coin, quantity):
                coins_to_insert[coin] = int(quantity)
            coin = input("Enter the type of coin (empty to finish): ")
        count_coins(coins_to_insert)
    
    if choice == "2":
        coins_to_remove = {}
        coin = input("Enter the type of coin to remove (empty to finish): ")
        while coin:
            quantity = input("Enter the quantity to remove: ")
            if check_input(coin, quantity):
                coins_to_remove[coin] = int(quantity)
            coin = input("Enter the type of coin to remove (empty to finish): ")
        remove_coins(coins_to_remove)
    
    if choice == "3":
        banknotes_to_insert = {}
        banknote = input("Enter the type of banknote (empty to finish): ")
        while banknote:
            quantity = input("Enter the quantity: ")
            if check_input(banknote, quantity):
                banknotes_to_insert[banknote] = int(quantity)
            banknote = input("Enter the type of banknote (empty to finish): ")
        count_banknotes(banknotes_to_insert)
    
    if choice == "4":
        banknotes_to_remove = {}
        banknote = input("Enter the type of banknote to remove (empty to finish): ")
        while banknote:
            quantity = input("Enter the quantity to remove: ")
            if check_input(banknote, quantity):
                banknotes_to_remove[banknote] = int(quantity)
            banknote = input("Enter the type of banknote to remove (empty to finish): ")
        remove_banknotes(banknotes_to_remove)
    
    if choice == "5":
        print_total_banknotes_coins()
        
    if choice == "6":
        print_total_balance()