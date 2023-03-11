class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None
        
    def __init__(self):
        return str(self.Value)
    
class LinkedList:
    def __init__(self):
        self.first = None
        self.size = 0
        
        
    def Append(self,Value):
        MyNode = Node(Value)
        if self.size == 0:
            self.first = MyNode
        else:
            Current = self.first
            while Current.Next != None:
                Current = Current.Next
            Current.Next = MyNode
            
            
        self.size += 1
        
        return MyNode
    
    def Remove(self, Value):
        if self.size == 0:
            return False
        
        else:
            Current = self.first
            while Current.Next.Value != Value:
                if Current.Next == None:
                    return False
                else:
                    Current = Current.Next
                    
            DeletedNode = Current.Next
            Current.Next = DeletedNode.Next 
        
        self.size == 1
        return DeletedNode
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        String = "["
        Current = self.first
        while Current != None:
            String += str(Current)
            String += str(",")
            Current = Current.Next
        String += "]"
        
        return String
    
MyList = LinkedList()

MyList.Append(1)
MyList.Append(2)
MyList.Append(3)
MyList.Append(4)

print(MyList)
        
        