import os
import json
from Crypto.PublicKey import ECC

KEY_DIR = "Keys"
VEHICLE_FILE = "vehicles.json"

os.makedirs(KEY_DIR, exist_ok=True)

if not os.path.exists(VEHICLE_FILE):
    with open(VEHICLE_FILE, "w") as f:
        json.dump({}, f)


def register_vehicle(vehicle_id):

    with open(VEHICLE_FILE, "r") as f:
        vehicles = json.load(f)

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
        f.write(key.export_key(format="PEM"))

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

    with open(VEHICLE_FILE, "w") as f:
        json.dump(vehicles, f, indent=4)

    print(
        f"{vehicle_id} registered successfully"
    )
