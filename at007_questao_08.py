from parse import parse # type: ignore
filename = "sistema.log"

def open_file(file):
     # open the log file
    with open(file, 'r') as f:
        # read lines into list (one item per line)
        data = f.readlines()
        return data

def find_failed_loggins(data):
    name_arr =[]
    for x in data:
        fmt = "{month} {day} {time} {server} sshd[{number}]: Failed password for {username} from {ip} port {portid} {con}"
        result =parse(fmt, str(x))

        if result:
            name_arr.append(result.named["username"])
    if len(name_arr) > 0:
        rep_name_arr=[]
        for x in name_arr:
            if name_arr.count(x) > 1:
                if x not in rep_name_arr:
                    rep_name_arr.append(x)
                    print(x)
    print(name_arr)
       
def main():   
    data = open_file(filename)
    find_failed_loggins(data)

if __name__ == "__main__":
    main()