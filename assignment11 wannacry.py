import subprocess
import sys
import re

def main():
    filter_flag = '-r' in sys.argv
    filter_pid = None
    filter_image = None

    if filter_flag:
        try:
            filter_pid = sys.argv[sys.argv.index('-r') + 1]
            filter_image = sys.argv[sys.argv.index('-r') + 2]
        except IndexError:
            print("Error: Missing arguments for filter.")
            sys.exit(1)

    with open("report.log", "w") as log_file, open("commands.txt", "r") as txt_file:
        for line in txt_file:
            command = line.strip()  # Remove leading/trailing whitespace
            if not command:  # Skip empty lines
                continue
            
            # Construct the command list
            command_list = ['sudo', '/home/c204-002/Downloads/volatility3-develop/vol.py', '-f', 'wcry.raw', command]
            result = subprocess.run(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            log_file.write(f"Command: {' '.join(command_list)}\n")  # Join command for readable output
            log_file.write(result.stdout)
            if result.stderr:
                log_file.write("\nErrors:\n" + result.stderr)
            log_file.write("=" * 40 + "\n")

    if filter_flag:
        with open("report.log", "r") as log_file:
            lines = log_file.readlines()
        with open("report.log", "w") as log_file:
            for line in lines:
                if re.search(rf"\b{filter_pid}\b", line) or re.search(rf"\b{filter_image}\b", line, re.IGNORECASE):
                    log_file.write(line)

if __name__ == "__main__":
    main()

