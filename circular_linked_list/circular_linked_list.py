class Node():
    
    def __init__(self, value):
        
        self.value = value
        
    def pointer(self, next_):
        
        self.next_ = next_
        

n1 = Node(1)
n2 = Node(2)
n3 = Node(10)

n1.pointer(n2)
n2.pointer(n3)
n3.pointer(n1)


def insert(n, val_to_insert):
    
    n_insert = Node(val_to_insert)

    found = 0
    corrected = 0
    
    while not found:

        if val_to_insert < n.value:

            lowest_value_found = 0
            n_next = n
            while not lowest_value_found:
                if n_next.value > n_next.next_.value:
                    lowest_value_found = 1 
                    if val_to_insert < n_next.next_.value:
                        n_insert.next_ = n_next.next_
                        n_next.next_ = n_insert
                        found = 1
                        corrected = 1
                else:
                    n_next = n_next.next_
                    
            n_insert.next_ = n
            found = 1
        elif n.next_.value < n.value:
            n_insert.next_ = n.next_
            n.next_ = n_insert
            corrected = 1
            found = 1
        else:
            n = n.next_
        
    n_next = n.next_
    
    while not corrected:
        
        if n_next.next_ == n:
            n_next.next_ = n_insert
            corrected = 1
        else:
            n_next = n_next.next_
        
    return n_insert


n_new = insert(n1, 3)

to_print = [n1, n2, n3, n_new]

for i in to_print:
    print(i.value, i.next_.value)