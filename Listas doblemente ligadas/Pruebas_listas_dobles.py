from Listas_dobles import DoubleLinkedList

ld = DoubleLinkedList()
print("Esta vacía?: ", ld.is_empty() )
ld.append(10)
ld.append(20)
ld.append(30)
print(f"La lista tiene{ld.get_size()} elementos")
ld.transversal()
ld.reverse_transversal()
ld.remove_from_head(10)
ld.transversal