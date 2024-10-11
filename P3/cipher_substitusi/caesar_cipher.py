def caesar_encrypt(plaintext, shift):
    result = ""
    for char in plaintext.upper():
        if char.isalpha():
            # Menggeser karakter sesuai kunci
            ascii_val = ord(char) + shift
            if ascii_val > ord('Z'):
                ascii_val -= 26
            result += chr(ascii_val)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    plaintext = "RAHASIA"
    shift = 3
    print("\nCaesar Cipher:")
    print(f"Plaintext: {plaintext}")
    print(f"Shift: {shift}")
    encrypted = caesar_encrypt(plaintext, shift)
    print(f"Encrypted: {encrypted}")
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted: {decrypted}")