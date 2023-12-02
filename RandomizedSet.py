import random


class RandomizedSet:


    def __init__(self):
        self.numMap = {}
        self.current_vals = []    

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        
        self.numMap[val] = len(self.current_vals)
        self.current_vals.append(val)        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx = self.numMap[val]
        lastVal = self.current_vals[-1]
        self.current_vals[idx] = lastVal
        self.current_vals.pop()
        self.numMap[lastVal] = idx
        
        return True

    def getRandom(self) -> int:
        ran = random.choice(self.current_vals)
        return ran