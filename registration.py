# CA/registration.py

import os

from Crypto.PublicKey import ECC
from vehicle_db import vehicles

KEY_DIR = "Keys"

os.makedirs(KEY_DIR, exist_ok=True)


def register_vehicle(vehicle_id):

    if vehicle_id in vehicles:

        print("Vehicle already registered")
        return

    key = ECC.generate(curve="P-256")

    private_file = os.path.join(
        KEY_DIR,
        f"{vehicle_id}_private.pem"
    )

    public_file = os.path.join(
        KEY_DIR,
        f"{vehicle_id}_public.pem"
    )

    with open(private_file, "wt") as f:

        f.write(
            key.export_key(format="PEM")
        )

    with open(public_file, "wt") as f:

        f.write(
            key.public_key().export_key(
                format="PEM"
            )
        )

    vehicles[vehicle_id] = {
        "private_file": private_file,
        "public_file": public_file
    }

    print(
        f"{vehicle_id} registered successfully"
    )
