import json
import matplotlib.pyplot as plt

FILE_NAME = "performance.json"

try:
    with open(FILE_NAME, "r") as f:
        data = json.load(f)

    operations = []
    avg_times = []

    for op, values in data.items():
        if len(values) > 0:
            operations.append(op)
            avg_times.append(sum(values) / len(values))

    plt.figure(figsize=(8, 5))
    plt.bar(operations, avg_times)

    plt.title("ARM2BE Performance Analysis")
    plt.xlabel("Operations")
    plt.ylabel("Execution Time (Seconds)")

    plt.tight_layout()

    plt.savefig("performance_graph.png")

    print("Graph saved as performance_graph.png")

    plt.show()

except FileNotFoundError:
    print("performance.json not found")

except Exception as e:
    print("Error:", e)
