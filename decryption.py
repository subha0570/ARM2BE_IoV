# Security/broadcast_decryption.py

from Crypto.Cipher import AES


def broadcast_decrypt(
        vehicle_id,
        cipher_data
):

    if vehicle_id not in cipher_data["authorized_keys"]:

        print("Vehicle is revoked or unauthorized")
        return None

    session_key = cipher_data[
        "authorized_keys"
    ][vehicle_id]

    cipher = AES.new(
        session_key,
        AES.MODE_EAX,
        nonce=cipher_data["nonce"]
    )

    plaintext = cipher.decrypt_and_verify(
        cipher_data["ciphertext"],
        cipher_data["tag"]
    )

    return plaintext.decode()