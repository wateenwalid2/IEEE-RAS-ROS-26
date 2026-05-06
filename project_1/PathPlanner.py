import heapq

class PathPlanner:
    def __init__(self, grid_size=20):
        self.grid_size = grid_size
        self.no_fly_zones = set() 
        
    def register_no_fly_zone(self, cluster):
        for coord in cluster:
            self.no_fly_zones.add(coord)

    def get_neighbors(self, node):
        x, y = node
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        return [
            n for n in neighbors 
            if 0 <= n[0] < self.grid_size and 0 <= n[1] < self.grid_size 
            and n not in self.no_fly_zones 
        ]

    def find_path(self, start, goal):
        if start == goal:
            return [] 
        
        frontier = [] 
        heapq.heappush(frontier, (0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while frontier:
            current = heapq.heappop(frontier)[1]
            if current == goal: break

            for next_node in self.get_neighbors(current):
                new_cost = cost_so_far[current] + 1 
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + abs(goal[0]-next_node[0]) + abs(goal[1]-next_node[1])
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current
        return self.reconstruct_path(came_from, start, goal)

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = []
        while current != start:
            if current not in came_from: return [] 
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path