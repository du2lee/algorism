import heapq
'''
queue = []
heapq.heappush(queue,[2, 'A'])              #example input
heapq.heappush(queue,[5, 'B'])
heapq.heappush(queue,[1, 'C'])
heapq.heappush(queue,[7, 'D'])
print(queue)                                #example output
for i in range(len(queue)):
    print(heapq.heappop(queue))
'''

mygraph = {                                 #example data
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}


def dijkstra(graph, start):

    #Initialize

    distances = {node: float('inf') for node in graph}          #array of #Initialize#Initializes
    distances[start] = 0
    queue =[]                                                   #우선순위queue
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance,  current_node = heapq.heappop(queue)


        if distance[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].item():     
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

        


