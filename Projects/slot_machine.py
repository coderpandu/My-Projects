# ******* Slot Machine *******
print("****** WELCOME TO THE SLOT MACHINE ******")
print("****** HOPE YOU WIN SOME MONEY 😁 ******")

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]
                        # results = []
                        # for symbol in range(3):
                        #     results.append(random.choice(symbols))
                        # return results

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 0
        elif row[0] == '🔔':
            return bet * 0
        elif row[0] == '⭐':
            print("Hurrey You Just Won!")
            return bet * 100 
    return 0   

def main():
    balance = 100

    print("*************************")
    print("Welcome to Python slots")
    print("symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("**************************")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please Enter a valid Number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds")
            continue

        if bet<= 0:
            print("Bet must be greater than Zero")
            continue
        
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry You Lost This Round 🤣🤣🤣")
        
        balance += payout

        play_again = input("Do you want to spin again? (Y/N):").upper()

        if play_again != 'Y':
            break
    
    print("*********************************************")
    print(f"Game Over! Your Final Balance is ${balance}")
    print("*********************************************")

if __name__ == '__main__':
    main()

