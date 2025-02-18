import hashlib
import base64
import sys

def hashit_iphone_passcode(data):
    hashed_string = hashlib.sha256(data.encode()).hexdigest()
    iphone_password = int(hashed_string, 16) % 1000000
    print(f"number = {iphone_password}")

def hashit_work_passcode(data):
    hashed_string = hashlib.sha256(data.encode()).digest()
    base64_encoded = base64.b64encode(hashed_string).decode()
    print(f"work passcode = {base64_encoded[:12]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <data>")
        sys.exit(1)

    data = sys.argv[1]
    hashit_work_passcode(data)
