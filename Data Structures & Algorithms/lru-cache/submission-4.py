class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = dict()
        self.copy = []

    def get(self, key: int) -> int:
        if key in self.cache:
            tmp=[]
            for i, c in enumerate(self.copy):
                if c[0] == key:
                    tmp = self.copy.pop(i)
                    self.copy.append(tmp)
                    break
            return tmp[1]
                
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            
            tmp=[]
            for i, c in enumerate(self.copy):
                if c[0] == key:
                    tmp = self.copy.pop(i)
                    break
        
            self.copy.append([tmp[0], value])
        else:
            self.copy.append([key, value])
        
        self.cache[key]=value
        
        if len(self.cache) > self.size:
            self.cache.pop(self.copy[0][0])
            self.copy.pop(0)
        
