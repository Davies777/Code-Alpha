from scapy.all import sniff

# Function to process packets
def packet_analyzer(packet):
    # Check if the packet has a layer of IP
    if packet.haslayer('IP'):
        ip_layer = packet.getlayer('IP')
        print(f"New Packet: {packet.summary()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
        print("="*50)

# Sniff the packets on the network interface, count=0 means continuous capture
print("Starting network sniffer...")
sniff(prn=packet_analyzer, count=0)


