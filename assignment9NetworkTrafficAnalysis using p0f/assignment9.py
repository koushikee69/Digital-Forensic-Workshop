from collections import Counter

def extract_column(file_path, column_index, separator):
    """
    This function reads a file and returns a list of values from a specified column
    based on the given separator.
    """
    with open(file_path, 'r') as file:
        return [line.strip().split(separator)[column_index] for line in file if len(line.strip().split(separator)) > column_index]

def get_unique_elements(elements):
    """
    This function returns a list of unique elements from the given list.
    """
    return list(set(elements))

def process_log_data(file_path):
    """
    This function processes the log file, extracting relevant details and performing 
    analysis to identify unique clients, servers, ports, and activity.
    """
    timestamps = extract_column(file_path, 0, ' ')
    clients = extract_column(file_path, 1, ' ')
    servers = extract_column(file_path, 2, ' ')
    server_ports = extract_column(file_path, 3, ' ')
    client_ports = extract_column(file_path, 4, ' ')
    packet_timestamps = extract_column(file_path, 5, ' ')
    os_details = extract_column(file_path, 6, ' ')

    unique_clients = get_unique_elements(clients)
    unique_servers = get_unique_elements(servers)
    unique_connections = get_unique_elements([f"{c}-{s}" for c, s in zip(clients, servers)])
    unique_server_ports = get_unique_elements(server_ports)
    unique_client_ports = get_unique_elements(client_ports)

    server_port_counts = Counter(server_ports)
    client_port_counts = Counter(client_ports)

    most_common_server_port = server_port_counts.most_common(1)[0] if server_port_counts else (None, 0)
    least_common_server_port = server_port_counts.most_common()[-1] if server_port_counts else (None, 0)
    most_common_client_port = client_port_counts.most_common(1)[0] if client_port_counts else (None, 0)
    least_common_client_port = client_port_counts.most_common()[-1] if client_port_counts else (None, 0)

    latest_timestamp = max(packet_timestamps)
    earliest_timestamp = min(packet_timestamps)

    unique_os = get_unique_elements(os_details)

    client_activity = {}
    for client, timestamp in zip(clients, timestamps):
        client_activity[client] = client_activity.get(client, 0) + 1

    most_active_client = max(client_activity, key=client_activity.get)

    # Displaying the analysis results
    print(f"Distinct Clients: {len(unique_clients)}")
    print(f"Distinct Servers: {len(unique_servers)}")
    print(f"Distinct Client-Server Pairs: {len(unique_connections)}")
    print(f"Distinct Server Ports: {len(unique_server_ports)}")
    print(f"Distinct Client Ports: {len(unique_client_ports)}")
    print(f"Most Frequent Server Port: {most_common_server_port[0]} ({most_common_server_port[1]} occurrences)")
    print(f"Least Frequent Server Port: {least_common_server_port[0]} ({least_common_server_port[1]} occurrences)")
    print(f"Most Frequent Client Port: {most_common_client_port[0]} ({most_common_client_port[1]} occurrences)")
    print(f"Least Frequent Client Port: {least_common_client_port[0]} ({least_common_client_port[1]} occurrences)")
    print(f"Most Recent Packet Timestamp: {latest_timestamp}")
    print(f"Earliest Packet Timestamp: {earliest_timestamp}")
    print(f"Detected Operating Systems: {', '.join(unique_os)}")
    print(f"Most Active Client: {most_active_client}")

# Main execution
if __name__ == "__main__":
    log_file = 'p0f.log'
    process_log_data(log_file)

