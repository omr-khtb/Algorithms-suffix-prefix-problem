class Node:
    def __init__(self):
        self.children = {}
        self.suffix_link = None
        self.start = None
        self.end = None


def build_generalized_suffix_tree(strings):
    strings = [s + '$' for s in strings]
    root = Node()

    for i, string in enumerate(strings):
        current = root
        for j, char in enumerate(string):
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]

            if current.start is None:
                current.start = i
            current.end = i

    return root


def dfs_traversal(node, stacks, answers, current_string, depth):
    if node.start is not None:
        stacks[current_string].append((depth, node))

    for char, child in node.children.items():
        dfs_traversal(child, stacks, answers, current_string, depth + 1)

    if node.end == current_string:
        for i, stack in enumerate(stacks):
            while stack and stack[-1][0] >= depth:
                top_depth, top_node = stack.pop()
                answers[i] = (top_node.start, top_node.end, depth)


def find_suffix_prefix_matches(strings):
    tree = build_generalized_suffix_tree(strings)
    stacks = [[] for _ in range(len(strings))]
    answers = [None] * len(strings)

    dfs_traversal(tree, stacks, answers, 0, 0)

    return answers


# Example usage:
strings = ["abab", "baba", "abacaba"]
result = find_suffix_prefix_matches(strings)
print(result)
