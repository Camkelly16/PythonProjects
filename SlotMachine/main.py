#SlotMachine Project
#The user will deposit some money, allows them to bet lines 1-3 on the slotmachine, 
#If they is right multiply their bet by their money, allow them to keep playing until they cash out,
# Add what they won to Balance 

MAXLINE = 3
def deposit():
    while True: #Continually ask the user enter a vaild amount.
            amount = input("What would you like to deposit? $")
            if amount.isdigit():
                  amount = int(amount)
                  if amount > 0:
                        break
                  else:
                        print("Amount must be greater than 0.")
            else:
                  print("Please enter a number.")

    return amount

def getNumberOfLine():
    while True: 
        lines = input("Enter the number of lines to bet on (1-" + str(MAXLINE) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXLINE:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def main():
    balance = deposit()
    lines = getNumberOfLine()
    print(balance,lines)



main()