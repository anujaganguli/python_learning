def enqueue(element, this_queue):
    this_queue.append(element)

def is_empty(this_queue):
    if this_queue == []:
        return True
    else:
        return False

def is_full(this_queue):
    return (len(this_queue) == 5)
    
def dequeue(this_queue):
    if is_empty(this_queue):
        return "The list is empty."
    else:
        first_element = this_queue[0]
        del this_queue[0]
        return first_element
    
counter1_q = []
counter2_q = []
counter3_q = []
standby_q = []

i = 0

while (i < 30):
    if not is_full(counter1_q):
        enqueue('Person ' + str(i), counter1_q)
    elif not is_full(counter2_q):
        enqueue('Person ' + str(i), counter2_q)
    elif not is_full(counter3_q):
        enqueue('Person ' + str(i), counter3_q)
    else:
        enqueue('Person ' + str(i), standby_q)
    
    i+=1

print(counter1_q)
print(counter2_q)
print(counter3_q)
print(standby_q)

