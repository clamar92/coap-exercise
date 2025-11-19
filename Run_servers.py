import subprocess

def main():
    # Server CoAP: visibile
    subprocess.Popen(["python", "__pycache__/Server_coap.cpython-39.pyc"])

    # Server HTTP: completamente silenziato
    subprocess.Popen(
        ["python", "__pycache__/Server_http.cpython-39.pyc"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

if __name__ == "__main__":
    main()
