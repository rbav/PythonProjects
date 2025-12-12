#Caesar Cipher Project
#Code by Nova_Tago

#The following project has an input message that 

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

print(caesar_cipher(text, 10)) 


