def _fake_anti_uni_distance(node1, node2):
    stack1 = deque([node1])
    stack2 = deque([node2])
    same = 0
    diff = 0
    while stack1 or stack2:
        if stack1:
            _node1 = stack1.popleft()
            if type(_node1).__name__ == 'Load':
                try:
                    _node1 = stack1.popleft()
                except IndexError:
                    _node1 = None
        else:
            _node1 = None
        if stack2:
            _node2 = stack2.popleft()
            if type(_node2).__name__ == 'Load':
                try:
                    _node2 = stack2.popleft()
                except IndexError:
                    _node2 = None
        else:
            _node2 = None
        if type(_node1).__name__ == type(_node2).__name__:
            same += 1
        else:
            diff += 1
        if _node1 and _node2:
            stack1.extend(ast.iter_child_nodes(_node1))
            stack2.extend(ast.iter_child_nodes(_node2))
    return 1.0 * same / (same + diff)
       