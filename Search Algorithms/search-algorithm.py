import random
import tkinter as tk

# Define the maze dimensions
rows = 6
columns = 6

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    def is_available(self,value):
        temp_list=[]
        for i in range(len(self.items)):
            temp_list.append(self.pop())
        temp_list.reverse()
        for i in range(len(temp_list)):
            self.push(temp_list[i])
        return value in temp_list
        
stack=Stack()


# Create an empty maze grid
maze = []
for j in range(rows):
    row = []
    for i in range(columns):
        row.append(' ')
    maze.append(row)


# Randomly select the starting node within 0-11 nodes
start_x = random.randint(0,1)
start_y = random.randint(0,5)
start_node=start_x,start_y

# Randomly select the goal node within 24-35 nodes
goal_x = random.randint(columns-2,columns-1)
goal_y = random.randint(0,5)
goal_node=goal_x,goal_y


# Set the starting and goal nodes in the maze
maze[start_y][start_x] = 'S'
maze[goal_y][goal_x] = 'G'

# Randomly select 4 barrier nodes within 12-23 nodes
barrier_nodes = set()
while len(barrier_nodes) < 4:
    node_x = random.randint(1, columns - 1)
    node_y = random.randint(0, 5)
    if (node_y != start_y or node_x != start_x) and (node_y != goal_y or node_x != goal_x):
        barrier_nodes.add((node_y, node_x))

# Set barrier nodes in the maze
for node_y, node_x in barrier_nodes:
    maze[node_y][node_x] = 'X'
    
stack.push((start_x,start_y))

def is_valid_move(x, y):
    return 0 <= x < rows and 0 <= y < columns and maze[y][x] != 'X' and maze[y][x] != 'S'

""" Start of DFS Search """

goal_found=False

def dfs():
    global goal_found

    # Storage for the nodes of visited and path
    came_from = {}
    visited=[]

    while not stack.is_empty() and not goal_found:
        x, y = stack.pop()

        if 0 <= x < columns and 0 <= y < rows and maze[y][x] != 'X' :
            if maze[y][x] !='S':
                visited.append((x, y))

            if maze[y][x] == 'G':
                goal_found = True
                break

            # Add neighboring nodes to stack and update came_from dictionary
            for neighbor in [(x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y + 1),
                            (x, y - 1), (x - 1, y + 1), (x - 1, y), (x - 1, y - 1)]:
                
                if is_valid_move(neighbor[0], neighbor[1]) and not stack.is_available(neighbor) and neighbor not in came_from :
                    stack.push(neighbor)
                    came_from[neighbor] = (x, y)
                    

    return came_from, visited

came_from_dict, dfs_visited_nodes = dfs()
path=[]

print("DFS visited nodes: ",dfs_visited_nodes)
print("DFS Time cost: ",len(dfs_visited_nodes))

# backtrack the path from goal to start using came_from dictionary
path = []
current_node = goal_node
while current_node in came_from_dict:
    path.insert(0, current_node)
    current_node = came_from_dict[current_node]

for node in path:
    x,y=node
    if maze[y][x] not in ['S','G']:
        maze[y][x]='*'

print("DFS path from start node to goal node:", path)
print("DFS Path cost: ",len(path))
print('DFS Maze:')
for row in maze:
    print("+" + " + ".join(["--" for _ in range(columns-1)]) + " +")
    print("| " + " | ".join(row) + " |")
print("+" + " + ".join(["--" for _ in range(columns-1)]) + " +")
    
if not goal_found:
    print("DFS Goal not found")
    # To print the visited nodes in maze
    # for nodes in visited_nodes:
    #     x,y=nodes
    #     if maze[y][x] not in ['S','G']:
    #         maze[y][x]='*'
    # for row in maze:
    #     print("+" + " + ".join(["--" for _ in range(columns-1)]) + " +")
    #     print("| " + " | ".join(row) + " |")
    # print("+" + " + ".join(["--" for _ in range(columns-1)]) + " +")
    
print('\n\n')


    
""" Start of A* Search """
    
def calculate_manhattan_distance(node, goal_node):
    return abs(node[0] - goal_node[0]) + abs(node[1] - goal_node[1])


for row in range(columns):
    for column in range(rows):
        current_node=row,column
        if maze[column][row]!='S' and maze[column][row]!='X':
            maze[column][row]=str(calculate_manhattan_distance(current_node,goal_node))

