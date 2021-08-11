# Handle Collision with Separate Chaining -- Nodes and Linked Lists --------------------------------
from linked_list import Node, LinkedList
flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'], ['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'], ['magnolia',
                                                                                                                                                                                                 'dignity'], ['morning glory', 'unrequited love'], ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'], ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]


class HashMap:
    def __init__(self, size=0):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        payload = Node([key, value])

        list_at_array = self.array[array_index]

        for item in list_at_array:
            if key == item[0]:
                item[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        list_at_index = self.array[array_index]

        for item in list_at_index:
            if key == item[0]:
                return item[1]

        return None


blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

print(blossom.retrieve('daisy'))
