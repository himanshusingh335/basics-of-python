
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


string = "LKMLJUPICNXL"
keyword = "SWINFSWINFSW"
print("Decrypted Text :", originalText(string, keyword))
