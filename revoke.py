# revoke.py

from vehicle_db import revoked_vehicles

def revoke_vehicle(vehicle_id):

    revoked_vehicles.add(vehicle_id)

    print(f"{vehicle_id} revoked successfully")
