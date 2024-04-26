MAX_LINES = 3
MAX_BET = 100
MIN_BET = 0

def deposit():
    while True:
            amount = input("What would you like to deposit? $")
            if amount.isdigit():
                  amount = int(amount)
                  if amount > 0:
                        break
                  else:
                       print('Amount must be greater than 0.')
            else:
                   print("Enter a number! ")
    return amount

deposit()


def get_no_of_lines():
    while True:
        lines = input("Enter the number of lines to be on (1-" + str(MAX_LINES)+")? ")
        if lines.isdigit():
                lines = int(lines)
                if lines >= 1 and lines <= MAX_LINES:
                    break
                else:
                    print('Enter a valid number of lines!')
        else:
                print("Enter a number! ")
        return lines


def get_bet():
    while True:
            amount = input("What would you like to bet? $")
            if amount.isdigit():
                  amount = int(amount)
                  if MIN_BET <= amount <= MAX_BET:
                        break
                  else:
                       print(f'Amount must be between {MIN_BET} - {MAX_BET} .')
            else:
                   print("Enter a number! ")
    return amount


def main():
      balance = deposit()
      lines = get_no_of_lines()
      bet = get_bet()
      total_bet = bet * lines
      print(f'You are betting {bet} on {lines} lines. Total bet is {total_bet}')

      print(balance, lines)

main()