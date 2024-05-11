import hashlib

string = b"Pure mathematics is, in its way, the poetry of logical ideas."
sha256 = hashlib.sha256()
sha256.update(string)
string_hash = sha256.hexdigest()

print(f"Hash:{string_hash}")

print(hashlib.algorithms_guaranteed)
