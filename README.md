# ARM2BE for Internet of Vehicles (IoV)

## Overview

This project is a Python-based implementation of the "Anonymous and Revocable Multi-Message Broadcast Encryption (ARM2BE) Scheme" for the Internet of Vehicles (IoV). The implementation was developed as part of my internship work to understand secure vehicular communication, user anonymity, message broadcasting, and vehicle revocation mechanisms.

## Features

* Vehicle Registration using ECC keys
* Secure Message Broadcast Encryption
* Message Decryption by Authorized Vehicles
* Digital Signature Generation and Verification
* Vehicle Revocation Mechanism
* SHA-256 Hashing
* Performance Analysis and Graph Generation

## Project Structure

ARM2BE_IoV
│
├── main.py
├── registration.py
├── encryption.py
├── decryption.py
├── signature.py
├── hashing.py
├── revoke.py
├── performance.py
├── graph.py
├── vehicle_db.py
├── vehicles.json
├── revoked.json
└── README.md


## Requirements

* Python 3.14
* PyCryptodome
* Matplotlib

Install dependencies:

pip install pycryptodome matplotlib

## Run the Project

python3 main.py

## Menu Options

1. Register Vehicle
2. Broadcast Message
3. Decrypt Message
4. Sign Message
5. Verify Signature
6. Revoke Vehicle
7. Generate Performance Graph
8. Exit

## Internship Information

This project was developed during my internship on "Secure Communication in Internet of Vehicles (IoV)",focusing on the implementation and analysis of the ARM2BE cryptographic scheme.

## Author: Subhajit Mahapatra
