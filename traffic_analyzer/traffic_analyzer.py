from scapy.all import sniff

def analyze_packet(packet):
    if packet.haslayer('IP'):
        ip_packet = packet['IP']
        print(f"[IP] Source: {ip_layer.src} -> Destination: {ip_layer.dst}")
    
    if packet.haslayer('TCP'):
        tcp_layer = packet['TCP']
        print(f"[TCP] Source Port: {tcp_layer.sport} -> Destination Port: {tcp_layer.dport}")

    if packet.haslayer('UDP'):
        udp_layer = packet['UDP']
        print(f"[UDP] Source Port: {udp_layer.sport} -> Destination Port: {udp_layer.dport}")

def start_sniffing(interface):
    print(f"Starting packet capture on {interface}...")
    sniff(iface=interface, prn=analyze_packet, count=10)

if __name__ == "__main__":
    interface = 'eth0'
    start_sniffing(interface)