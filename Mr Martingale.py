# You're in the casino, playing Roulette, going for the "1-18" bets only and desperate to beat the house and so you want to test how effective the Martingale strategy is.

# You will be given a starting cash balance and an array of binary digits to represent a win or a loss as you play: 0 for loss and 1 for win.

# You should create a function martingale to return the balance after playing all rounds.

# You start with a stake of 100 dollars(unit of cash). If you lose a round, you lose the stake placed on that round and double the stake for your next bet. When you win, you win 100% of the stake and revert back to staking 100 dollars on your next bet.

# Example

# martingale(1000, [1, 1, 0, 0, 1]) === 1300
# you win your 1st round: gain $100, balance = 1100
# win 2nd round: gain $100, balance = 1200
# lose 3rd round: lose $100 dollars, balance = 1100
# double stake for 4th round and lost: staked $200, lose $200, balance = 900
# double stake for 5th round and won: staked $400 won $400, balance = 1300

# NOTE: Your balance is allowed to go below 0 (debt) :(

# See Wikipedia articles for more info on:
# Martingale
# Roulette

def martingale(bank, outcomes):
    current_stake = 100
    new_bank = bank
    for outcome in outcomes:
        new_bank -= current_stake #bet
        new_bank += current_stake * outcome * 2   #+0 if lost, +stake if won
        if outcome == 0:
            current_stake *= 2
        else:
            current_stake = 100
    return new_bank

print(martingale(1000, [1, 1, 0, 0, 1]))# === 1300
