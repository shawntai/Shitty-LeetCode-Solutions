def sol(head):
    middle = head
    curr_end = head
    i = 1
    while curr_end.next != None:
        curr_end = curr_end.next
        if i % 2 == 1:
            middle = middle.next
        i += 1
    return middle