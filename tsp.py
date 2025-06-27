import math
import sys
from common import print_tour


def tsp(cities):
    n = len(cities)
    current_city = 0
    path = [current_city] 
    not_visited_cities = set(range(1,n))

    distance = [[0] * n for i in range(n)] #都市間の距離を記録する行列
    for i in range(n):
        for j in range(n):
            distance[i][j] = math.sqrt((cities[i][0]-cities[j][0]) ** 2 + (cities[i][1]-cities[j][1]) ** 2)

    while not_visited_cities:
        next_city = min(not_visited_cities,key = lambda city: distance[current_city][city])
        not_visited_cities.remove(next_city)
        path.append(next_city)
        current_city = next_city
        
    return path

if __name__ == "__main__":
    cities = []
    with open(sys.argv[1]) as f:
        for i in f.readlines()[1:]:
            xy = i.split(",")
            cities.append((float(xy[0]),float(xy[1])))
    path = tsp(cities)
    print_tour(path)
    with open(output_file, 'w') as f:
        f.write("index\n")
        for city in path:
            f.write(str(city) + '\n')

