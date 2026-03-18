import json

def read_from_s3():
    print("Reading data from S3 bucket (simulated)...")

    with open("data.json") as f:
        data = json.load(f)

    print("Data received:", data)
    return data


def process_data(data):
    print("Processing data...")

    data["status"] = "processed"
    return data


def save_output(data):
    print("Saving processed output...")

    with open("output.json", "w") as f:
        json.dump(data, f)

    print("Output saved successfully")


if __name__ == "__main__":
    data = read_from_s3()
    processed = process_data(data)
    save_output(processed)