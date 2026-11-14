# SILK BANK ATM - Full Solution

# Part 1: The Safe
stored_PIN = 1122
starting_balance = 10000
max_tries = 3

# Part 2: Withdrawal Helper Function (Function with return)
def withdraw_amount(balance):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance and amount % 500 == 0:
        return balance - amount  # success -> new balance
    else:
        return 0  # fail signal

# Part 3: Main Flow (Function calling function + While Loop + Break)
def silk_bank_atm():
    retries = 0
    current_balance = starting_balance

    while retries < max_tries:
        pin = int(input("Please Enter your PIN: "))

        if pin == stored_PIN:
            print("PIN correct, welcome!")
            new_balance = withdraw_amount(current_balance)

            if new_balance != 0:  # transaction success
                print("Your transaction has been successful, please collect your card and cash")
                current_balance = new_balance
                print(f"Your current balance is {current_balance}")
            else:  # transaction fail
                print("Invalid amount. Must be <= balance and multiple of PKR 500")
            print(f"Your current balance is {current_balance}")
            break  # exit ATM loop after transaction attempt

        else:  # wrong pin
            retries += 1
            if retries == max_tries:
                print("Your Card is being captured due to continuous incorrect pin")
                break
            else:
                print(f"Wrong PIN, tries left: {max_tries - retries}")

# Part 4: Run the ATM
silk_bank_atm()