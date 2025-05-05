from parse import parse
filename = "sistema.log"

def open_file(file):
     # open the log file
    with open(file, 'r') as f:
        # read lines into list (one item per line)
        data = f.readlines()
        return data


def cmp(date):
	date=date.split()
	print(date[1])
	print(date[2])
	return int(date[1]),date[2],


# Utility function to print the contents
# of the array
def printDates(dates, n):
	for i in range(n):
		print(dates[i])

def main():   
    data = open_file(filename)
    n = len(data)

	# Sort the dates
    data.sort(key=cmp)

	# Print the sorted dates
    printDates(data, n)

if __name__ == "__main__":
    main()