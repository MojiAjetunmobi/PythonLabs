#import libraries
import binascii
from Crypto.PublicKey import RSA

#read in the key value provided
rsa_key = RSA.importKey(open('mykey2.pem', 'r').read())
rsa_key2 = RSA.importKey(open('mykey3.pem', 'r').read())

#output the values n,e,d for the rsa_key value
print(rsa_key.n)
print(rsa_key.e)
print(rsa_key.d)

#output the values n,d for the rsa_key2 values
print(rsa_key2.n)
print(rsa_key2.d)

#covert to string
def convertToString(myInteger):
    return binascii.unhexlify(format(myInteger, "x").encode("utf-8")).decode("utf-8")

#cipher value
ciphertext2 = 474862643754336865489984490773307542016161159436213530034995807183836312346778617047666360854948178434525541089212091928949344492697684657497682106740050084305554758259427768463395264318566101255923490595579348647860471822284428834756812967844672795316325109976652375135659724572710513755433401072885408968307124213606768098411795080747616961236626790699862671834311406129266854138764009952421206625693567227556664511584573464971029270576495696636132292906861410359486612705079004947333371264698887189359265840678094723729950785568382017843975809503403984016678927664449791524785943376314787680072596720311587221852

#decrypt cyphertext and convert to string and output plaintext
decryption = pow(ciphertext2, rsa_key2.d, rsa_key2.n) #decryption
plaintext = convertToString(decryption) #pass decryption into conversion method
print (plaintext) #output decryption
