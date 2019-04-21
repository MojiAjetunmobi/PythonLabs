"""
Hash chain

Procedure - discovered that the hash chain seed of 654e1c2ac6312d8c6441282f155c8ce9
			given in the assignment was arrived at by changing the case of the user name
			and hashing it with md5 algorithmn.

			Likewise, I changed the case of the username ('ECSC')for the challenge problem
			to lowercase and then hashed it with the md5 algorithmn.

			In the process, I had to pass in unicode utf-8 to allow the md5 to hash the string
			username as bytes

			Finally, I had to call hexidigest to turn the output into the familiar hashing formats,
			in this case md5.

			I used a while loop to iterate through the hash chains until the challenge hash value
			was found.

			To do this, I used a loop guard variable - hashValueFound - and initialized it
			to false. This was later set to true, once the challenge hash value was found.

			The else part of the loop was to continue the hash chain in an iteration and I used a print
			statement to output this iteration on the screen. This would stop once the challenge hash
			is found and loop guard set to true.
"""

#hash chain code
import hashlib #imported python hash library

hashValue = 'c89aa2ffb9edcc6604005196b5f0e0e4' #authenticating hash

userName = 'ECSC'.lower() #username changed to lower case
hash = hashlib.md5() #md5 hashing algorithm
hash.update(userName.encode('utf-8')) #username hashed using md5 algorithm
newHash = hash.hexdigest() #hashed value turned into readable and familiar md5 values

hashValueFound = False #declaration and initialisation of boolean variable for loop

##loop for iterating hashes in a hash chain until hashValue is found
while(hashValueFound == False):
	if(newHash == hashValue):	#If any iteration of a hash is the hash value, then hash value found
		print("Hash value found: " + newHash) ##print found hash value
		hashValueFound = True #set boolean variable to true to exit loop
	#if not
	else:
		newHash = hashlib.md5(newHash.encode('utf-8')).hexdigest() #continue hashing the hashes in a chain
		print(newHash) #print the hashes in the chain as the loop iterates
