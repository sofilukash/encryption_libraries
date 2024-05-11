import hmac

key = b'secret_key'
message = b'Mathematics is the most beautiful and most powerful creation of the human spirit.'
h = hmac.new(key, message, 'sha256')

digest = h.digest()
print(f"Hash: {digest}")

hex_digest = h.hexdigest()
print(f"Hash: {hex_digest}")
