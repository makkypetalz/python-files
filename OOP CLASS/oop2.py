class Cars:
    def __init__(self,colour,wheel):
        self.colour=colour
        self.wheel=wheel
        
    def proper(self):
        return f"The car has a {self.colour} painting and has {self.wheel} tyres"
        
p1=Cars("red",4)
print(p1.proper())
p2=Cars("blue",6)
print(p2.proper()) 


        