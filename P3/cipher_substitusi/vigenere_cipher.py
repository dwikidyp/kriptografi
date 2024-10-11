def vigenere_encrypt(plaintext, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) - ord('A') for i in key]
    plaintext = plaintext.upper()
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            # Mengambil shift dari kunci sesuai posisi
            shift = key_as_int[i % key_length]
            # Menggeser karakter
            ascii_val = (ord(plaintext[i]) - ord('A') + shift) % 26
            result += chr(ascii_val + ord('A'))
        else:
            result += plaintext[i]
    return result

def vigenere_decrypt(ciphertext, key):
    result = ""
    key = key.upper()
    key_length = len(key)
    key_as_int = [ord(i) - ord('A') for i in key]
    ciphertext = ciphertext.upper()
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Mengambil shift dari kunci sesuai posisi
            shift = key_as_int[i % key_length]
            # Mengembalikan karakter
            ascii_val = (ord(ciphertext[i]) - ord('A') - shift) % 26
            result += chr(ascii_val + ord('A'))
        else:
            result += ciphertext[i]
    return result

# Contoh penggunaan
if __name__ == "__main__":
    
    # Test Vigenere Cipher
    plaintext = "RAHASIA"
    key = "KUNCI"
    print("\nVigenere Cipher:")
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    encrypted = vigenere_encrypt(plaintext, key)
    print(f"Encrypted: {encrypted}")
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")