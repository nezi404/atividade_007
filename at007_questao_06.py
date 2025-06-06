from parse import parse # type: ignore
filename = "sistema.log"

def open_file(file):
     # open the log file
    with open(file, 'r') as f:
        # read lines into list (one item per line)
        data = f.readlines()
        return data

def find_sudo_loggins(data):
    for x in data:
        fmt = "{month} {day} {time} {server} sudo[{number}]: {username} : {tty} ; PWD={pwd} ; USER={user} ; COMMAND={command}"
        result =parse(fmt, str(x))

        if result:
            print(result.named["username"])

def main():   
    data = open_file(filename)
    find_sudo_loggins(data)

if __name__ == "__main__":
    main()