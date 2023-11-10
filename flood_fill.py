"""
take the input = [
                    [1,1,1],
                    [1,1,0],
                    [1,0,1]
                 ]
src = [1,1]
color = 2

Bread first approach

queue = []
queue.enqueue(1,1)
while queue is not empty:
    node = queue.dequeue()
    1. change the color of position to 2
    2. find the neighbors of the node:
        2.1 x=1, y=1 with 4-neighbour
                   (x-1,y)
                      |
         (x,y-1)<---(x,y) --->(x,y+1)
                      |
                   (x+1,y)
        2.2  Generate four points based on above
             (x-1,y) (x+1,y) (x,y-1) (x,y+1)
             (0,1)   (2,1)   (1,0)   (1,2)
        2.3  Check if the four positions are valid, no negative numbers
             All are valid (0,1)   (2,1)   (1,0)   (1,2)
        2.4  Check if the four positions are same color,
             If yes, add them to the queue. If no, dont add.
             queue.enqueue(0,1)
             queue.enqueue(1,0)
             # skip adding (2,1) & (1,2) as they are not same color
"""
import time
input = [[1,1,1],
         [1,1,0],
         [1,0,1],
        ]
src = [1,1]
color = 2


def flood_fill(input, src, color):
    queue = []
    queue.append(src)
    save_color_src = input[src[0]][src[1]]
    input[src[0]][src[1]] = 2
    upper_limit_input_y = len(input[0])
    upper_limit_input_x = len(input)
    print(f"upper_limit_input_y {upper_limit_input_y}")
    print(f"upper_limit_input_x {upper_limit_input_x}")

    while len(queue)>0:
        print(f"input values {input}")
        # time.sleep(1)
        print(f"queue {queue}")
        node = queue.pop(0)
        print(f"processing node {node}")
        if input[node[0]][node[1]] == save_color_src:
            # change color
            print(f"changing color from {save_color_src} to {color} for {node}")
            input[node[0]][node[1]] = color
        # generate neighbors
        neighbors = []
        neighbors.append([node[0]-1, node[1]])
        neighbors.append([node[0]+1, node[1]])
        neighbors.append([node[0], node[1]-1])
        neighbors.append([node[0], node[1]+1])
        print(f"neighbors {neighbors}")
        for neighbor in neighbors:
            if neighbor[0] < 0 or neighbor[1] < 0:
                # lower limit
                print(f"skip lower {neighbor}")
                continue
            elif neighbor[0] >= upper_limit_input_x or neighbor[1] >= upper_limit_input_y:
                # upper limit
                print(f"skip upper {neighbor}")
                continue
            elif input[neighbor[0]][neighbor[1]] == color:
                # print(f"adding neighbor {neighbor}")
                print(f"color already changed {neighbor}")
                continue
            elif input[neighbor[0]][neighbor[1]] == save_color_src:
                print(f"adding neighbor {neighbor}")
                queue.append(neighbor)
            else:
                print(f"color not match {neighbor}")
                continue
        # print(f"queue {queue}")
    return input

print(f"before input: {input}")
output = flood_fill(input, src, color)
print(f"before output: {output}")



