#Caesar Cipher Project
#Code by Nova_Tago

#The following project has an input message that 

#_____________________________Section 1________________________________
# This section introduces the fundamental concept of caesar ciphers 
def caesar_cipher(message, shift):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    result = ""
    
    for char in message:
        if char.lower() in alphabet:
            # Get the numeric value (a=1, b=2, …, z=26)
            num = alphabet.index(char.lower()) + 1
            
            # Apply shift, wrap around using modulo
            shifted_num = (num + shift - 1) % 26 + 1  # keep range 1–26
            
            # Convert back to letter
            shifted_char = alphabet[shifted_num - 1]
            
            # Preserve case (uppercase stays uppercase)
            if char.isupper():
                shifted_char = shifted_char.upper()
            
            result += shifted_char
        else:
            # Keep spaces/punctuation unchanged
            result += char
    
    return result

# Example usage
text = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

#print(caesar_cipher(text, 10)) 
#calls the function to decode the text with known shift of 10

reply = "This is a test of my caesar cipher project. Lets see if it works! (10)"

#print(caesar_cipher(reply, 10))
#Calls the function to encrype the message using a shift of 10



#___________________________Section 2 __________________________________
#Example of brute force decryption

Vishal1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

Vishal2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

#print (caesar_cipher(Vishal1, 10))
#print (caesar_cipher(Vishal2, 14))

Vishal3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx." 

#print (caesar_cipher(Vishal3, 1)+ "   shift = 1")
#print (" ")
#print (caesar_cipher(Vishal3, 2)+ "   shift = 2") 
#print (" ")
#print (caesar_cipher(Vishal3, 3)+ "   shift = 3") 
#print (" ")
#print (caesar_cipher(Vishal3, 4)+ "   shift = 4") 
#print (" ")
#print (caesar_cipher(Vishal3, 5)+ "   shift = 5") 
#print (" ")
#print (caesar_cipher(Vishal3, 6)+ "   shift = 6") 
#print (" ")
#print (caesar_cipher(Vishal3, 7)+ "   shift = 7") 
#print (" ")

#___________________________Section 3_______________________________
#Second section Vigenere Cipher
# A polyalphabetic substitution cipher
# Invented by an Italian Cryptologist named Giovan Battista Bellaso

def vigenere_decode(ciphertext, keyword):
    result = []
    key_index = 0
    keyword = keyword.lower()

    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')

            c = ord(char.lower()) - ord('a')
            k = ord(keyword[key_index % len(keyword)]) - ord('a')

            # NOTE: add the key value to decode this message
            p = (c + k) % 26
            result.append(chr(p + base))

            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


if __name__ == "__main__":
    keyword = "friends"
    message = (
        "txm srom vkda gl lzlgzr qpdb? fepb ejac! "
        "ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
    )

    print(vigenere_decode(message, keyword))
    
#_____________________________Section 4___________________________
def vigenere_encode(plaintext, keyword):
    result = []
    key_index = 0
    keyword = keyword.lower()

    for char in plaintext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')

            p = ord(char.lower()) - ord('a')
            k = ord(keyword[key_index % len(keyword)]) - ord('a')

            # NOTE: subtract key to match the earlier cipher
            c = (p - k) % 26
            result.append(chr(c + base))

            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


if __name__ == "__main__":
    keyword = input("Please enter a keyword: ")
    message = "You can now encode messages using this cipher!"

    encoded_message = vigenere_encode(message, keyword)
    print(encoded_message)
