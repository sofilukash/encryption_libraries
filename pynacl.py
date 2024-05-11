import nacl.secret
import nacl.utils

# Це повинно бути суворо секретним, це комбінація до сейфу
key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

# Це сейф, який можна використовувати для шифрування або дешифрування повідомлень
box = nacl.secret.SecretBox(key)

# Це повідомлення для надсилання, воно повинно бути байтовим рядком, оскільки SecretBox буде
#   розглядати його як просто бінарний блок даних.
message = b"It is clear that the chief end of mathematical study must be to make the students think."

# Зашифрувати повідомлення
encrypted = box.encrypt(message)

# Розшифрувати повідомлення
decrypted = box.decrypt(encrypted)

# Вивести оригінальне повідомлення, зашифроване повідомлення та розшифроване повідомлення
print("Оригінальне повідомлення:", message)
print("Зашифроване повідомлення:", encrypted)
print("Розшифроване повідомлення:", decrypted)
