#

import picamera
import socket
import subprocess

camera = picamera.PiCamera()

def record_h264(filename, time_s=60, res=[640, 480])
	assert len(res) == 2, "Resolution must have 2 dimensions."
	camera.resolution = tuple(res)
	camera.start_recording(filename)
	camera.wait_recording(time_s)
	camera.stop_recording()


def stream_to(address):


	# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
	# all interfaces)
	server_socket = socket.socket()
	server_socket.bind((address, 8000))
	server_socket.listen(0)

	# Accept a single connection and make a file-like object out of it
	connection = server_socket.accept()[0].makefile('rb')
	try:
	    # Run a viewer with an appropriate command line. Uncomment the mplayer
	    # version if you would prefer to use mplayer instead of VLC
	    cmdline = ['vlc', '--demux', 'h264', '-']
	    #cmdline = ['mplayer', '-fps', '25', '-cache', '1024', '-']
	    player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
	    while True:
	        # Repeatedly read 1k of data from the connection and write it to
	        # the media player's stdin
	        data = connection.read(1024)
	        if not data:
	            break
	        player.stdin.write(data)
	finally:
	    connection.close()
	    server_socket.close()
	    player.terminate()