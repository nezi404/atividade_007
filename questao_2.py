from parse import parse
filename = "sistema.log"

def open_file(file):
     # open the log file
    with open(file, 'r') as f:
        # read lines into list (one item per line)
        data = f.readlines()
        return data

def find_sucess_loggins(data):
    value = "Accepted password"
    for x in data:
        fmt = "{month} {day} {time} {server} {user}[{number}]: {msg}"
        result = parse(fmt, str(x))

        if value in result.named["msg"]:
            print(result.named["msg"])

def main():   
    data = open_file(filename)
    find_sucess_loggins(data)

if __name__ == "__main__":
    main()