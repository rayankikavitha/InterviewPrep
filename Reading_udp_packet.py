# UDP packet data starts at 3rd byte.
# read the 3rd position of every line. It gives UDP packet sequence.
# This function should check for packet sequence, and if the sequence is missing return delta.

import pyshark
 
def get_capture_count():
    p = pyshark.FileCapture('/Users/kavitha.rayanki/Downloads/real-camera-1s.pcapng', keep_packets=False)
 
    packet_counter = 0
    def counter(*args):
        packet_counter += 1
 
    p.apply_on_packets(counter, timeout=100000)
 
    return packet_counter
 



def udp_packet_seq_check(cap):
	n=get_capture_count()
	print n
	prevseq = None
	for i in range(n):
		curseq = int(cap[i].data.data[4:6],16)
		if prevseq:
			delta = curseq - prevseq
			if delta > 1:
				print "delta =",delta
			print curseq 
		prevseq = curseq





