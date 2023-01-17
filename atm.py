import os.path

file_exists = os.path.exists('balance.txt')

if file_exists:
    with open('balance.txt', 'w') as balance:
       balance.write("100")


def main_menu():
    selection = input("What would you like to do today? "
                      "Deposit money. [D] "
                      "Withdraw money. [W] "
                      "Inspect balance. [B] "
                      "Quit program. [Q]"
                      )
    if selection == "D" or selection == "d":
        deposit_menu()

    elif selection == "W" or selection == "w":
        withdraw_menu()

    elif selection == "B" or selection == "b":
        balance_menu()

    elif selection == "Q" or selection == "q":
        print("Have a nice day.q")
        quit()

    else:
        print( "\"" + selection + "\" is not a valid option, please select a valid option.")
        main_menu()


def deposit_menu():
    amount = int(input("how much money would you like to add to your balance?"))
    if amount < 0:
        print("the amount you've entered is invalid due to it being either zero or lower please rectify")
        deposit_menu()

    else:
        with open('balance.txt') as balance:
            current_balance = int(balance.read())
            with open('balance.txt', 'w') as balance2:
                balance2.write(str(current_balance + amount))
        with open('balance.txt') as balance:
            print(balance.read())

main_menu()







