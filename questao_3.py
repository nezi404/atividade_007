from parse import parse
filename = "sistema.log"

def open_file(file):
     # open the log file
    with open(file, 'r') as f:
        # read lines into list (one item per line)
        data = f.readlines()
        return data

def find_ips_ssh(data):
    for x in data:
        fmt = "{month} {day} {time} {server} sshd[{number}]: Accepted password for {usern} {from} {ip} {port} {portn} {ssh2}"
        result = parse(fmt, str(x))

        if result:
            print(result.named["ip"])
    

def main():   
    data = open_file(filename)
    find_ips_ssh(data)

if __name__ == "__main__":
    main()