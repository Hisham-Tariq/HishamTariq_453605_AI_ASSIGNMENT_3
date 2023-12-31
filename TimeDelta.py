from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_format = "%a %d %b %Y %H:%M:%S %z"
    t1 = datetime.strptime(t1, date_format).timestamp()
    t2 = datetime.strptime(t2, date_format).timestamp()
    return str(int(abs(t1 - t2)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

