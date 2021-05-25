############------------ IMPORTS ------------############
from queue import PriorityQueue
import math


############------------ HELPER CODE ------------############
def heuristic_measure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def generate_path(prev, start, goal):
    current = goal
    path = [current]
    while current is not start:
        current = prev[current]
        path.append(current)
    path.reverse()
    return path


############------------ FUNCTION ------------############
def shortest_path(graph, start, goal):

    path_queue = PriorityQueue()
    path_queue.put(start, 0)

    prev = {start: None}
    score = {start: 0}

    while not path_queue.empty():
        current = path_queue.get()

        if current == goal:
            generate_path(prev, start, goal)

        for node in graph.roads[current]:
            update_score = score[current] + heuristic_measure(
                graph.intersections[current], graph.intersections[node])

            if node not in score or update_score < score[node]:
                score[node] = update_score
                total_score = update_score + \
                    heuristic_measure(
                        graph.intersections[current], graph.intersections[node])
                path_queue.put(node, total_score)
                prev[node] = current

    return generate_path(prev, start, goal)
