import string

def rail_fence_encrypt(plaintext, rails):
    # Menghilangkan spasi dan mengubah ke huruf kapital
    plaintext = plaintext.replace(" ", "").upper()
    
    # Membuat matriks kosong
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    # Mengisi matriks sesuai pola rail fence
    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        
        if rail == rails - 1:
            direction = -1
        elif rail == 0:
            direction = 1
            
    # Menggabungkan hasil
    ciphertext = ''
    for rail in fence:
        ciphertext += ''.join(rail)
    
    return ciphertext

def rail_fence_decrypt(ciphertext, rails):
    # Menghitung panjang plaintext
    length = len(ciphertext)
    
    # Membuat matriks kosong
    fence = [[''] * length for _ in range(rails)]
    
    # Menandai posisi karakter dengan '*'
    rail = 0
    direction = 1
    for i in range(length):
        fence[rail][i] = '*'
        rail += direction
        
        if rail == rails - 1:
            direction = -1
        elif rail == 0:
            direction = 1
    
    # Mengisi matriks dengan karakter ciphertext
    index = 0
    for i in range(rails):
        for j in range(length):
            if fence[i][j] == '*' and index < length:
                fence[i][j] = ciphertext[index]
                index += 1
    
    # Membaca plaintext dari matriks
    plaintext = ''
    rail = 0
    direction = 1
    for i in range(length):
        plaintext += fence[rail][i]
        rail += direction
        
        if rail == rails - 1:
            direction = -1
        elif rail == 0:
            direction = 1
            
    return plaintext

# Contoh penggunaan
if __name__ == "__main__":
    # Rail Fence Cipher
    plaintext = "RAHASIA"
    rails = 2
    
    print("Rail Fence Cipher:")
    print(f"Plaintext: {plaintext}")
    print(f"Jumlah rel: {rails}")
    
    encrypted = rail_fence_encrypt(plaintext, rails)
    print(f"Ciphertext: {encrypted}")
    
    decrypted = rail_fence_decrypt(encrypted, rails)
    print(f"Decrypted: {decrypted}")