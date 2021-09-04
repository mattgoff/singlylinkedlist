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

  def DeleteNode(self, key):
    cur_node = self.head

    if cur_node and cur_node.data == key:
      self.head = cur_node.next
      cur_node = None
      return

    prev_node = None
    while cur_node and cur_node.data != key:
      prev_node = cur_node
      cur_node = cur_node.next

    if cur_node is None:
      return

    prev_node.next = cur_node.next
    cur_node = None

  def DeleteNodeAtPosition(self, pos):
    cur_node = self.head
    if pos == 0:
      self.head = cur_node.next
      cur_node = None
      return

    prev_node = None
    count = 1
    while cur_node and count != pos:
      prev = cur_node
      cur_node = cur_node.next
      count += 1

    if cur_node is None:
      return

    prev_node = cur_node.next
    cur_node = None

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

  def GetLengthIterative(self):
    cur_node = self.head
    count = 0

    while cur_node:
      count += 1
      cur_node = cur_node.next

    return count

  def GetLengthRecursive(self, node):
    if node is None: return 0
    return 1 + self.GetLengthRecursive(node.next)

llist = SinglyLinkedList()
llist.AppendNode("A")
llist.AppendNode("B")
llist.AppendNode("C")
llist.AppendNode("D")
llist.print_list()
# llist.ReverseIterative()
# llist.ReverseRecursive()
llist.DeleteNode("C")
llist.print_list()
print("Itterative Length of list: {}".format(llist.GetLengthIterative()))
print("Recursive Length of list: {}".format(llist.GetLengthRecursive(llist.head)))
