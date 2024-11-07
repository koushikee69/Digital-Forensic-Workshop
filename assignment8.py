def parse_log_file(file_path):
    """
    This function processes a log file to extract unique client and server details,
    timestamps, and client/server ports.
    """
    client_ips = set()     # Store unique client IPs
    server_ips = set()     # Store unique server IPs
    client_ports = set()   # Store unique client ports
    server_ports = set()   # Store unique server ports
    timestamps = set()     # Store timestamps from logs

    with open(file_path, 'r') as log_file:
        for line in log_file:
            log_parts = line.split('|')

            # Extract timestamp (first part of each log entry)
            timestamp = log_parts[0].strip("[]")

            # Find and extract client and server information from the log
            client_info = next(part for part in log_parts if part.startswith('cli='))
            server_info = next(part for part in log_parts if part.startswith('srv='))

            # Extract client IP and port from the 'cli' field
            client_ip, client_port = client_info.split("=")[1].split('/')

            # Extract server IP and port from the 'srv' field
            server_ip, server_port = server_info.split("=")[1].split('/')

            # Add extracted details to respective sets
            client_ips.add(client_ip)
            server_ips.add(server_ip)
            client_ports.add(client_port)
            server_ports.add(server_port)
            timestamps.add(timestamp)

    # Return collected data
    return client_ips, server_ips, timestamps, client_ports, server_ports


def display_results(client_ips, server_ips, timestamps, client_ports, server_ports):
    """
    This function prints the analysis results in a human-readable format.
    """
    print(f"Total number of distinct client IPs: {len(client_ips)}")
    print(f"Total number of distinct server IPs: {len(server_ips)}")
    print(f"Total unique client ports: {len(client_ports)}")
    print(f"Total unique server ports: {len(server_ports)}")
    print(f"Most recent timestamp: {max(timestamps)}")
    print(f"Oldest timestamp: {min(timestamps)}")


# Main execution
if __name__ == "__main__":
    # Log file path
    log_file_path = 'log.txt'

    # Parse the log file and extract the relevant details
    unique_clients, unique_servers, log_timestamps, client_ports, server_ports = parse_log_file(log_file_path)

    # Display the results of the analysis
    display_results(unique_clients, unique_servers, log_timestamps, client_ports, server_ports)

