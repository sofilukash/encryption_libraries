from OpenSSL import crypto

def generate_self_signed_cert():
    # Створення приватного ключа
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Створення самопідписаного сертифікату
    cert = crypto.X509()
    cert.get_subject().CN = "localhost"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, "sha256")

    # Виведення сертифікату у консоль
    cert_pem = crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode()
    print("Самопідписаний сертифікат:")
    print(cert_pem)

    # Виведення приватного ключа у консоль
    key_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode()
    print("\nПриватний ключ:")
    print(key_pem)

# Виклик функції для створення сертифікату та виведення його у консоль
generate_self_signed_cert()
