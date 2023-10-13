

def get_combos(steps):
    output = 0
    queue = []
    queue.append(steps)
    step_list = [1,2]
    while len(queue) > 0:
        node = queue.pop(0)
        for each_step in step_list:
            if node - each_step > 0:
                new_node = node - each_step
                print(f"for {new_node} added {each_step}")
                queue.append(new_node)
            elif node - each_step == 0:
                print(f"Reached destination for {node} with {each_step}")
                output += 1
            elif node - each_step < 0:
                continue
            print(f"output={output}")
    print(f"number of ways to climb step={steps} is {output}")

get_combos(4)