# agent_idastar.py
import pygame

class Agent(pygame.sprite.Sprite):
    def __init__(self, environment, grid_size):
        super().__init__()
        self.grid_size = grid_size
        self.environment = environment
        self.position = [0, 0]  
        self.task_completed = 0
        self.completed_tasks = []
        self.path = []  
        self.moving = False  

        self.image = pygame.image.load("car.png")  
        self.image = pygame.transform.scale(self.image, (grid_size, grid_size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0) 

    def move(self):
        if self.path:
            next_position = self.path.pop(0)
            self.position = list(next_position)
            self.rect.topleft = (self.position[0] * self.grid_size, self.position[1] * self.grid_size)
            self.check_task_completion()
        else:
            self.moving = False  

    def check_task_completion(self):
        position_tuple = tuple(self.position)
        if position_tuple in self.environment.task_locations:
            task_number = self.environment.task_locations.pop(position_tuple)
            self.task_completed += 1
            self.completed_tasks.append(task_number)

    def find_nearest_task(self):
        nearest_task = None
        shortest_path = None
        for task_position in self.environment.task_locations.keys():
            path = self.idastar_search(task_position)
            if path:
                if not shortest_path or len(path) < len(shortest_path):
                    shortest_path = path
                    nearest_task = task_position
        if shortest_path:
            self.path = shortest_path[1:] 
            self.moving = True

    def idastar_search(self, goal):
        def dfs(path, g_cost, bound):
            node = path[-1]
            f_cost = g_cost + self.heuristic(node, goal)
            if f_cost > bound:
                return f_cost, None
            if node == goal:
                return f_cost, path
            
            min_threshold = float("inf")
            for neighbor in self.get_neighbors(*node):
                if neighbor not in path:
                    new_g_cost = g_cost + 1
                    new_path = path + [neighbor]
                    t, result = dfs(new_path, new_g_cost, bound)
                    if result:
                        return t, result
                    min_threshold = min(min_threshold, t)
            return min_threshold, None

        start = tuple(self.position)
        bound = self.heuristic(start, goal)
        path = [start]
        
        while True:
            t, result = dfs(path, 0, bound)
            if result:
                return result
            if t == float("inf"):
                return None
            bound = t

    def heuristic(self, pos, goal):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    def get_neighbors(self, x, y):
        neighbors = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.environment.is_within_bounds(nx, ny) and not self.environment.is_barrier(nx, ny):
                neighbors.append((nx, ny))
        return neighbors
