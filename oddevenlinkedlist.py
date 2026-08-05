class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head

def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def main():
    # input format: e.g. "list : 1 2 3 4 5"
    parts = input().split()
    values = list(map(int, parts))  # skip "list" or "list:"
    head = build_linked_list(values)
    new_head = oddEvenList(head)
    print(to_list(new_head))

if __name__ == "__main__":
    main()
