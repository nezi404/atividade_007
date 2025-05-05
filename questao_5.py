from parse import parse
filename = "sistema.log"

def open_file(file):
     # open the log file
    with open(file, 'r') as f:
        # read lines into list (one item per line)
        data = f.readlines()
        return data

def count_sucess_loggins(data):
    counter = 0
    value = "Accepted password"
    for x in data:
        fmt = "{month} {day} {time} {server} sshd[{number}]: {msg}"
        result = parse(fmt, str(x))

        if result:
            if value in result.named["msg"]:
                counter+=1
    
    print(f"Number of accepted loggins: {counter}")

def count_failed_loggins(data):
    counter = 0
    value = "Failed password"
    for x in data:
        fmt = "{month} {day} {time} {server} sshd[{number}]: {msg}"
        result = parse(fmt, str(x))

        if result:
            if value in result.named["msg"]:
                counter+=1
    
    print(f"Number of failed loggins: {counter}")

def main():   
    data = open_file(filename)
    count_sucess_loggins(data)
    count_failed_loggins(data)

if __name__ == "__main__":
    main()