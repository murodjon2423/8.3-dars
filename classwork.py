class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def count_elements(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def search(self, key):
        indices = []
        count = 0
        current = self.head
        while current:
            if current.data == key:
                indices.append(count)
            count += 1
            current = current.next
        return indices

    def remove_zeros(self):
        while self.head and self.head.data == 0:
            self.head = self.head.next
        current = self.head
        while current and current.next:
            if current.next.data == 0:
                current.next = current.next.next
            else:
                current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_tuple(self):
        return tuple(self.to_list())

    def swap_adjacent_values(self):
        current = self.head
        while current and current.next:
            current.data, current.next.data = current.next.data, current.data
            current = current.next.next if current.next.next else None

# Masalaning dastlabki qismi
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(0)
linked_list.append(4)
linked_list.append(0)
linked_list.append(5)

# Metodlarni sinov uchun
print("Elementlar soni:", linked_list.count_elements())
print("0 qiymatini o'chirishdan keyin:", linked_list.to_list())
print("Mavjud bo'lsa necha marta va qaysi indekslarda uchrashini aniqlash:", linked_list.search(5))
linked_list.remove_zeros()
print("Qiymati nolga teng tugunlar o'chirilgandan keyin:", linked_list.to_list())
print("Linked listdan tuple:", linked_list.to_tuple())

# Yonma-yon tugunlarni almashtirish
print("Yonma-yon tugunlarni almashtirishdan keyin:", linked_list.to_list())
linked_list.swap_adjacent_values()
print("Yonma-yon tugunlarni almashtirishdan so'ng:", linked_list.to_list())
