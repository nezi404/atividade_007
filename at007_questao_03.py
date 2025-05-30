import re
from parse import parse  # type: ignore

filename = "sistema.log"

def open_file(file):
    with open(file, 'r') as f:
        return f.readlines()

def find_ips_ssh(data):
    ips = []
    for line in data:
        if "Accepted password" in line:
            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ips.append(match.group(1))
    return ips

def main():
    data = open_file(filename)
    ips = find_ips_ssh(data)

    # Exibe os IPs únicos, ordenados
    for ip in sorted(set(ips)):
        print(ip)

if __name__ == "__main__":
    main()
