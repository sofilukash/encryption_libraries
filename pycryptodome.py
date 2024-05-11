from Crypto.Cipher import AES
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

# Дані для шифрування
data = 'Nature is written in mathematical language.'.encode()
# Генерація випадкових ключів
aes_key = get_random_bytes(16)
hmac_key = get_random_bytes(16)

# Шифрування за допомогою AES в режимі CTR
cipher = AES.new(aes_key, AES.MODE_CTR)
ciphertext = cipher.encrypt(data)

# Обчислення HMAC-SHA256
hmac = HMAC.new(hmac_key, digestmod=SHA256)
tag = hmac.update(cipher.nonce + ciphertext).digest()

# Виведення результатів у консоль
print("Cipher Text:", ciphertext)
print("HMAC Tag:", tag)
