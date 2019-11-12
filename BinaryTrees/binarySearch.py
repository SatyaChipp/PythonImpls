

data=list(range(0, 20, 3))

target = 15

def binarySearch(data, target): #iterative
    #list to be sorted first
    low = 0
    high = len(data)-1
    while low<=high:
        mid = (low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            high = mid-1
        elif target>data[mid]:
            low = mid+1
    return False
def binarySearchRecursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid= (low+high)//2
        if target == data[mid]:
            return True
        elif target <data[mid]:
            return binarySearchRecursive(data, target, low, mid-1)
        else:
            return binarySearchRecursive(data, target, mid+1, high)
class node:
    def __init__(self, data=None):
        self.data =data
        self.right=None
        self.left=None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if not self.root: #check if root is present else emplty binary search tree
            self.root = node(data)
        else:
            self._insert(data, self.root) #add a helper function
    def _insert(self, data, cur_node):
        if data<cur_node.data:
            if not cur_node.left:
                cur_node.left = node(data)
            else:
                self._insert(data, cur_node.left)
        elif data>cur_node.data:
            if not cur_node.right:
                cur_node.right = node(data)
            else:
                self._insert(data,cur_node.right)
        else:
            print("Duplicate element")

    def find(self, data):
        if not self.root:
            return None
        else:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False

    def _find(self, data, cur_node):
        if data==cur_node.data:
            return True
        elif data>cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data<cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder': ##root-left-right
            return self.preOrderTraversal(self.root, "")
        if traversal_type == 'inorder':
            return self.inOrderTraversal(self.root, "")
        if traversal_type == 'postorder':
            return self.postOrderTraversal(self.root, "")

    def preOrderTraversal(self, start, traversal):
        if start:
            traversal += (str(start.data) + '-') #start with root
            traversal = self.preOrderTraversal(start.left, traversal)
            traversal = self.preOrderTraversal(start.right, traversal)
        return traversal

    def inOrderTraversal(self, start, traversal):
        if start:##left root right
            traversal = self.inOrderTraversal(start.left, traversal)
            traversal += (str(start.data) + '-')
            traversal = self.inOrderTraversal(start.right, traversal)
        return traversal

    def postOrderTraversal(self, start, traversal):
        if start: #right root left
            traversal = self.postOrderTraversal(start.right, traversal)
            traversal += (str(start.data) + '-')
            traversal = self.postOrderTraversal(start.left, traversal)
        return traversal

if __name__ == '__main__':
    print(data)
    print(binarySearch(data, 25))
    print(binarySearchRecursive(data, 25, 0, len(data)-1))
    bst = BST()
    bst.insert(23)
    bst.insert(34)
    bst.insert(67)
    bst.insert(90)
    bst.insert(6758)
    from subprocess import call
    # call('pip install bs4')
    # import bs4
    # from bs4 import BeautifulSoup
    # import requests
    # page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
    # soup = BeautifulSoup(page.content, 'html.parser')
    # soup.find_all('p')[0].get_text()
    # print(soup.prettify())
    # html = list(soup.children)[2]
    # print(html.children)
    print(bst.find(34))
    print(bst.print_tree('preorder'))
    print(bst.print_tree('inorder'))
    print(bst.print_tree('postorder'))


