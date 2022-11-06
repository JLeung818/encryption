x = input("encryption type: ")
y = input("input text")
if x in "Caesar Cipher":
    C = y
    plainText = ""
    C = C.replace("Caesar Cipher(+3):", "")
    C = C.replace(" ", "/")
    C = C.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    plainText = ""
    for char in C:
        if char == "/":
            plainText = plainText + " "
        else:
            index = alphabet.find(char) - 3
            plainText = plainText + alphabet[index]
    break
elif x in "Morse Code":
    M = y
    M = M.replace("Morse Code:", "")
    morse = {
    '....' : 'h', '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd', '.' : 'e', '..-.' : 'f', '--.' : 'g', '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p', '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.-.-.-' : '.', '..--..' : '?', '--..--' : ',', '/' : ' ', '.----' : '1', '..---' : '2', '...--' : '3', '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7', '---..' : '8', '----.' : '9', '-----' : '0'
    }
    words = []
    letters = []
    j = -1
    for i in M.split(" "):
        j = j + 1
        letters = letters + [i.split("/")]
        for k in range(len(letters[j])):
            words = str(words) + morse.get(letters[j][k], " ")
        words = words + ""
    plainText = "".join(words)
    plainText = plainText.replace("[]", "")
    break
elif x in "Hex":
    H = y
    H = H.replace("Hex:", "")
    Hex = ""
    for i in range(len(H)):
        plaintextChar = H
        tbytes = bytes.fromhex(plaintextChar)
        plainText = tbytes.decode("ASCII")
        i = i + 1
    break
