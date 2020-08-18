#!/usr/bin/env python3.8

class HashTable():
    def __init__(self, size=2):
        self.container = [None] * size
        self.size = size

    def hash_function(self, key):
        return hash(key) % len(self.container)

    def insert(self, key, value):
        index = self.hash_function(key)
        if(self.container[index]):
            for k in self.container[index]:
                if(k[0] == key):
                    k[1] = value
                else:
                    self.container[index].append([key, value])
        else:
            self.container[index] = [[key, value]]

    def get(self, key):
        index = self.hash_function(key)
        if not(self.container[index]):
            raise KeyError(f'could not retrieve key {key}, no associated value')
        else:
            for k in self.container[index]:
                if(k[0] == key):
                    return k[1]

        raise KeyError(f'could not retrieve key {key}, no associated value')

    def is_full(self):
        items = 0
        for element in self.container:
            if not(element):
                items+=1
        print(items)
        return (items > len(self.container)/2)

    def resize(self):
        pass

H = HashTable()

H.insert("Hello", "World")
H.insert("Hola", "Fernando")
print(H.container)
# print(H.get("World"))
print(H.is_full())
