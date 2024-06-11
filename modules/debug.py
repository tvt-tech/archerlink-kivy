import subprocess
import atexit

from sys import platform
import socket
import asyncio

import socket

# Define host and port
import time


def open_vlc(rtsp_uri):
    if platform.startswith('win'):
        vlc_process = subprocess.Popen(r'"C:\Program Files\VideoLAN\VLC\vlc.exe" '
                                       r'-vvv "screen://" --screen-fps=60 --sout '
                                       r'"#transcode{vcodec=mp4v,vfilter=croppadd'
                                       r'{croptop=0,cropbottom=0,cropleft=0,cropright=0,'
                                       r'paddtop=0,paddbottom=0,paddleft=0,paddright=0},'
                                       r'width=1280,height=720,acodec=none}:'
                                       r'rtp{sdp='
                                       # r'rtsp://:8554/test'
                                       fr'{rtsp_uri}'
                                       r'}" --no-sout-all --sout-keep')

        def cleanup():
            vlc_process.terminate()
            vlc_process.wait()  # Wait for the process to terminate

        atexit.register(cleanup)


def open_tcp(host, port):
    async def run_tcp_server():
        while True:
            try:
                # Create a TCP/IP socket
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    # Bind the socket to the address and port
                    s.bind((host, port))
                    # Listen for incoming connections
                    s.listen()
                    print(f"Server is listening on {host}:{port}")
                    # Accept incoming connections
                    conn, addr = s.accept()
                    with conn:
                        print(f"Connected by {addr}")
                        while True:
                            # Receive data from the client
                            data = conn.recv(1024)
                            if not data:
                                break
                            await asyncio.sleep(5)
                            # Process received data (here, we'll just print it)
                            print(f"Received: {data.decode()}")
                            if data.decode() == 'CMD_RTSP_TRANS_START':
                                conn.sendall('CMD_ACK_START_RTSP_LIVE'.encode())
                            else:
                                # Echo back the received data
                                conn.sendall(data)
            except ConnectionError:
                pass

    loop = asyncio.get_event_loop()
    loop.create_task(run_tcp_server())