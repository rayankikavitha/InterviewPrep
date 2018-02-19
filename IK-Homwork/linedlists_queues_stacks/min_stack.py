"""
Implement additional method called getMin() for the stack.
At any point of time, it should return minimum
if the stack has[1,2,3,5] , output = 1
if the stack has [1,5,3,0], output = 0

Option1: maintaining a second stack with the mins seen so far
Option2 : not using additional stack, using the same stack for storing mins

"""
class minstack:
    def __init__(self):
        self.s =[]
        self.mins=[]
    def push(self,val):
        self.s.append(val)
        if len(self.mins) > 0:
            if self.mins[len(self.mins)-1] > val:
                self.mins.append(val)
        else:
            self.mins.append(val)
    def pop(self):
        top = self.s.pop()
        if len(self.mins) > 0:
            if top == self.mins[len(self.mins)-1]:
                self.mins.pop()
    def getmin(self):
        return self.mins[len(self.mins)-1]

# driver program to test
input = [5,7,3,2,1,9]
st = minstack()
for each in input:
    st.push(each)
print st.s
print st.mins
print st.getmin()
st.pop()
st.pop()
print st.getmin()

