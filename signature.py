import os

from Crypto.Signature import DSS
from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256


def sign_message(vehicle_id, hash_obj):

    private_file = f"Keys/{vehicle_id}_private.pem"

    if not os.path.exists(private_file):

        print(f"Vehicle {vehicle_id} is not registered.")
        return None

    with open(private_file, "rt") as f:

        private_key = ECC.import_key(
            f.read()
        )

    signer = DSS.new(
        private_key,
        "fips-186-3"
    )

    return signer.sign(hash_obj)


def verify_signature(
        vehicle_id,
        hash_obj,
        signature
):

    public_file = f"Keys/{vehicle_id}_public.pem"

    if not os.path.exists(public_file):

        print(f"Vehicle {vehicle_id} is not registered.")
        return False

    with open(public_file, "rt") as f:

        public_key = ECC.import_key(
            f.read()
        )

    verifier = DSS.new(
        public_key,
        "fips-186-3"
    )

    try:

        verifier.verify(
            hash_obj,
            signature
        )

        return True

    except ValueError:

        return False