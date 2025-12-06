import socket
import threading
import os
import time

HOST = "0.0.0.0"
PORT = 5050

AUDIO_DIR = "audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def handle_client(conn, addr):
    print(f"[CLIENT CONNECTED] {addr}")

    while True:
        header = conn.recv(4)
        if not header:
            break

        command = header.decode().strip()

        if command == "TXT":
            msg = conn.recv(1024).decode()
            print(f"[TEXT MESSAGE] {addr}: {msg}")


        elif command == "AUD":

            filename = f"{int(time.time() * 1000)}.wav"

            filepath = os.path.join(AUDIO_DIR, filename)

            filesize = int(conn.recv(16).decode().strip())

            frames = conn.recv(filesize)

            import wave

            wf = wave.open(filepath, "wb")

            wf.setnchannels(1)

            wf.setsampwidth(2)  # 16-bit audio

            wf.setframerate(44100)

            wf.writeframes(frames)

            wf.close()

            print(f"[AUDIO SAVED] {filepath}")

            conn.send(filename.encode())

    conn.close()
    print(f"[CLIENT DISCONNECTED] {addr}")


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((HOST, PORT))
    s.listen()

    print(f"[SERVER READY] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == "__main__":
    main()
