from scapy.all import *

def extract_http_headers(packet):
    if packet.haslayer(Raw):
        raw_data = packet[Raw].load.decode('utf-8', errors='ignore')
        
        if "HTTP" in raw_data:
            print(raw_data)

sniff(prn=extract_http_headers, filter="tcp port 80", store=0)
