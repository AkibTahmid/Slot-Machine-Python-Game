# Slot Machine Game 🎰

A simple text-based slot machine game implemented in Python. This project allows users to simulate a slot machine experience, deposit money, place bets on multiple lines, and spin to win!

## Features

- Deposit funds to start playing.
- Place bets on 1 to 3 lines.
- Flexible betting amounts (min: ৳1, max: ৳100 per line).
- Randomized slot machine spins with custom symbols and payouts.
- Displays winnings and tracks balance in real-time.

## Symbols and Payouts

| Symbol | Frequency | Value Multiplier |
|--------|-----------|------------------|
| A      | 2         | x5              |
| B      | 4         | x4              |
| C      | 6         | x3              |
| D      | 8         | x2              |

## How to Play

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/slot-machine-game.git

2. Navigate to the project directory:
   ```bash
   cd slot-machine-game

4. Run the game using Python:
   ```bash
   python slot_machine.py

5. Quit the game anytime by pressing q.



Requirements: 
   - Python 3.x
   - No external libraries are required.
   - Code Overview



Main Functions:

   - deposit(): Handle user deposits.
   - get_number_of_lines(): Get the number of lines to bet on.
   - get_bet(): Determine the bet amount per line.
   - spin(balance): Perform the slot machine spin and calculate results.
   - check_winnings(): Check and calculate the winnings based on the spin result.


Utility Functions:

   - get_slot_machine_spin(): Generate the slot machine spin results.
   - print_slot_machine(): Display the slot machine spin results.
   - Example Gameplay


Example Gameplay
```bash
What would you like to deposit? ৳ 100
Enter the number of lines to bet on (1-3): 2
What would you like to bet on each line? ৳ 10
You are betting 10 ৳ on 2 lines. Total bet is: 20 ৳
Slot Machine Results:
A | C | B
B | B | B
C | D | D
You won 40 ৳.
You won on lines: 2
Current Balance: 120 ৳
