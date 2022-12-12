

# A Huffman Tree Node
import heapq


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
Dict = {}
# 0 if compress 1 if de_compress

# characters for huffman tree
chars = []
# frequency of characters
freq = []


def compress():
    f = open("inn.txt", "r")
    Data = f.read()
    data_set = set(Data)
    numper_of_data = len(data_set)

    for i in data_set:
        chars.append(i)
        freq.append(Data.count(i))

    print(chars)
    print(freq)
    print(numper_of_data)

    Dict = huffman_tree(chars, freq)
    print(Dict)
    f2 = open("out_compress.txt", "a")
    for i in Data:
        print(Dict[i])
        f2.write(Dict[i])


def De_cpmpress():
    f = open("out_compress.txt", "r")
    Data = f.read()
    Dict = huffman_tree(chars, freq)
    d_swap = {v: k for k, v in Dict.items()}
    print(d_swap)
    print(Dict)
    f2 = open("out_De_compress.txt", "a")
    i = 0
    while i < len(Data):
        str_code = Data[i]
        Lenth = 1
        while str_code not in d_swap.keys():

            if i + Lenth < len(Data):
                str_code = str_code + Data[i + Lenth]
                Lenth += 1
        print(d_swap[str_code])
        f2.write(d_swap[str_code])
        i += Lenth


def Huff_Code(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if (node.left):
        Huff_Code(node.left, newVal)
    if (node.right):
        Huff_Code(node.right, newVal)

    # if node is edge node then
    # display its huffman code
    if (not node.left and not node.right):
        Dict[node.symbol] = newVal
        print(f"{node.symbol} -> {newVal}")
    return Dict


def huffman_tree(chars, freq):
    # chars = ['E','T','A','O','I','N','S','R','H','L','D','C','U']
    # freq = [125,93,80,76,72,71,65,61,55,41,40,31,27]

    # list containing unused nodes
    nodes = []

    # converting characters and frequencies
    # into huffman tree nodes
    for x in range(len(chars)):
        heapq.heappush(nodes, node(freq[x], chars[x]))

    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on their frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        heapq.heappush(nodes, newNode)

    # Huffman Tree is ready!
    return Huff_Code(nodes[0])


def main():
    compress()

    De_cpmpress()


if __name__ == '__main__':
    main()
