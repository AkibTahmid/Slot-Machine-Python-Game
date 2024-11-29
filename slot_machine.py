import random

# Constants for the slot machine
MAX_LINES = 3 # Maximum number of lines a user can bet on
MAX_BET = 100 # Maximum amount that can be bet per line
MIN_BET = 1 # Minimum amount that can be bet per line

ROWS = 3 # Number of rows in the slot machine
COLS = 3 # Number of columns in the slot machine


# Configuration for symbols and their frequency
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Configuration for symbol values
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# Function to check winnings based on the spin results
def check_winnings(coluums, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = coluums[0][line]
        for column in coluums:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: # Executes if the loop completes without a break
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Function to generate a slot machine spin
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns


# Function to print the slot machine in a readable format
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i !=len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


# Function to get a deposit amount from the user
def deposit():
    while True:
        amount = input("What would you like to deposit? ৳ ")
        if amount.isdigit():
            amount = int (amount)
            if amount > 0:
                break
            else:
                print ("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# Function to get the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number the lines to bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print ("Enter the valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


# Function to get the bet amount per line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ৳ ")
        if amount.isdigit():
            amount = int (amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print (f"Amount must be between {MAX_BET} ৳ - {MAX_BET} ৳.")
        else:
            print("Please enter a number.")

    return amount


# Function to handle the slot machine spin and calculate results
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print (f"You do not have enough to bet that amount, your current balance is: {balance} ৳ ")
        else:
            break

    print (f"You are betting {bet} ৳ on {lines}. Total bet is equal to: {total_bet} ৳ ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings (slots, lines, bet, symbol_value)
    print(f"You won {winnings} ৳.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


# Main function to start the game
def main():
    balance = deposit()
    while True:
        print(f"Current Balance is {balance} ৳ ")
        answer = input ("Press enter to play (q to quit) ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance} ৳")

main()