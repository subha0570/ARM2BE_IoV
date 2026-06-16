# Security/broadcast_encryption.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from CA.vehicle_db import vehicles
from CA.vehicle_db import revoked_vehicles


def broadcast_encrypt(message):

    # Session Key
    session_key = get_random_bytes(16)

    cipher = AES.new(
        session_key,
        AES.MODE_EAX
    )

    ciphertext, tag = cipher.encrypt_and_digest(
        message.encode()
    )

    authorized_keys = {}

    # Only non-revoked vehicles receive K
    for vid in vehicles:

        if vid not in revoked_vehicles:

            authorized_keys[vid] = session_key

    return {
        "ciphertext": ciphertext,
        "nonce": cipher.nonce,
        "tag": tag,
        "authorized_keys": authorized_keys
    }