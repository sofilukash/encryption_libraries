from cryptography.fernet import Fernet

# Генерування ключа
key = Fernet.generate_key()

# Створення об'єкту шифрування
cipher = Fernet(key)

# Шифрування повідомлення
message = cipher.encrypt(b"What is mathematics? It is only a systematic effort of solving puzzles posed by nature.")

print("Encryption:", message)

# Розшифрування повідомлення
plain_text = cipher.decrypt(message)
print("Deciphering:", plain_text.decode())
