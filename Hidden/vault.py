key = 35
easy2 = "bQ@K|aVJOGJMD|pWFSP|rVLWFP|bMZ"

easy4 = "uopjoBA"

easy5 = "|BPnWPBJESLS|TFLFQEWZ|ZVDLWJLSW"

mod2a = "fB|FWQoE|VWMWeLQ"

mod2b = "[N`MF|JWaWL|P|OL"

mod4 = "nab|oJAQBQZ"

tiebreaker1 = [(35, 34), (35, 33), (32, 38), (32, 38), (33, 34), (39, 35), (33, 32), (35, 38), (38, 38), (38, 35)]

tiebreaker2 = [111, 74, 65, 81, 66, 81, 90, 3, 98, 106, 3, 102, 79, 66, 74, 77, 70, 3, 113, 74, 64, 75, 3, 104, 70, 85, 74, 77, 3, 104, 77, 74, 68, 75, 87, 15, 3, 112, 75, 74, 85, 66, 80, 75, 66, 77, 72, 66, 81, 3, 97, 3, 109, 66, 74, 81, 25, 3, 98, 81, 87, 74, 69, 74, 64, 74, 66, 79, 3, 106, 77, 87, 70, 79, 79, 74, 68, 70, 77, 64, 70, 15, 3, 119, 66, 87, 66, 3, 110, 64, 100, 81, 66, 84, 3, 107, 74, 79, 79, 3, 16, 81, 71, 3, 70, 71, 74, 87, 74, 76, 77, 3, 17, 19, 18, 16, 13]

def decoder(code):
    return ''.join(chr(ord(char) ^ key) for char in code)

def decrypt(encrypted_path, key = key):
    decrypted_path = []
    for encrypted_x, encrypted_y in encrypted_path:
        x = encrypted_x ^ key
        y = encrypted_y ^ key
        decrypted_path.append((x, y))
    return decrypted_path
