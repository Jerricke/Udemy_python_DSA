# hash 
# hash is ONE WAY -> you can only put the input in to get the output, never the output for the input
# hash is deterministic, the output will always be the same for the same input

# collisions
# chain links
# linear probing

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
            return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

mht = HashTable()

mht.set_item('bolts', 1400)
mht.set_item('washers', 50)
mht.set_item('lumber', 70)

mht.print_table()