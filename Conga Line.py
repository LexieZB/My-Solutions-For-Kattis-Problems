class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None
        self.partner = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def add_tail_node(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.pre = self.tail
        self.tail = new_node

    def save_partner(self):
        temp = self.head.next
        while temp:
            temp.partner = temp.next
            temp.next.partner = temp
            temp = temp.next.next

    def insert_node(self, pre_node, value):
        new_node = Node(value)
        new_node.next = pre_node.next
        pre_node.next = new_node
        new_node.pre = pre_node
        pre_node.next.pre = new_node

    def delete_node(self, aim):
        aim.pre.next = aim.next
        aim.next.pre = aim.pre

    def move_node_to_tail(self, aim_node):
        old_pre = aim_node.pre
        old_pre.next = aim_node.next
        old_next = aim_node.next
        old_next.pre = aim_node.pre

        aim_node.pre = self.tail
        self.tail.next = aim_node
        aim_node.next = None
        self.tail = aim_node

    def move_node_to_partner(self, aim_node):
        old_pre = aim_node.pre
        old_pre.next = aim_node.next
        old_next = aim_node.next
        old_next.pre = aim_node.pre

        partner_pos = aim_node.partner
        if partner_pos.value == self.tail.value:  # 试试不加value
            self.move_node_to_tail(aim_node)
        else:
            partner_pos.next.pre = aim_node
            aim_node.next = partner_pos.next
            partner_pos.next = aim_node
            aim_node.pre = partner_pos

    def print_ll(self):
        temp = self.head.next
        while temp:
            print(temp.value)
            temp = temp.next

    def search_ll(self, aim):
        temp = self.head.next
        while temp:
            if temp.value == aim:
                return temp
            temp = temp.next

NQ = list(map(int, input().split()))
N = NQ[0]
Q = NQ[1]
couple = {}
name_list = []
for i in range(N):
    temp = input().split()
    # print(temp)
    couple[temp[0]] = temp[1]
    couple[temp[1]] = temp[0]
    name_list.append(temp[0])
    name_list.append(temp[1])
LL = LinkedList()

for i in name_list:
    LL.add_tail_node(i)
LL.save_partner()
mic = LL.head.next
order_list = list(input())

for i in order_list:
    if i == 'F':
        mic = mic.pre
    elif i == 'B':
        mic = mic.next

    elif i == 'R':

        if mic.next == None:
            mic = LL.head.next
        else:

            temp = mic.pre
            LL.move_node_to_tail(mic)
            mic = temp.next


    elif i == 'C':
        # print(' ')
        if mic.next == None:
            mic = LL.head.next
        elif mic.partner==mic.pre:
            mic = mic.next
        else:
            temp = mic.pre
            LL.move_node_to_partner(mic)
            mic = temp.next

    elif i == 'P':
        print(mic.partner.value)
print(' ')
LL.print_ll()
