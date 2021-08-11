class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
        
    def Insert_Begin(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
    def Insert_End(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def Insert_Index(self,data,index):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            count=1
            while(temp.next!=None and count<index):
                temp=temp.next
                count+=1
            new_node.next=temp.next
            new_node.prev=temp
            temp.next.prev=new_node
            temp.next=new_node
    def Delete_Begin(self):
        if self.head==None:
            print("No element to delete")
        else:
            self.head=self.head.next
    def Delete_End(self):
        if self.head==None:
            print("No element to delete")
        elif(self.head.next==None):
            self.head=None  
            
        else:
            temp=self.head
            while(temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def Delete_Index(self,index):
        if self.head==None:
            print("No element to delete")
        else:
            count=1
            temp=self.head
            while temp.next!=None and count<index:
                count+=1
                temp=temp.next
            temp.next=temp.next.next
                
    
    def Display(self):
        temp=self.head
        if (self.head==None):
            print("NO nodes")
        while(temp!=None):
            print(temp.data,"-->",end=" ")
            temp=temp.next
    def Search(self,data):
        if self.head==None:
            print("NO nodes")
        else:
            temp=self.head
            count=0
            while(temp!=None):
                count+=1
                if(temp.data==data):
                    print(data," found at Position-->",count)
                    return
                temp=temp.next
            print("Element not found")
    

