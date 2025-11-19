import subprocess
import sys

def main():
    python_exec = sys.executable

    coap_proc = subprocess.Popen([python_exec, "__pycache__/Server_coap.cpython-311.pyc"])
    http_proc = subprocess.Popen(
        [python_exec, "__pycache__/Server_http.cpython-311.pyc"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    try:
        print("Servers running. Press CTRL+C to stop.")
        coap_proc.wait()
    except KeyboardInterrupt:
        print("Stopping servers...")
        coap_proc.terminate()
        http_proc.terminate()

if __name__ == "__main__":
    main()
