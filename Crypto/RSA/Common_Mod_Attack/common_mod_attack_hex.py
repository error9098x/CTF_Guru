import gmpy2
import binascii

def common_modulus_attack(n, e1, e2, c1, c2):
    gcd, s, t = gmpy2.gcdext(e1, e2)
    if gcd != 1:
        raise ValueError("e1 and e2 are not coprime.")

    if s < 0:
        s = -s
        c1 = gmpy2.invert(c1, n)

    if t < 0:
        t = -t
        c2 = gmpy2.invert(c2, n)

    result = (gmpy2.powmod(c1, s, n) * gmpy2.powmod(c2, t, n)) % n
    return int(result)




# Sample input - replace these values with your actual data
n ='0xa96e6f96f6aedd5f9f6a169229f11b6fab589bf6361c5268f8217b7fad96708cfbee7857573ac606d7569b44b02afcfcfdd93c21838af933366de22a6116a2a3dee1c0015457c4935991d97014804d3d3e0d2be03ad42f675f20f41ea2afbb70c0e2a79b49789131c2f28fe8214b4506db353a9a8093dc7779ec847c2bea690e653d388e2faff459e24738cd3659d9ede795e0d1f8821fd5b49224cb47ae66f9ae3c58fa66db5ea9f73d7b741939048a242e91224f98daf0641e8a8ff19b58fb8c49b1a5abb059f44249dfd611515115a144cc7c2ca29357af46a9dc1800ae9330778ff1b7a8e45321147453cf17ef3a2111ad33bfeba2b62a047fa6a7af0eef'
c1 = '0x55cfe232610aa54dffcfb346117f0a38c77a33a2c67addf7a0368c93ec5c3e1baec9d3fe35a123960edc2cbdc238f332507b044d5dee1110f49311efc55a2efd3cf041bfb27130c2266e8dc61e5b99f275665823f584bc6139be4c153cdcf153bf4247fb3f57283a53e8733f982d790a74e99a5b10429012bc865296f0d4f408f65ee02cf41879543460ffc79e84615cc2515ce9ba20fe5992b427e0bbec6681911a9e6c6bbc3ca36c9eb8923ef333fb7e02e82c7bfb65b80710d78372a55432a1442d75cad5b562209bed4f85245f0157a09ce10718bbcef2b294dffb3f00a5a804ed7ba4fb680eea86e366e4f0b0a6d804e61a3b9d57afb92ecb147a769874'
c2 = '0x79834ce329453d3c4af06789e9dd654e43c16a85d8ba0dfa443aefe1ab4912a12a43b44f58f0b617662a459915e0c92a2429868a6b1d7aaaba500254c7eceba0a2df7144863f1889fab44122c9f355b74e3f357d17f0e693f261c0b9cefd07ca3d1b36563a8a8c985e211f9954ce07d4f75db40ce96feb6c91211a9ff9c0a21cad6c5090acf48bfd88042ad3c243850ad3afd6c33dd343c793c0fa2f98b4eabea399409c1966013a884368fc92310ebcb3be81d3702b936e7e883eeb94c2ebb0f9e5e6d3978c1f1f9c5a10e23a9d3252daac87f9bb748c961d3d361cc7dacb9da38ab8f2a1595d7a2eba5dce5abee659ad91a15b553d6e32d8118d1123859208'
e1 = '0x10001'
e2 = '0x23'



# Convert hex to integers
n = int(n, 16)
c1 = int(c1, 16)
c2 = int(c2, 16)
e1 = int(e1, 16)
e2 = int(e2, 16)

# Perform the attack
message = common_modulus_attack(n, e1, e2, c1, c2)

# Convert the message back to bytes
plaintext_bytes = binascii.unhexlify(format(message, 'x'))

# Attempt to print the plaintext message. Strip away potential leading null bytes.
plaintext = plaintext_bytes.lstrip(b'\x00').decode('utf-8', errors='ignore')
print("Decoded plaintext:", plaintext)
