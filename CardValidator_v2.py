#import libraries
from random import Random
import copy
import random

"""
How luhn algorithmn works for credit card validation

0 1 2 3   4 5 6 7   8 9 10 11   12 13 14 15
4 5 3 2   0 0 8 2   8 1  7  1    7  9  1  0

sum of odd placed numbers from right to left
0 + 9 + 1 + 1 + 2 + 0 + 2 + 5 = 20 (for odd placed didits)

sum of even placed numbers from right to left
1    7   7    8    8    0    3   4

double every even placed number (i.e multiply by 2)
1 * 2  7 * 2  7 * 2  8 * 2  8 * 2  0 * 2  3 * 2  4 * 2
1      14      14      16     16      0      6     8

for every double digit that is arrived at, add the two digits
1   1 4   1 4   1 6   1 6   0   6   8
1   1+4   1+4   1+6   1+6   0   6   8
2 +  5  +  5   + 7   + 7  + 0 + 6 + 8 = 40 (for even placed digits)

add sum of odd and even placed digits together
40 + 20 = 60

for luhn check:
    60 % 10 == 0 (valid)
else
    (invalid)
"""

#make a selection
choice = int(input("Select an option: \n 1 - Check Card \n 2 - Generate Card Number \n 3 - Exit \n "))

#method to change numbers from keyboard input which is in string format to integer
def numbers(figure):
    #change figures to integer
    return [int(j) for j in str(figure)]

#method to do a luhm algorithmn check on card number input
def checksum(figures_on_card):
    numbers_on_card = numbers(figures_on_card) #numbers on card assigned to numbers
    odd_number = numbers_on_card[-1::-2] #count odd placements from right
    even_number = numbers_on_card[-2::-2] #count even placements from right
    add_number = sum(odd_number) #add the odd number placements

    #for even number placements
    for number in even_number:
        add_number += sum(numbers(2 * number)) #multiply the numbers and add them
    return add_number % 10 #modulus 10 the added numbers

#method to validate luhn check on card
def valid_card(figures_on_card):
    return checksum(figures_on_card) == 0 #call method to check card number

#check card numbers for checksum and vendor
def cardCheck():
    enter_choice = 'y' #loop guard variable
    #loop to iterate the number of times to input card numbers
    while enter_choice == 'y' or enter_choice == 'Y':
        try: #exception handler
            figures_on_card = input("Please enter the digits on your card: \n") #prompt

            #check to validate card sizes
            if valid_card(figures_on_card) and 12 <= len(figures_on_card) and len(figures_on_card) <= 19:
                print("\nValid card number.")

                #check to validate vendors of cards
                if figures_on_card[0:1] == "4": #visa check
                    print("VISA card")
                elif figures_on_card[0:4] == "6011":
                    print("Discover card")  #discover check
                elif figures_on_card[0:2] == "30":
                    print("Diner's Club - Carte Blanche card") #diners check
                elif figures_on_card[0:2] == "22" or figures_on_card[0:2] == "52":
                    print("Mastercard") #mastercard check
                elif figures_on_card[0:2] == "35":
                    print("JCB card")  #jcb check
                elif figures_on_card[0:2] == "36" or figures_on_card[0:2] == "54" or figures_on_card[0:2] == "55":
                    print("Diner's Club card") #diners club check
                elif figures_on_card[0:2] == "63":
                    print("InstalPayment card") #instalpayment check
                elif figures_on_card[0:2] == "34" or figures_on_card[0:2] == "37":
                    print("American Express (AMEX) card")  #amex check
                elif figures_on_card[0:2] == "06" or figures_on_card[0:2] == "50" or figures_on_card[0:2] == "67":
                    print("Maestro card")  #maestro check
            else:
                print("\nInvalid card entry") #check for wrong entry

            #prompt to check another number
            enter_choice = input("Please, enter (y) or (n) to check another card number: \n")
            #check to exit
            if enter_choice == "n":
                print("Thank you, goodbye!")

        #exception handlers
        except ValueError:
            print("Incorrect card entry, please try again! \n")
        except:
            print("Disallowed entry: \n", sys.exc_info()[0])
            raise

#generate card number
def cardGenerator():
    for x in range(10):
        print (random.randint(1,101))

if choice == 1:
    print("Card check: ")
    cardCheck()

elif choice == 2:
    print("Generate credit card:")
    print("under construction ...")
    cardGenerator()

elif choice == 3:
    print("Thank you, Goodbye!")
