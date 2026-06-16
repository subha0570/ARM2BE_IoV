from Crypto.Hash import SHA256

def create_hash(message):

    hash_obj = SHA256.new(
        message.encode()
    )

    return hash_obj