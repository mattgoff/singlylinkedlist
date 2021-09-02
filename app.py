class SinglyLinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head = None

  def print_list(self):
    current_node = self.head
    temp_list = []
    while current_node:
      temp_list.append(current_node.data)
      current_node = current_node.next
    output = " -> ".join(temp_list)
    print(output)

  def AppendNode(self, data):
    new_node = SinglyLinkedNode(data)
    if self.head is None:
      self.head = new_node
      return
    else:
      last_node = self.head
      while last_node.next:
        last_node = last_node.next

      last_node.next = new_node

  def PrependNode(self, data):
    new_node = SinglyLinkedNode(data)
    new_node.next = self.head
    self.head = new_node

  def InsertNode(self, prev_node, data):
    if not prev_node:
      print("Previous node is not in the list")
      return

    new_node = SinglyLinkedNode(data)

    new_node.next = prev_node.next
    prev_node.next = new_node

  def ReverseIterative(self):
    prev = None
    cur = self.head

    while cur:
      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt

    self.head = prev

  def ReverseRecursive(self):

    def _reverse_recursive(cur, prev):
      if not cur:
        return prev

      nxt = cur.next
      cur.next = prev
      prev = cur
      cur = nxt
      return _reverse_recursive(cur, prev)

    self.head = _reverse_recursive(cur=self.head, prev=None)


llist = SinglyLinkedList()
llist.AppendNode("A")
llist.AppendNode("B")
llist.AppendNode("C")
llist.AppendNode("D")
llist.print_list()
# llist.ReverseIterative()
llist.ReverseRecursive()
llist.print_list()

