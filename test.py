def decrypt_msg(encrypted_msg):
    alphabet = {0: " ", 1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j", 11: "k",
                12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s", 20: "t", 21: "u", 22: "v",
                23: "w", 24: "x", 25: "y", 26: "z"}
    
    alphabet_inv = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
                "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22,
                "w": 23, "x": 24, "y": 25, "z": 26}

    decrypted_msg = ""

    for offset in range(1, 27):
        print("offset", offset)
        msg = ""
        for char in encrypted_msg:
            print("char:", char)
            if char in alphabet_inv:
                # Desencriptamos el caracter utilizando el desfase actual
                position = (alphabet_inv[char] - offset) % 27
                print("position:", position)
                msg += alphabet[position]
            else:
                msg += char
                
            print("msg:", msg)
        # Verificamos si el mensaje desencriptado contiene palabras comunes en inglés
        common_english_words = {"the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at"}
        decrypted_words = msg.split()
        english_words = [word for word in decrypted_words if word.lower() in common_english_words]
        
        if len(english_words) > 0:
            decrypted_msg = msg
            break
        
    return decrypted_msg

encrypted_message = "rvtufkmbrdpr fmasmegppreemvemeuaiv tmgb"
print("Encrypted message:", decrypt_msg(encrypted_message))