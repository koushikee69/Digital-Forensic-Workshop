from scapy.all import rdpcap

# Function to extract unique IP addresses
def extract_ips(packet, client_ips, server_ips):
    if packet.haslayer('IP'):
        ip_data = packet['IP']
        client_ips.add(ip_data.src)  # Add client IP
        server_ips.add(ip_data.dst)  # Add server IP

# Function to track client-server communication pairs
def extract_client_server_pairs(packet, client_server_pairs):
    if packet.haslayer('IP'):
        ip_data = packet['IP']
        client_server_pairs.add((ip_data.src, ip_data.dst))

# Function to extract transport layer (TCP/UDP) ports
def extract_ports(packet, server_ports, client_ports):
    if packet.haslayer('TCP') or packet.haslayer('UDP'):
        transport_layer = packet.getlayer('TCP') if packet.haslayer('TCP') else packet.getlayer('UDP')
        server_ports.add(transport_layer.dport)  # Add server port
        client_ports.add(transport_layer.sport)  # Add client port

# Function to track protocols
def extract_protocols(packet, protocols):
    if packet.haslayer('TCP'):
        protocols.add('TCP')
    elif packet.haslayer('UDP'):
        protocols.add('UDP')
    elif packet.haslayer('ICMP'):
        protocols.add('ICMP')
    elif packet.haslayer('ARP'):
        protocols.add('ARP')

# Function to process the pcap file
def process_pcap(file_path):
    # Load the pcap data
    packets = rdpcap(file_path)

    # Initialize sets to store unique data
    client_ips = set()
    server_ips = set()
    client_server_pairs = set()
    server_ports = set()
    client_ports = set()
    protocols = set()

    # Process each packet using the above functions
    for packet in packets:
        extract_ips(packet, client_ips, server_ips)
        extract_client_server_pairs(packet, client_server_pairs)
        extract_ports(packet, server_ports, client_ports)
        extract_protocols(packet, protocols)

    # Return the collected data
    return client_ips, server_ips, client_server_pairs, server_ports, client_ports, protocols

# Function to print the results
def print_results(client_ips, server_ips, client_server_pairs, server_ports, client_ports, protocols):
    print(f"Total number of distinct server IP addresses: {len(server_ips)}")
    print(f"Total number of distinct client IP addresses: {len(client_ips)}")
    print(f"Number of unique client-server interactions: {len(client_server_pairs)}")
    print(f"Total distinct server ports used: {len(server_ports)}")
    print(f"Total distinct client ports used: {len(client_ports)}")
    print(f"List of network protocols detected: {protocols}")

# Main execution
if __name__ == "__main__":
    # Define the pcap file path
    pcap_file_path = '/home/c204-002/Downloads/ipp.pcap'

    # Process the pcap file
    client_ips, server_ips, client_server_pairs, server_ports, client_ports, protocols = process_pcap(pcap_file_path)

    # Print the results
    print_results(client_ips, server_ips, client_server_pairs, server_ports, client_ports, protocols)

