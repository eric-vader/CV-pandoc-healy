graph = {
    'S': {('A', 1), ('B', 5),  ('C', 15)},
    'A': {('G', 10), ('S', 1)},
    'B': {('G', 5), ('S', 5)},
    'C': {('G', 5), ('S', 15)},
    'G': set()
}

from priority_queue import PriorityQueue
from collections import defaultdict

def uniform_cost_search(graph, inital_node, goal_test, is_tree, is_update):

    node = inital_node
    frontier = PriorityQueue('min')
    frontier.append((node,''), 0)
    explored = set([inital_node])
    explored_l = []
    # raise NotImplementedError
    # print(f"Reached: {explored}\n")
    while frontier:
        _f = ' '.join([ f"{s[0]}({v}-{s[1]})" for v,s in sorted(frontier.heap)])
        _e = ' '.join(explored_l)
        print(f"Frontier: {_f}")
        print(f"Explored: {_e}")
        # print(' '.join([ f"{s}({v})" for v,s in sorted(frontier.heap)]))
        node_cost, (node, node_path) = frontier.pop()
        # print(f"Pop: {node}")
        # print(f"{_f}|{_e}")
        
        explored.add(node)
        explored_l.append(node)
        
        if goal_test(node):
            return node_path+node
        for child, cost in graph[node]:
            if child not in explored or is_tree:
                if child not in frontier or (not is_update):
                    frontier.append((child, node_path+node), cost + node_cost)
                    # print(f"Insert {child}")
                else:
                    if cost + node_cost < frontier[child]:
                        del frontier[child]
                        frontier.append((child, node_path+node), cost + node_cost)
                        # print(f"Update {child}")
    return None

print("=====")
print("Tree")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=True, is_update=False))
assert(p=="SBG")

print("=====")
print("Graph")
print("=====")
print(p:=uniform_cost_search(graph, 'S', lambda n: n=='G', is_tree=False, is_update=True))
assert(p=="SBG")