import json
import os

S3_BUCKET = "s3_bucket"  # simulated S3 folder


def upload_to_s3(file_name):
    print("Uploading to S3 (simulated)...")

    os.makedirs(S3_BUCKET, exist_ok=True)
    os.system(f"cp {file_name} {S3_BUCKET}/")

    print(f"{file_name} uploaded to {S3_BUCKET}")


def download_from_s3(file_name):
    print("Downloading from S3 (simulated)...")

    path = f"{S3_BUCKET}/{file_name}"

    if not os.path.exists(path):
        raise Exception("File not found in S3")

    with open(path) as f:
        data = json.load(f)

    print("Data downloaded:", data)
    return data


def process_data(data):
    print("Processing data...")

    data["status"] = "processed"
    return data


def save_output(data):
    print("Saving output...")

    with open("output.json", "w") as f:
        json.dump(data, f)

    print("Output saved successfully")


if __name__ == "__main__":
    # Step 1: Upload input to S3
    upload_to_s3("data.json")

    # Step 2: Download from S3
    data = download_from_s3("data.json")

    # Step 3: Process
    processed = process_data(data)

    # Step 4: Save output
    save_output(processed)
