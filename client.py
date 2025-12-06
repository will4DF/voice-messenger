import socket
import pyaudio


HOST = "127.0.0.1"
PORT = 5050


def record_audio(seconds=3):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print(f"* Recording {seconds}s...")
    frames = []

    for _ in range(int(RATE / CHUNK * seconds)):
        frames.append(stream.read(CHUNK, exception_on_overflow=False))

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Return raw PCM bytes
    return b"".join(frames)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("[CLIENT] Connected to server.\n")

    while True:
        print("1) Send Text")
        print("2) Record & Send Voice")
        print("3) Quit")
        choice = input("> ")

        if choice == "1":
            msg = input("Message: ")
            s.send(b"TXT ")
            s.send(msg.encode())

        elif choice == "2":
            secs = input("Seconds (default 3): ")
            secs = int(secs) if secs else 3

            raw_audio = record_audio(secs)

            # Send audio header
            s.send(b"AUD ")
            s.send(str(len(raw_audio)).ljust(16).encode())
            s.send(raw_audio)

            # Server returns filename
            filename = s.recv(1024).decode()
            print(f"[SERVER SAVED VOICE AS] {filename}")

        elif choice == "3":
            break

    s.close()


if __name__ == "__main__":
    main()
