class ListNode:
    def __init__(self, data):
        
        self.data = data
        self.next = None
        self.previous = None
        return
    
    def has_value(self, value):
        
        if self.data == value:
            return True
        else:
            return False
