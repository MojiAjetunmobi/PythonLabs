#encryption
def encryption():
    print("You have chosen to encrypt\n")

    #variables
    userInput = input("Please enter text to encrypt: \n")
    key = int(input("Please enter key size: \n"))
    encryption = "" #empty string assigned to encryption variable for message encrypted

    #encryption loop
    #for loop for iterating through the characters of the input message and add the shift value to it
    for character in userInput:
        #check to make sure only characters are encrypted
        if character.isalpha() == True:
            #'a'-'z' is 97-122 and 'A'-'Z' is 65-90 0in ascii.
            #This is will be used for purposes of wrap around

            #to check for upper case characters
            if character == character.lower():
                k = ord(character)- 97 #k represents each upper character and is converted to its acsii equivalent
                k += key #shift value added to k
                k = k % 26 #for the purposes of wrap around depending on key value
                encryption += chr(k + 97) #k added each time to encryption message and change ascii back to character
            else:
                k = ord(character)- 65 #k represents each lower case character and is converted to its acsii equivalent
                k += key #shift value added to k
                k = k % 26 #for the purposes of wrap around depending on key value
                encryption += chr(k + 65) #k added each time to encryption message and change ascii back to character
        else:
            #add the non-alpha characters to encryption variable
            encryption += character

    #output
    print(encryption)

#decryption
def decryption():
    print("You have chosen to decrypt\n")

    #variables
    userInput = input("Please enter the cipher text: \n")
    key = int(input("Please enter key size: \n"))
    decryption = "" #empty string assigned to encryption variable for message encrypted

    #decryption loop
    #for loop for iterating through the characters of the input message and subtract the shift value from it
    for character in userInput:
        #check to make sure only characters are encrypted
        if character.isalpha() == True:
            #'a'-'z' is 97-122 and 'A'-'Z' is 65-90 0in ascii.
            #This is will be used for purposes of wrap around

            #to check for upper case characters
            if character == character.lower():
                k = ord(character)- 97 #k represents each character and is converted to its acsii equivalent
                k -= key #shift value subtracted from k
                k = k % 26 #for the purposes of wrap around depending on key value
                decryption += chr(k + 97) #k added each time to encryption message and change ascii back to character
            else:
                k = ord(character)- 65 #k represents each character and is converted to its acsii equivalent
                k -= key #shift value subtracted from k
                k = k % 26 #for the purposes of wrap around depending on key value
                decryption += chr(k + 65) #k added each time to encryption message and change ascii back to character
        else:
            #add the non-alpha characters to encryption
            decryption += character

    #output
    print(decryption)

#brute force decryption
def bruteforce(k, cipher):
    print("Bruteforce Decryption\n")

    #variables
    bruteforceDecrypt = "" #empty string assigned to decryption variable for message decrypted

    #decryption loop
    #for loop for iterating through the characters of the input message and subtract the shift value from it
    for character in cipher:
        messageCharacter = (ord(character) - k) % 126 #modulus with the ascii value

        #check to make sure only letters are acted on
        if messageCharacter < 32:
            messageCharacter += 95
        bruteforceDecrypt += chr(messageCharacter)

    #print(bruteforceDecrypt) #output
    return bruteforceDecrypt

#main
def main():
    #menu choice
    choice = int(input("1. Encryption\n2. Decryption\n3. Brute Force\nChoose(1, 2, 3): \n"))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    elif choice == 3:
        cipher = input("Enter message to brute force: \n")
        #iterate through the key ranges
        for i in range(1, 95, 1):
            print(bruteforce(i, cipher)) #call on brute force decryption method on the cipher text.
    else:
        print("You made a incorrect selection, goodbye!") #exit code

# call main
if __name__ == "__main__":
    main()
