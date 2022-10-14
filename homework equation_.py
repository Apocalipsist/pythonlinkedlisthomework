def remove(self,value_to_remove):
    check = self.head
    while check is not None:
        nxt_node = check.node.next
        if check.value == value_to_remove:
            nxt_node = check.next
            check.next = check.node.next
        check.next = check.next
        return
