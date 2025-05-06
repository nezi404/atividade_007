filename = "sistema.log"

def open_file(file):
    with open(file, 'r') as f:
        return f.readlines()

def extract_sort_key(line):
    parts = line.split()
    if len(parts) < 3:
        return (0, "")  # linha incompleta
    try:
        day = int(parts[1])
        time = parts[2]  # formato: HH:MM:SS
        return (day, time)
    except ValueError:
        return (0, "")

def print_dates(data):
    for line in data:
        print(line.strip())

def main():
    data = open_file(filename)
    data.sort(key=extract_sort_key)
    print_dates(data)

if __name__ == "__main__":
    main()
