import heapq
from collections import defaultdict
import pickle

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    freq_map = defaultdict(int)
    for char in data:
        freq_map[char] += 1

    priority_queue = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left_node = heapq.heappop(priority_queue)
        right_node = heapq.heappop(priority_queue)

        merged_node = HuffmanNode(None, left_node.freq + right_node.freq)
        merged_node.left = left_node
        merged_node.right = right_node

        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_codes(node, current_code="", code_map=None):
    if code_map is None:
        code_map = {}

    if node is not None:
        if node.char is not None:
            code_map[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", code_map)
        build_huffman_codes(node.right, current_code + "1", code_map)

    return code_map

def huffman_encode(data):
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)

    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, root

def huffman_decode(encoded_data, root):
    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root

    return decoded_data

def save_huffman_tree(root, filename="huffman_tree.pkl"):
    with open(filename, "wb") as file:
        pickle.dump(root, file)

def load_huffman_tree(filename="huffman_tree.pkl"):
    with open(filename, "rb") as file:
        root = pickle.load(file)
    return root

# Example usage:
data_to_encode = input("Enter data to encode : ")
encoded_data, huffman_tree = huffman_encode(data_to_encode)

# Saving the Huffman tree
save_huffman_tree(huffman_tree)

# Loading the Huffman tree
loaded_huffman_tree = load_huffman_tree()

# Decoding
decoded_data = huffman_decode(encoded_data, loaded_huffman_tree)

print("Original data:", data_to_encode)
print("Encoded data:", encoded_data)
print("Decoded data:", decoded_data)