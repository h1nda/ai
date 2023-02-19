def read_input(filename):
    with open(filename, 'r') as file:
        raw = [[int(num) for num in line.split()] for line in file]
        M = raw[0][0]
        N = raw[0][1]
        weight, cost = [list(output) for output in list(zip(*raw[1:]))]
        return M, N, weight, cost

def main():
    M, N, weight,cost = read_input("KP short test data.txt")
    print(weight)

if __name__ == "__main__":
    main()