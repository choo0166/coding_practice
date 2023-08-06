"""
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

put(key, value): adds a key-value pair to the cache. 
If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.

get(key): gets the value at key. If no such key exists, return -1.

Each operation should run in O(1) average time complexity.

"""

class LLNode:
    """
    Linked list node containing the key-element pair
    and references to next and previous nodes in the 
    chain.  
    """
    def __init__(self, k, e) -> None:
        self.k = k
        self.e = e
        self.next = None 
        self.prev = None

    def __repr__(self) -> str:
        return f"({self.k}, {self.e})"


class LRUCache:
    """
    LRU cache implementation with hashmap and doubly linked list.
    Hashmap provides O(1) get operation by mapping each key to the
    node in the list. Doubly linked list provides O(1) put operation
    by using link references to update positions of nodes in cache.

    :param int n: Capacity of cache.
    """
    def __init__(self, n: int) -> None:
        if n <= 0:
            raise ValueError("Cache capacity should be positive.")
        self.capacity = n
        self.hmap = {}
        self.size = 0

        # Doubly-linked list with head/tail sentinel nodes
        # with head pointing to most recently accessed node
        # and tail pointing to least recently accessed node
        self.head = LLNode("H", None)
        self.tail = LLNode("T", None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def __move_to_start(self, node: LLNode) -> None:
        # if node is already at the start, return
        if self.head.next == node:
            return
        # connect the neighbours of the moved node
        node.prev.next = node.next
        node.next.prev = node.prev
        # connect node between head and its neighbour
        tmp = self.head.next
        self.head.next = node 
        tmp.prev = node
        node.prev = self.head 
        node.next = tmp

    
    def __remove_least_used(self) -> None:
        tmp = self.tail.prev 
        tmp.prev.next = self.tail 
        self.tail.prev = tmp.prev
        del(self.hmap[tmp.k])
        del(tmp)
        self.size -= 1


    def put(self, key, value: int) -> None:
        if key in self.hmap:
            raise ValueError("Key already exists.")
        node = LLNode(key, value)
        self.hmap[key] = node
        if self.size == self.capacity:
            # remove the least recently accessed node
            self.__remove_least_used()

        # connect head to node
        tmp = self.head.next
        self.head.next = node
        tmp.prev = node
        self.size += 1

        # connect node to neighbours
        node.prev = self.head
        node.next = tmp
            

    def get(self, key: int) -> int:
        node = self.hmap.get(key)
        if node:
            # move node to beginning of list
            self.__move_to_start(node)
            return node.e
        
        return -1

    
    def traverse(self) -> None:
        start = self.head
        while start.next:
            print(start)
            start = start.next
        else:
            print(self.tail)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.traverse()
cache.get(1)
cache.traverse()

cache.put(3, 3)
cache.traverse()
cache.get(2)
cache.put(4, 4)
cache.traverse()