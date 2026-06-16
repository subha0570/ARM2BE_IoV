import matplotlib.pyplot as plt
import numpy as np

# Number of messages
nm = 100

# Encryption Cost (ms)
encryption = {
    "Hung": 821011.8,
    "Qu": 100844.7,
    "Tsai": 475828.7,
    "Tseng": 8201.1,
    "Ma": 14826.4,
    "Deng": 3375.3,
    "ARM2BE": 341.476
}

# Decryption Cost (ms)
decryption = {
    "Hung": 46.149,
    "Qu": 3.359,
    "Tsai": 65.446,
    "Tseng": 32.719,
    "Ma": 32.781,
    "Deng": 3.348,
    "ARM2BE": 6.689
}

# Ciphertext Length (bits)
ciphertext = {
    "Hung": 3318400,
    "Qu": 1664000,
    "Tsai": 5254400,
    "Tseng": 67200,
    "Ma": 83200,
    "Deng": 16320,
    "ARM2BE": 32640
}

# ----------------------------
# Encryption Graph
# ----------------------------

plt.figure(figsize=(8,5))
plt.bar(encryption.keys(), encryption.values())
plt.yscale("log")
plt.title("Encryption Cost Comparison")
plt.ylabel("Time (ms)")
plt.xlabel("Schemes")
plt.show()

# ----------------------------
# Decryption Graph
# ----------------------------

plt.figure(figsize=(8,5))
plt.bar(decryption.keys(), decryption.values())
plt.title("Decryption Cost Comparison")
plt.ylabel("Time (ms)")
plt.xlabel("Schemes")
plt.show()

# ----------------------------
# Ciphertext Length Graph
# ----------------------------

plt.figure(figsize=(8,5))
plt.bar(ciphertext.keys(), ciphertext.values())
plt.yscale("log")
plt.title("Ciphertext Length Comparison")
plt.ylabel("Bits")
plt.xlabel("Schemes")
plt.show()