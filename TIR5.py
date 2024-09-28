import socket
import struct

localIP = '127.0.0.1'
targetIP = '127.0.0.1'
port = 4242
bufferSize = 1024
TIRtranslationalConst = 5.12							#track ir translation constant, unclear why the output appears to be multiplied by 5.12, but this corrects it

# socket.shutdown(socket.SHUT_RDWR)                                           #untested expiriment
# socket.close()                                                              #untested expiriment
print('starting UDP socket connection')
UDPSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
UDPSocket.bind((localIP, port))
print('UDP socket is up')


def update():
	x       = trackIR.x / TIRtranslationalConst
	y       = trackIR.y / TIRtranslationalConst
	z       = trackIR.z / TIRtranslationalConst
	pitch   = trackIR.pitch
	yaw     = trackIR.yaw
	roll    = trackIR.roll

	UDPSocket.sendto( struct.pack( '<6d', x, y, z, yaw, pitch, roll ), ( targetIP, port ) ) #sequence matters, yaw before pitch. Thanks opentrack

  # diagnostics window in freepie, removed from final build for potential performance gains. If unsure if things are working on freepie, uncomment the 6 lines below here
	# diagnostics.watch(x)
	# diagnostics.watch(y)
	# diagnostics.watch(z)
	# diagnostics.watch(pitch)
	# diagnostics.watch(yaw)
	# diagnostics.watch(roll)


if starting:
	trackIR.update += update





# if someone is after making the inverse of this script, reading from opentrack into freepie, you would want to use
# data, _ = UDPServerSocket.recvfrom(48)
# unpackedData = struct.unpack('<6d', data[0:48])
# these would create a tuple with the 6 datapoints required for x y z ry rx rz
