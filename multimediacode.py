import heapq
from collections import defaultdict, Counter
import pickle

class HuffmanNode:
    def __init__(self, char=None, frequency=None):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(data):
    # Count the frequency of each character
    frequency_counter = Counter(data)

    # Create a priority queue for Huffman nodes
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequency_counter.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)

        internal_node = HuffmanNode(frequency=left_child.frequency + right_child.frequency)
        internal_node.left = left_child
        internal_node.right = right_child

        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]  # The root of the Huffman tree

def build_huffman_codes(node, current_code="", code_dict=None):
    if code_dict is None:
        code_dict = {}

    if node is not None:
        if node.char is not None:
            code_dict[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", code_dict)
        build_huffman_codes(node.right, current_code + "1", code_dict)

    return code_dict

def huffman_encode(data):
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)

    # Encode the data using the Huffman codes
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

if __name__ == "__main__":
    # Example usage
    input_data = "STATE"

    # Encoding
    encoded_data, huffman_tree_root = huffman_encode(input_data)
    print("Encoded data:", encoded_data)

    # Saving the Huffman tree
    save_huffman_tree(huffman_tree_root)

    # Loading the Huffman tree
    loaded_huffman_tree = load_huffman_tree()

    # Decoding
    decoded_data = huffman_decode(encoded_data, loaded_huffman_tree)
    print("Decoded data:", decoded_data)