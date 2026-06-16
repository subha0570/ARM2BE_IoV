# main.py

import time
import subprocess

from registration import register_vehicle

from encryption import (
    broadcast_encrypt
)

from decryption import (
    broadcast_decrypt
)

from hashing import (
    create_hash
)

from signature import (
    sign_message,
    verify_signature
)

from revoke import (
    revoke_vehicle
)

from performance import (
    save_time
)


cipher_data = None
signature = None
hash_obj = None


while True:

    print("\n===== ARM2BE Project =====")

    print("1. Register Vehicle")
    print("2. Broadcast Message")
    print("3. Decrypt Message")
    print("4. Sign Message")
    print("5. Verify Signature")
    print("6. Revoke Vehicle")
    print("7. Generate Graph")
    print("8. Exit")

    choice = input("Choice: ")


    if choice == "1":

        vid = input(
            "Vehicle ID: "
        )

        start = time.perf_counter()

        register_vehicle(
            vid
        )

        end = time.perf_counter()

        save_time(
            "Register",
            end - start
        )


    elif choice == "2":

        message = input(
            "Message: "
        )

        start = time.perf_counter()

        cipher_data = (
            broadcast_encrypt(
                message
            )
        )

        end = time.perf_counter()

        save_time(
            "Encrypt",
            end - start
        )

        print(
            "Broadcast Message Sent Successfully"
        )

    elif choice == "3":

        if cipher_data is None:

            print(
                "No Broadcast Message Available"
            )

        else:

            vid = input(
                "Vehicle ID: "
            )

            start = time.perf_counter()

            plaintext = (
                broadcast_decrypt(
                    vid,
                    cipher_data
                )
            )

            end = time.perf_counter()

            save_time(
                "Decrypt",
                end - start
            )

            if plaintext:

                print(
                    "\nDecrypted Message:"
                )

                print(
                    plaintext
                )

    elif choice == "4":

        vid = input(
            "Vehicle ID: "
        )

        msg = input(
            "Message: "
        )

        hash_obj = create_hash(
            msg
        )

        start = time.perf_counter()

        signature = sign_message(
            vid,
            hash_obj
        )

        end = time.perf_counter()

        save_time(
            "Sign",
            end - start
        )

        if signature:

            print(
                "Message Signed Successfully"
            )

        else:

            print(
                "Signing Failed"
            )

    elif choice == "5":

        vid = input(
            "Vehicle ID: "
        )

        if hash_obj is None:

            print(
                "No Message Hash Found"
            )

        elif signature is None:

            print(
                "No Signature Found"
            )

        else:

            start = time.perf_counter()

            result = verify_signature(
                vid,
                hash_obj,
                signature
            )

            end = time.perf_counter()

            save_time(
                "Verify",
                end - start
            )

            if result:

                print(
                    "Valid Signature"
                )

            else:

                print(
                    "Invalid Signature"
                )

    elif choice == "6":

        vid = input(
            "Vehicle ID: "
        )

        start = time.perf_counter()

        revoke_vehicle(
            vid
        )

        end = time.perf_counter()

        save_time(
            "Revoke",
            end - start
        )


    elif choice == "7":

        try:

            subprocess.run(
                [
                    "python3",
                    "graph.py"
                ]
            )

        except Exception as e:

            print(
                "Graph Error:",
                e
            )



    elif choice == "8":

        print(
            "Exiting ARM2BE System..."
        )

        break

    else:

        print(
            "Invalid Choice"
        )
