import csv

input_file = "filter_log.csv"
trusted_vendors = ["hp", "dell"]  

suspicious_devices = []

with open(input_file, "r") as infile:
    csv_reader = csv.reader(infile, delimiter=' ')  

    for row in csv_reader:
        if len(row) < 5:
            continue  
        
        mac = row[1]
        vendor = row[4].strip().lower()  

        if vendor not in trusted_vendors:
            suspicious_devices.append((mac, vendor))

if suspicious_devices:
    print("Suspicious devices found:")
    for mac, vendor in suspicious_devices:
        print(f"MAC Address: {mac}, Vendor: {vendor.capitalize()}")
else:
    print("No suspicious devices found.")

