import heapq

class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
        self.huff = ""

    def __lt__(self, next):
        return self.freq < next.freq
    
def printNodes(node, val=""):
    newVal = val+str(node.huff)

    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

def huff_enc(symbols, freq):
    nodes = []

    for i in range(len(symbols)):
        heapq.heappush(nodes, Node(symbols[i], freq[i]))
    
    while len(nodes)>1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        newNode = Node(left.symbol+right.symbol, left.freq+right.freq, left, right)
        heapq.heappush(nodes, newNode)
    printNodes(nodes[0])


symbols = ['a', 'b', 'c', 'd', 'e', 'f'] 
freq = [5, 9, 12, 13, 16, 45] 

huff_enc(symbols, freq)