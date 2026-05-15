import secrets

print(secrets.token_hex())
print(secrets.randbits(200))
print(type(secrets.randbits(200)))