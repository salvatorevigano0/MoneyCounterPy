# MoneyCounterPy

This python program allows for a single user to insert and remove coins and banknotes, keep track of the total amount of money, and view the total balance.

## Table of Contents

1. [Functionality](#functionality)
2. [Structure](#structure)
3. [Data Storage](#data-storage)
4. [Instructions](#instructions)
5. [Example](#example)

## Functionality

The program offers the following functionalities:

- Insert coins: Allows users to insert coins into the system.
- Remove coins: Allows users to remove coins from the system.
- Insert banknotes: Allows users to insert banknotes into the system.
- Remove banknotes: Allows users to remove banknotes from the system.
- See total number of banknotes and coins inserted: Displays the total number of banknotes and coins currently in the system.
- See total balance: Displays the total balance of the banknotes and coins currently in the system.

## Structure

The program is structured as follows:

- `main`: This is the main function that contains the program loop.
- `check_input`: This function checks if the input is valid.
- `count_coins`: This function adds the coins inserted to the JSON file.
- `remove_coins`: This function removes the coins from the JSON file.
- `count_banknotes`: This function adds the banknotes inserted to the JSON file.
- `remove_banknotes`: This function removes the banknotes from the JSON file.
- `print_total_banknotes_coins`: This function prints the total number of banknotes and coins inserted in the JSON file.
- `print_total_balance`: This function prints the total balance of the banknotes and coins inserted in the JSON file.

## Data Storage

The data is stored in a JSON file named `moneycounter.json`. The JSON file is used to store the data persistently so that the data is not lost when the program is closed.

## Instructions

To use the program, follow these instructions:

1. Choose an option from the menu (1 to 6):
   - 1: Insert coins
   - 2: Remove coins
   - 3: Insert banknotes
   - 4: Remove banknotes
   - 5: See total number of banknotes and coins inserted
   - 6: See total balance
   - 7: Exit
2. Depending on the option chosen, follow the prompts to input the coin or banknote type and quantity.
3. To exit the program, choose option 7.

## Example

Here's an example of how to use the program:

1. Choose option 1 to insert coins.
2. Enter the coin type (e.g., 2 for €2 coin).
3. Enter the quantity of coins.
4. Choose option 5 to see the total number of coins inserted.
5. Choose option 6 to see the total balance.
6. Choose option 7 to exit the program.