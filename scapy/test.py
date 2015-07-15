from scapy.all import *

tcp = TCP()
print "[+] Displaying TCP Packet details..."
print tcp.show()

ip = IP()
print "[+] Displaying IP Packet details..."
print ip.show()

ether = Ether()
print "[+] Displaying Ether details..."
print ether.show()

print "[+] Layering packets..."
packet = ether/ip/tcp
print "[+] Displaying layered packet details..."
packet.show()