def a_star_search():
    visited_nodes = []
    open_list = [(0, start_node)]
    came_from = {}
    actual_cost = {start_node: 0}
    total_cost = {start_node: calculate_manhattan_distance(start_node, goal_node)}
    
    while open_list:
        open_list.sort()
        current_node = open_list.pop(0)[1]
        visited_nodes.append(current_node)
        if current_node == goal_node:
            maze[current_node[1]][current_node[0]]='G'
            
            # Construct the path
            path = []
            while current_node in came_from:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            return path,visited_nodes

        for neighbor in [(current_node[0] - 1, current_node[1] - 1), (current_node[0] - 1, current_node[1]),
                        (current_node[0] - 1, current_node[1] + 1), (current_node[0], current_node[1] - 1),
                        (current_node[0], current_node[1] + 1), (current_node[0] + 1, current_node[1] - 1),
                        (current_node[0] + 1, current_node[1]), (current_node[0] + 1, current_node[1] + 1)]:
            if is_valid_move(neighbor[0], neighbor[1]):
                visited_score = actual_cost[current_node] + 1
                if neighbor not in actual_cost or visited_score < actual_cost[neighbor]:
                    came_from[neighbor] = current_node
                    actual_cost[neighbor] = visited_score
                    print(actual_cost)
                    total_cost[neighbor] = visited_score + int(maze[neighbor[1]][neighbor[0]])
                    if neighbor not in [node[1] for node in open_list]:
                        open_list.append((total_cost[neighbor], neighbor))
                        
        
    return None,visited_nodes


path_a_star, a_star_visited_nodes = a_star_search()
maze[goal_y][goal_x]='G'
a_star_visited_nodes.pop(0)

for row in range(columns):
    for column in range(rows):
        if maze[column][row] not in ['S','G','*','X']:
            maze[column][row]=' '
            
print('A* Cost to reach the goal: ',len(a_star_visited_nodes))
print('A* Visited nodes ',a_star_visited_nodes)

if path_a_star:
    print('A* Path Cost: ',len(path_a_star))
    print("A* Final Path:", path_a_star)
else:
    print("Goal not reachable from the starting node using A*.")
    
if path_a_star:
    for node in path_a_star:
        x, y = node
        if maze[y][x] not in['S','G']:
            maze[y][x] = '*'

# Print the A* search maze
print("A* Search Maze:")
for row in maze:
    print("+" + " + ".join(["--" for _ in range(columns-1)]) + " +")
    print("| " + " | ".join(row) + " |")
print("+" + " + ".join(["--" for _ in range(columns-1)]) + " +")



""" Print the path for visited nodes in console if not found"""

# for node in visited_nodes:
#     x, y = node
#     if maze[y][x] not in['S','G']:
#         maze[y][x] = '*'
# # # Print the A* search maze
# print("A* Search Maze:")
# for row in maze:
#     print("+" + " + ".join(["--" for _ in range(columns-1)]) + " +")
#     print("| " + " | ".join(row) + " |")
# print("+" + " + ".join(["--" for _ in range(columns-1)]) + " +")





"""Plot the maze in GUI"""
cell_numbers={}

count = 0
for row in range(rows):
    for column in range(columns):
        cell_numbers[(row, column)] = count
        count += 1
        
cell_size=90

def plot_maze(maze,title,path,visited_nodes):
    window=tk.Toplevel()
    window.title(title)

    canvas = tk.Canvas(window, width=columns * cell_size, height=rows * cell_size)
    canvas.pack()


    # Draw the maze
    for row in range(rows):
        for column in range(columns):
            x1, y1 = column * cell_size, row * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size


            canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")

            # plot the start node
            if (column, row) == start_node:
                canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red")
                canvas.create_text(x1 + 0.5 * cell_size, y1 + 0.5 * cell_size, text="S", fill="white", font=("Times", 18, "bold"))

            # plot the goal node
            elif (column, row) == goal_node:
                canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green")
                canvas.create_text(x1 + 0.5 * cell_size, y1 + 0.5 * cell_size, text="G", fill="white", font=("Arial", 18, "bold"))

            # plot the barrier nodes
            elif(maze[row][column])=='X':
                canvas.create_rectangle(x1, y1, x2, y2, outline="grey", fill="black")
                canvas.create_text(x1 + 0.5 * cell_size, y1 + 0.5 * cell_size, text=cell_numbers[(column, row)], fill="white")
                
            else:
                    canvas.create_text(x1 + 0.5 * cell_size, y1 + 0.5 * cell_size, text=cell_numbers[(column, row)], fill="black")

            try:
                # plot the path
                if (column, row) in path and (column,row)!= start_node and (column,row)!= goal_node:
                    canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="yellow")
                    canvas.create_text(x1 + 0.5 * cell_size, y1 + 0.5 * cell_size, text=cell_numbers[(column, row)], fill="black", font=("Times", 18))
                
                # plot the visited nodes
                elif (column, row) in visited_nodes and (column, row) not in path and (column,row)!=start_node and (column,row)!=goal_node:
                    canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#e66c6c")
                    canvas.create_text(x1 + 0.5 * cell_size, y1 + 0.5 * cell_size, text=cell_numbers[(column, row)], fill="black", font=("Helvetica", 15))
                
            except TypeError:
                if (column, row) in visited_nodes and (column,row)!= start_node and (column,row)!= goal_node:
                    canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="#e66c6c")
                    canvas.create_text(x1 + 0.5 * cell_size, y1 + 0.5 * cell_size, text=cell_numbers[(column, row)], fill="black", font=("Helvetica",15))
                    
    return window

DFS=plot_maze(maze,"DFS",path,dfs_visited_nodes)

A_STAR=plot_maze(maze,"A* Search",path_a_star,a_star_visited_nodes )



DFS.geometry("540x540+0+25")
A_STAR.geometry("540x540+600+25")


tk.mainloop()