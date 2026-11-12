import requests
import concurrent.futures
import uuid

URL = "http://127.0.0.1:8000/customers"

def fire_request():
    random_email = f"user_{uuid.uuid4()}@stress.com"
    payload = {
        "fullname": "stress tester",
        "email": random_email
    }

    try:
        response = requests.post(URL, json=payload)
        print(f"Sttus: {response.status_code}")
    except Exception as e:
        print(f"network erros: {e}")


def run_attack():
    print("starting stress test")

    with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
        for _ in range(1000):
            executor.submit(fire_request)

    print("stress test finished")


# Standard Python entry point
if __name__ == "__main__":
    run_attack()