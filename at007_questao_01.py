from parse import parse # type: ignore
filename = "sistema.log"

def main():   
 # open the log file
    with open(filename, 'r') as f:
        # read lines into list (one item per line)
        data = f.readlines()
        # print the size of the array with the log file lines
        print(len(data))

if __name__ == "__main__":
    main()