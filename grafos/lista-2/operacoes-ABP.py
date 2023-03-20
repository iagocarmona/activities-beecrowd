# Definir a classe do nó da árvore
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

# Definir a classe da árvore
class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.result = []

    # Inserção de um nó na árvore
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._insert(value, current_node.left_child)
        elif value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._insert(value, current_node.right_child)
        else:
            return

    # Busca de um nó na árvore
    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value, current_node):
        if current_node is None:
            return False
        elif current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search(value, current_node.left_child)
        else:
            return self._search(value, current_node.right_child)

    # Traversal da árvore em ordem prefixa (raiz-esquerda-direita)
    def preorder(self):
        self.result = []
        if self.root is not None:
            self._preorder(self.root)

    def _preorder(self, current_node):
        if current_node is not None:
            self.result.append(current_node.value)
            self._preorder(current_node.left_child)
            self._preorder(current_node.right_child)

    # Traversal da árvore em ordem infixa (esquerda-raiz-direita)
    def inorder(self):
        self.result = []
        if self.root is not None:
            self._inorder(self.root)

    def _inorder(self, current_node):
        if current_node is not None:
            self._inorder(current_node.left_child)
            self.result.append(current_node.value)
            self._inorder(current_node.right_child)

    # Traversal da árvore em ordem posfixa (esquerda-direita-raiz)
    def postorder(self):
        self.result = []
        if self.root is not None:
            self._postorder(self.root)

    def _postorder(self, current_node):
        if current_node is not None:
            self._postorder(current_node.left_child)
            self._postorder(current_node.right_child)
            self.result.append(current_node.value)

tree = BinarySearchTree()

while True:
    try:
        str = input()
    except:
        break
    
    arrayStr = str.split()
    length = len(arrayStr)

    func = arrayStr[0] if length > 0 else ""
    value = arrayStr[1] if length == 2 else ""
    
    if func == "I":
        tree.insert(value)
    
    if func == "P":
        exists = tree.search(value)
        if exists:
            print(value, "existe")
        else:
            print(value, "nao existe")
        
    if func == "PREFIXA":
        tree.preorder()
        idx = 0
        for i in tree.result:
            if idx < len(tree.result) - 1:
                print(i, end = ' ')
            else:
                print(i)
            idx = idx + 1
    
    if func == "INFIXA":
        tree.inorder()
        idx = 0
        for i in tree.result:
            if idx < len(tree.result) - 1:
                print(i, end = ' ')
            else:
                print(i)
            idx = idx + 1
        
    if func == "POSFIXA":
        tree.postorder()
        idx = 0
        for i in tree.result:
            if idx < len(tree.result) - 1:
                print(i, end = ' ')
            else:
                print(i)
            idx = idx + 1
    
    arrayStr.clear()
    value = ""
    func = ""

