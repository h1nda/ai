def load_cities(filename):
    with open(filename) as file:
        return [line.rstrip() for line in file]

def load_dists(filename):
    with open(filename, 'r') as file:
        return [[int(num) for num in line.split()] for line in file]

def create_dict(cities, dist_matrix):
    dictionary = {}
    for i, cityA in enumerate(cities):
        for j, cityB in enumerate(cities):
            dictionary[(cityA,cityB)] = dist_matrix[i][j]
    
    return dictionary

def init(city_filename, dist_filename):
    cities = load_cities(city_filename)
    dist_matrix = load_dists(dist_filename)
    return cities, create_dict(cities,dist_matrix)

def main():
    cities, d = init("./data/uk12_code.txt", "./data/uk12_dist.txt")
    print(cities)

if __name__ == "__main__":
    main()