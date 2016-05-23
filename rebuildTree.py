from collections import deque

class rebuildTree():
  
  class _Node:
    __slots__='_element','_parent','_left','_right','_currentSize','_rebuildSize'
    def __init__(self, element, parent=None, left=None, right=None, currentSize=0, rebuildSize=0):
      self._element=element
      self._parent=parent
      self._left=left
      self._right=right
      self._currentSize=currentSize
      self._rebuildSize=rebuildSize

  def __init__(self):
    self._root=None
    self._size=0

  def insert(self,x):
    if self._size==0:
      self._root=self._Node(x)
      self._root._currentSize=1
      self._root._rebuildSize=1
      self._size+=1
    else:
      node=self._subtree_search(self._root,x)
      if node._element<x:
        node._right=self._Node(x,node)
        node=node._right
        node._currentSize=1
        node._rebuildSize=1
      else:
        node._left=self._Node(x,node)
        node=node._left
        node._currentSize=1
        node._rebuildSize=1
      node = node._parent
      while node is not None:
        node._currentSize+=1
        node=node._parent
      node=self.findRebuild(self._root,x)
      if node is not None:
        if node._parent==None:
          self._root = node
          node = node._parent
        else:
          if node._element> node._parent._element:
            node._parent._right=node
          else:
            node._parent._left=node
      self._size+=1

  def findRebuild(self,node,x):
      if node._currentSize>=2*node._rebuildSize:
        return self.rebuild(node)
      else:
        if node._element==x:
          return None
        elif node._element>x:
          return self.findRebuild(node._left,x)
        else:
          return self.findRebuild(node._right,x)
      
  def rebuild(self, node):
    L=self.getList(node)
    subTree=self.make_empty_tree(node,node._currentSize)
    L.sort()
    L.reverse()
    subTree = self.fill_in_tree(subTree,L)
    return subTree

  def getList(self,node):
    L=[]
    for i in self._subtree_inorder(node):
      L.append(i._element)
    return L
  
  def make_empty_tree(self,node,size):
    q = deque()
    subTreeRoot=self._Node(None,node._parent)
    q.append(subTreeRoot)
    node_count = 1
    while node_count < size:
      node = q.popleft()
      if node_count+1<=size:
        left=self._Node(None,node)
        node._left=left
        q.append(left)
        node_count += 1
        if node_count+1<=size:
          right=self._Node(None,node)
          node._right=right
          q.append(right)
          node_count += 1
    return subTreeRoot
  
  def fill_in_tree(self,node, L):
    if node: #if I haven't fallen off the tree
      if node._left is None and node._right is None:
        node._element=L.pop()
        node._currentSize=1
        node._rebuildSize=1
        return node
      else:
        node._left = self.fill_in_tree(node._left, L)
        if node._left is not None:
             node._currentSize+=node._left._currentSize
             node._rebuildSize+=node._left._rebuildSize
        node._element=L.pop()
        node._currentSize+=1
        node._rebuildSize+=1
        node._right = self.fill_in_tree(node._right, L)
        if node._right is not None:
             node._currentSize+=node._right._currentSize
             node._rebuildSize+=node._right._rebuildSize
        return node

  def _subtree_inorder(self,node):
    if node._left is not None:
      for other in self._subtree_inorder(node._left):
        yield other
    yield node
    if node._right is not None:
      for other in self._subtree_inorder(node._right):
        yield other

  def _subtree_search(self, node, k):
    if k==node._element:
      return node
    elif k<node._element:
      if node._left is not None:
        return self._subtree_search(node._left,k)
      return node
    else:
      if node._right is not None:
        return self._subtree_search(node._right,k)
      return node

  




