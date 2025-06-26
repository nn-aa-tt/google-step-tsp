import math

def tsp(cities):
    n = len(cities)
    current_city = 0
    path = [current_city] 
    not_visited_cities = [range(0,n)]

    distance = [[0] * n for i in range(n)] #都市間の距離を記録する行列
    for i in range(n):
        for j in range(n):
            distance[i][j] = math.sqrt((cities[i][0]-cities[j][0]) ** 2 + (cities[i][1]-cities[j][1]) ** 2)

    while len(path) < n:
        next_city = None
        for i in not_visited_cities:
            if distance[current_city][i] == min(distance[current_city]):
                next_city = i
                not_visited_cities.remove(i)
                path.append(next_city)
                break

    return path

if _name_ = "_main_":
    path = tsp(sys.argv[1])
    print(path)



