from decimal import *

partner_tips = []


# Make floats into static decimals for cash use
def dec(cash_value):
	cash_dec = Decimal(cash_value).quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
	return cash_dec


# Test user response for logic control
def test():
    try:
        test = input('("N" or Enter to continue) > ')
        if test.upper() == 'Y' or test == '':
            return True
        elif test.upper() == 'N':
            return False
        else:
        	print('\nDouble check what you entered'.upper())
    except:
        return False


# Add user input to list of all tips
def employee_tips(hourly_rate):
	global partner_tips
	hours_worked = dec(input('How many hours did they work?\n'))
	pertner_tip_amount = hourly_rate * hours_worked
	partner_tips.appened(partner_tip_amount)


def main():
	global partner_tips
	ready_to_move_on = False
	while not ready_to_move_on:
		try:
			tips = dec(input('Enter in our total tips > $'))
			
			if test():
				print('\nGood our tips are ${}'.format(tips))
				ready_to_move_on = True
		except:
			print('\nDouble check what you entered'.upper())
	ready_to_move_on = False
	while not ready_to_move_on:
		try:
			hours = dec(input('\nEnter total tippable hours > '))
			hourly_rate = tips / hours
			if test():
				ready_to_move_on = True
		except:
			print('\nDouble check what you entered'.upper())
	print('\nOur rate is $%.2f' % hourly_rate)








main()















