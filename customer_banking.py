# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account


# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_setup_complete = False
    while not savings_setup_complete:
        savings_balance = input("Please enter your initial savings balance.\n")

        if not savings_balance.replace(".", "", 1).isdigit():
            print("This is not a valid number. Please try again.")
        else:
            savings_balance = float(savings_balance)

            while True:
                savings_interest = input(
                    "Please enter your annual interest rate for the savings account.\n"
                )
                # Removes % if input by user
                savings_interest = savings_interest.replace("%", "", 1)
                if not savings_interest.replace(".", "", 1).isdigit():
                    print("This is not a valid number. Please try again.")
                else:
                    savings_interest = float(savings_interest)
                    break
            while True:
                savings_maturity = input(
                    "Please enter the length of months to determine amount of interest. Enter in whole numbers only.\n"
                )
                if not savings_maturity.isdigit():
                    print("This is not a valid number. Please try again.")
                else:
                    savings_maturity = int(savings_maturity)
                    savings_setup_complete = True
                    break

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity
    )

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(
        f"Your interest earned is ${interest_earned:,.2f} and your updated savings account balance with interest earned for {savings_maturity} months is ${updated_savings_balance:,.2f}"
    )

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    cd_setup_complete = False
    while not cd_setup_complete:
        cd_balance = input("Please enter your initial CD account balance.\n")

        if not cd_balance.replace(".", "", 1).isdigit():
            print("This is not a valid number. Please try again.")
        else:
            cd_balance = float(cd_balance)

            while True:
                cd_interest = input(
                    "Please enter your annual interest rate for the CD account.\n"
                )

                # Removes % if input by user
                cd_interest = cd_interest.replace("%", "", 1)

                if not cd_interest.replace(".", "", 1).isdigit():
                    print("This is not a valid number. Please try again.")
                else:
                    cd_interest = float(cd_interest)
                    break

            while True:
                cd_maturity = input(
                    "Please enter the length of months for the CD. Enter in whole numbers only.\n"
                )
                if not cd_maturity.isdigit():
                    print("This is not a valid number. Please try again.")
                else:
                    cd_maturity = int(cd_maturity)
                    cd_setup_complete = True
                    break

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity
    )

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(
        f"Your interest earned is ${interest_earned:,.2f} and your updated CD account balance with interest earned for {cd_maturity} months is ${updated_cd_balance:,.2f}."
    )
    print(f"\nHave a nice day.")


if __name__ == "__main__":
    # Call the main function.
    main()
