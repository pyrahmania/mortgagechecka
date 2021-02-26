print(
    "Hello and welcome to Mortgage CheckA.\nJust going to ask you a few simple questions..."
)
bankrupt = input(
    "Have you been declaired bankrupt in the past 6 years? Y/N: ").lower()

# .lower() makes whatever the input is a lower case.

str(bankrupt)

if bankrupt == "y":
    print("Sorry, not today.")

elif bankrupt == "n":
    default = input(
        "Great! Have you defaulted on any accounts or loans in the past 6 years? Y/N: "
    ).lower()

    if default == "y":
        print("Sorry, not today.")

    elif default == "n":
        credit = input(
            "Amazing! Any reason to suspect you might have bad credit? Y/N: "
        ).lower()

if credit == "y":
    print("Sorry, not today.")

    # struggling with the sum abit need to think this through better

elif credit == "n":
    income = float(
        input("So far so good. Almost there. What is your monthly income?: "))
    outgoings = float(
        input(
            "...and what are your monthly outgoings, not including mortgage?: "
        ))
    if (income / 2) < outgoings:
        print(
            f"Sorry, your outgoings of £{int(outgoings)} are more than 50% of your montly income of £{int(income)}.  As such, we are not able to autoapprove this application."
        )
    else:
        print(
            "Congratulations, you are pre approved for one of our fantastic deals!"
        )

# here madge I can see you in here. This is great.

# next - do the sums of income and outgoings.
# Then, some how if outgoings are more than half, no. Less than, amazing you have pre qualified.
