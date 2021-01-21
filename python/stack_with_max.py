# Stack with max
# This test creates a stack and populates it with integers, issuing first
# a push (to populate the stack), then gets the max value of the stack, 
# then a pop (to remove the highest value), and again gets the max value of the stack
# It works with the given numbers, and with a while loop

class StackWithMax: 
    def __init__(self): 
          
        # main stack  
        self.mainStack = []  
      
        # tack to keep track of 
        # max element  
        self.trackStack = [] 
  
    def push(self, x): 
        self.mainStack.append(x)  
        if (len(self.mainStack) == 1): 
            self.trackStack.append(x)  
            return
  
        # If current element is greater than  
        # the top element of track stack,  
        # append the current element to track  
        # stack otherwise append the element  
        # at top of track stack again into it.  
        if (x > self.trackStack[-1]):  
            self.trackStack.append(x)  
        else: 
            self.trackStack.append(self.trackStack[-1]) 
  
    def getMax(self): 
        return self.trackStack[-1] 
  
    def pop(self): 
        self.mainStack.pop()  
        self.trackStack.pop() 
  
# Driver Code 
if __name__ == '__main__': 
  
    s = StackWithMax() 
    s.push(20)  
    print(s.mainStack)
    print(s.getMax())  
    s.push(10)  
    print(s.mainStack)
    print(s.getMax())
    s.pop() 
    s.push(50)
    print(s.mainStack)
    print(s.getMax()) 
 
    loop_n = 0
    to_loop = 10
    while ( loop_n <= to_loop):
        s.push(loop_n)
        print(s.mainStack)
        print(s.getMax())
        loop_n = loop_n + 1 
