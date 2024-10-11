import string

def columnar_transposition_encrypt(plaintext, key):
    # Menghilangkan spasi dan mengubah ke huruf kapital
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    
    # Membuat matriks
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    cols = len(key)
    rows = -(-len(plaintext) // cols)  # Ceiling division
    matrix = [[''] * cols for _ in range(rows)]
    
    # Mengisi matriks
    pos = 0
    for i in range(rows):
        for j in range(cols):
            if pos < len(plaintext):
                matrix[i][j] = plaintext[pos]
                pos += 1
            else:
                matrix[i][j] = 'X'  # Padding
                
    # Membaca kolom sesuai urutan key
    ciphertext = ''
    for i in key_order:
        for j in range(rows):
            ciphertext += matrix[j][i]
            
    return ciphertext

def columnar_transposition_decrypt(ciphertext, key):
    key = key.upper()
    cols = len(key)
    rows = -(-len(ciphertext) // cols)  # Ceiling division
    
    # Membuat matriks
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    matrix = [[''] * cols for _ in range(rows)]
    
    # Mengisi matriks
    pos = 0
    for i in key_order:
        for j in range(rows):
            if pos < len(ciphertext):
                matrix[j][i] = ciphertext[pos]
                pos += 1
                
    # Membaca plaintext dari matriks
    plaintext = ''
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != '':
                plaintext += matrix[i][j]
                
    return plaintext

# Contoh penggunaan
if __name__ == "__main__":
    # Columnar Transposition Cipher
    plaintext = "RAHASIA"
    rails = 2

    print("\nColumnar Transposition Cipher:")
    key = "KUNCI"
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    encrypted = columnar_transposition_encrypt(plaintext, key)
    print(f"Ciphertext: {encrypted}")
    
    decrypted = columnar_transposition_decrypt(encrypted, key)
    print(f"Decrypted: {decrypted}")