class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def merge_nodes(nodes):
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        nodes.append(new_node)
    return nodes[0]

def generate_huffman_codes(root, code, huffman_codes):
    if root:
        if root.char is not None:
            huffman_codes[root.char] = code
        generate_huffman_codes(root.left, code + "0", huffman_codes)
        generate_huffman_codes(root.right, code + "1", huffman_codes)

def huffman_encoding(text):
    freq_dict = {}
    for char in text:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    
    nodes = [Node(char, freq) for char, freq in freq_dict.items()]
    root = merge_nodes(nodes)
    
    huffman_codes = {}
    generate_huffman_codes(root, "", huffman_codes)
    
    encoded_text = "".join(huffman_codes[char] for char in text)
    
    return huffman_codes, encoded_text

text = input("Enter text: ")
codes, encoded_text = huffman_encoding(text)

print("Huffman Codes:")
for char, code in codes.items():
    print(f"'{char}': {code}")

print("Encoded Text:", encoded_text)
