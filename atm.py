import os.path

file_exists = os.path.exists('balance.txt')

if file_exists == False:
    with open('balance.txt', 'w') as balance:
        balance.write("100")
    print("your balance has been created")


def main_menu():
    selection = input("What would you like to do today? "
                      "Deposit money. [D] "
                      "Withdraw money. [W] "
                      "Inspect balance. [B] "
                      "Quit program. [Q] "
                      )
    if selection == "D" or selection == "d":
        deposit_menu()

    elif selection == "W" or selection == "w":
        withdraw_menu()

    elif selection == "B" or selection == "b":
        balance_menu()

    elif selection == "Q" or selection == "q":
        print("Have a nice day!")
        quit()

    else:
        print("\"" + selection + "\" is not a valid option, please select a valid option.")
        main_menu()


def deposit_menu():
    d_amount = int(input("how much money would you like to add to your balance? "))
    if d_amount < 0:
        print("The amount you've entered is invalid due to it being either zero or lower. Please rectify")
        deposit_menu()

    else:
        with open('balance.txt') as balance:
            current_balance = int(balance.read())
            with open('balance.txt', 'w') as balance2:
                balance2.write(str(current_balance + d_amount))
        with open('balance.txt') as balance:
            print("Your new balance is now: " + balance.read())
        new_op()


def withdraw_menu():
    with open('balance.txt') as balance:
        current_balance = balance.read()
        w_amount = int(input("How much money would you like to withdraw from your account? "))


        if w_amount == 0 or w_amount > int(current_balance):
            print("The amount you've entered is invalid due to it being either zero or more than your current balance. "
                  "Please rectify.")
            withdraw_menu()
        else:
            with open('balance.txt', 'w') as balance2:
                new_balance = (int(current_balance) - w_amount)
                balance2.write(str(new_balance))
            with open('balance.txt') as balance:
                print("You have successfully withdrawn: " + str(
                    w_amount) + ". And your new total balance is: " + balance.read())
            new_op()


def balance_menu():
    with open('balance.txt') as balance:
        print("your current balance is: " + balance.read())
        new_op()


def new_op():
    answer = input("would you like to continue operations? (Y/N)")
    if answer.lower() == "y" or answer.lower() == "yes":
        main_menu()

    elif answer.lower() == "n" or answer.lower() == "n":
        print("Have a nice day!")
        quit()

    else:
        print("\"" + selection + "\" is not a valid option, please select a valid option.")
        main_menu()



main_menu()
