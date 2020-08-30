class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self 
    
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

#No puedo hacer iter(counter) porque es un objeto el counter
c = counter(0,10)
# iter(c)

for n in Counter(50,55):
    print(n)