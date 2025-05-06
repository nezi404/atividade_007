from collections import Counter
import re

filename = "sistema.log"

def open_file(file):
    with open(file, 'r') as f:
        return f.readlines()

def extract_ips(data):
    ips = []
    for line in data:
        if "Accepted password" in line:
            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ips.append(match.group(1))
    return ips

def count_ips(ips):
    return Counter(ips).most_common()

def main():
    data = open_file(filename)
    ips = extract_ips(data)
    ip_counts = count_ips(ips)

    for ip, count in ip_counts:
        print(f"{ip}: {count}")

if __name__ == "__main__":
    main()
