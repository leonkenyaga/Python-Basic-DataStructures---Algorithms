# Binary Search Tree node class
class node:
    def __init__(self,value=None):
        self.value = value
        self.right_child= None
        self.left_child= None

#Binary Search Tree class 
class binary_search_tree:
    def __init__(self):
        self.root= None

    #Insert method (public and non-recursive) enables the addition of elements into the BST
    def insert(self,value):
        #If there is no root node add the the passed element as the value of the root node
        if self.root==None:
            self.root = node(value)
            print("inserted", value)
        else:
            self.__insert(value, self.root)
    # The private version (recursive) of the BST class insert method
    def __insert(self, value, currentNode):
        #Check if the value is less than the value of the currentNode
        if value<currentNode.value:
            #Check if the currentNode has a left child
            if currentNode.left_child == None:
                #if it doesn't insert a node with the parsed value
                currentNode.left_child = node(value)
                print("inserted", value)
            #Otherwise call the __insert method recursively on the left child
            else:
                self.__insert(value, currentNode.left_child)
        #Check if the value is greater than the value of the currentNode
        elif value > currentNode.value:
            #Check if the currentNode has a right child
            if currentNode.right_child == None:
                #if it doesn't insert a node with the parsed value
                currentNode.right_child = node(value)
                print("inserted", value)
            #Otherwise call the __insert method recursively on the right child
            else:
                self.__insert(value, currentNode.right_child)

        else:
            print ("Value already in tree!")
    #Print BST function (public and non-recursive)
    def printtree(self):
        if self.root!=None:
            self.__printtree(self.root)
    #Print BST function (private and recursive)
    def __printtree(self, currentNode):
        if currentNode!=None:
            self.__printtree(currentNode.left_child)
            print ("printing node:  ", currentNode.value)
            self.__printtree(currentNode.right_child)
    def height(self):
       if self.root!=None:
        return self._height(self.root,0)
       else:
        return 0
    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height=self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)
        


def fill_tree(tree, num_elems=10, max_int = 100):
    from random import randint
    for i in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree = fill_tree(tree)
tree.printtree()

print("tree height is: ", tree.height())
            





