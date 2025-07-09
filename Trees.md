I can provide the Python code solutions for the problems you listed,
along with explanations of their time and space complexity. However, I
cannot directly generate a PDF file. You would need to copy and paste
the provided content into a document editor (like Google Docs, Microsoft
Word, or a LaTeX editor) and then save or print it as a PDF.

Here's how I'll structure the response for each problem: 1. **Problem**
**Title**

> 2\. **Problem** **Description** **(Brief)** 3. **Conceptual**
> **Approach**
>
> 4\. **Python** **Code** **Solution**
>
> 5\. **Time** **Complexity** **Analysis** 6. **Space** **Complexity**
> **Analysis**

Let's start with the first problem:

**Test** **if** **a** **binary** **tree** **is** **height-balanced**

**Problem** **Description:** A binary tree is height-balanced if for
every node, the heights of its two subtrees differ by at most one.

**Conceptual** **Approach:** We can perform a post-order traversal (or a
variation of it). For each node, we recursively calculate the height of
its left and right subtrees. If at any point the absolute difference
between the heights of the left and right subtrees is greater than 1,
the tree is not balanced. We also need to propagate the height of the
current subtree upwards. A special value (e.g., -1) can be used to
signal an unbalanced subtree.

**Python** **Code** **Solution:** class TreeNode:

> def \_\_init\_\_(self, val=0, left=None, right=None): self.val = val
>
> self.left = left self.right = right

def is_balanced(root):

> def check_balance_and_height(node): if not node:
>
> return True, -1 \# (is_balanced, height)

left_balanced, left_height = check_balance_and_height(node.left)

> if not left_balanced: return False, 0

right_balanced, right_height = check_balance_and_height(node.right)

> if not right_balanced: return False, 0
>
> current_balanced = abs(left_height - right_height) \<= 1
> current_height = 1 + max(left_height, right_height)

return current_balanced and left_balanced and right_balanced,
current_height

> balanced, \_ = check_balance_and_height(root) return balanced

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited exactly once to calculate
its height and check balance.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity O(log N).

**Test** **if** **a** **binary** **tree** **is** **symmetric**

**Problem** **Description:** A binary tree is symmetric if the left and
right subtrees are mirror images of each other.

**Conceptual** **Approach:** We can define a helper function that takes
two nodes, say node1 and node2. For the tree to be symmetric, node1.val
must be equal to node2.val, and the left child of node1 must be a mirror
of the right child of node2, and the right child of node1 must be a
mirror of the left child of node2. This can be implemented using
recursion.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problem

def is_symmetric(root): if not root:

> return True
>
> def is_mirror(node1, node2): if not node1 and not node2:
>
> return True
>
> if not node1 or not node2 or node1.val != node2.val: return False

return is_mirror(node1.left, node2.right) and is_mirror(node1.right,
node2.left)

> return is_mirror(root.left, root.right)

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each pair of nodes that are compared (which
effectively covers all nodes once) contributes a constant amount of
work.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity

O(log N).

**Compute** **the** **lowest** **common** **ancestor** **in** **a**
**binary** **tree**

**Problem** **Description:** Given a binary tree and two nodes, p and q,
find their lowest common ancestor (LCA). The LCA of two nodes p and q is
the lowest node in T that has both p and q as descendants (where we
allow a node to be a descendant of itself).

**Conceptual** **Approach:** We can use a recursive approach. A function
can traverse the tree. 1. If the current node is None, return None.

> 2\. If the current node is p or q, then this node is a potential LCA.
> 3. Recursively search for p and q in the left subtree.
>
> 4\. Recursively search for p and q in the right subtree. 5. Based on
> the results from left and right searches:
>
> ○ If both left and right searches return non-None nodes, it means p is
> in one subtree and q is in the other. Therefore, the current node is
> the LCA.
>
> ○ If only the left search returns a non-None node, it means both p and
> q (or one of them if the current node itself is one) are in the left
> subtree. So, the result from the left search is the LCA.
>
> ○ If only the right search returns a non-None node, similarly, the
> result from the right search is the LCA.
>
> ○ If neither returns a non-None node, then neither p nor q are
> descendants of the current node.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problem

def lowest_common_ancestor(root, p, q): if not root or root == p or root
== q:

> return root
>
> left_lca = lowest_common_ancestor(root.left, p, q) right_lca =
> lowest_common_ancestor(root.right, p, q)
>
> if left_lca and right_lca:
>
> return root \# p in one subtree, q in another elif left_lca:

return left_lca \# Both p and q (or one if root is one) are in left
subtree

> else:

return right_lca \# Both p and q (or one if root is one) are in right
subtree (or not found)

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. In the worst case, we might visit all nodes.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity

O(log N).

**Compute** **the** **LCA** **when** **nodes** **have** **parent**
**pointers**

**Problem** **Description:** Given a binary tree where each node has a
parent pointer, and two nodes p and q, find their lowest common ancestor
(LCA).

**Conceptual** **Approach:**

> 1\. **Method** **1:** **Using** **Heights/Depths**
>
> ○ Calculate the depth (or height) of both p and q from the root.
>
> ○ Move the deeper node up by the difference in depths until both nodes
> are at the same depth.
>
> ○ Then, move both nodes up simultaneously, one step at a time, using
> their parent pointers until they meet. The node where they meet is the
> LCA.
>
> 2\. **Method** **2:** **Using** **Set** **(or** **visited**
> **pointers)**
>
> ○ Traverse up from p to the root, adding all ancestors of p to a set.
>
> ○ Traverse up from q to the root. The first ancestor of q that is
> present in the set of p's ancestors is the LCA.

**Python** **Code** **Solution** **(Method** **1** **-** **More**
**space-efficient):** class TreeNodeWithParent:

> def \_\_init\_\_(self, val=0, left=None, right=None, parent=None):
> self.val = val
>
> self.left = left self.right = right self.parent = parent

def get_depth(node): depth = 0

> while node.parent: node = node.parent depth += 1
>
> return depth

def lowest_common_ancestor_with_parent(p, q): depth_p = get_depth(p)

> depth_q = get_depth(q)
>
> \# Move deeper node up while depth_p \> depth_q:
>
> p = p.parent depth_p -= 1
>
> while depth_q \> depth_p: q = q.parent depth_q -= 1
>
> \# Move both nodes up simultaneously until they meet while p != q:
>
> p = p.parent
>
> q = q.parent return p

**Time** **Complexity** **Analysis:** O(H), where H is the height of the
binary tree. In the worst case (skewed tree), H can be N. We traverse up
from p and q to the root at most twice.

**Space** **Complexity** **Analysis:** O(1). We only use a few variables
to store depths and current nodes.

**Sum** **the** **root-to-leaf** **paths** **in** **a** **binary**
**tree**

**Problem** **Description:** Given a binary tree where each node
contains a digit from 0-9, each root-to-leaf path represents a number.
Return the total sum of all such numbers.

**Conceptual** **Approach:** We can perform a depth-first search (DFS)
traversal. As we traverse down, we build the current number represented
by the path from the root to the current node. When we reach a leaf
node, we add the formed number to a global sum (or pass it up the
recursion stack).

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def sum_numbers(root): total_sum = 0

> def dfs(node, current_number): nonlocal total_sum
>
> if not node: return
>
> current_number = current_number \* 10 + node.val
>
> if not node.left and not node.right: \# Leaf node total_sum +=
> current_number
>
> return
>
> dfs(node.left, current_number) dfs(node.right, current_number)
>
> dfs(root, 0) return total_sum

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited exactly once.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity

O(log N).

**Find** **a** **root** **to** **leaf** **path** **with** **specified**
**sum**

**Problem** **Description:** Given a binary tree and a target sum,
determine if the tree has a

root-to-leaf path such that adding up all the values along the path
equals the given target sum. **Conceptual** **Approach:** This can be
solved with a recursive DFS. For each node, subtract its value from the
target_sum. If the current node is a leaf and the remaining target_sum
is 0, then a valid path is found. Otherwise, recursively call for left
and right children with the updated target_sum.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def has_path_sum(root, target_sum): if not root:

> return False
>
> \# If it's a leaf node and the remaining sum is 0, we found a path if
> not root.left and not root.right:
>
> return target_sum == root.val
>
> \# Recursively check left and right subtrees remaining_sum =
> target_sum - root.val
>
> return has_path_sum(root.left, remaining_sum) or \\
> has_path_sum(root.right, remaining_sum)

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. In the worst case, we might visit all nodes.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity O(log N).

**Implement** **an** **inorder** **traversal** **without** **recursion**

**Problem** **Description:** Traverse a binary tree in inorder (left,
root, right) without using recursion. **Conceptual** **Approach:** We
can use an iterative approach with a stack.

> 1\. Initialize an empty stack. 2. Start from the root.
>
> 3\. While the current node is not None or the stack is not empty:
>
> ○ Keep pushing the current node onto the stack and move to its left
> child until the current node becomes None. This pushes all left
> descendants onto the stack.
>
> ○ Pop a node from the stack. This is the next node in inorder
> sequence. Process it (e.g., print its value).

○ Move to the right child of the popped node. **Python** **Code**
**Solution:**

\# Assuming TreeNode class from previous problems

def inorder_traversal_iterative(root): result = \[\]

> stack = \[\] current = root
>
> while current or stack:
>
> \# Reach the leftmost node of the current subtree while current:
>
> stack.append(current) current = current.left

\# Current must be None at this point, meaning we've gone as left as
possible

> current = stack.pop() result.append(current.val)
>
> \# Now go to the right subtree current = current.right
>
> return result

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is pushed onto and popped from the
stack exactly once.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. In the worst case (skewed tree), the stack might store
all N nodes, making the space complexity O(N). In the best case
(balanced tree), the stack stores log N nodes, making the space
complexity O(log N).

**Implement** **a** **preorder** **traversal** **without** **recursion**

**Problem** **Description:** Traverse a binary tree in preorder (root,
left, right) without using recursion.

**Conceptual** **Approach:** We can use an iterative approach with a
stack. 1. Initialize an empty stack and add the root to it (if not
None).

> 2\. Initialize an empty list for the result. 3. While the stack is not
> empty:
>
> ○ Pop a node from the stack.
>
> ○ Process the popped node (e.g., add its value to the result). ○ Push
> its right child onto the stack (if not None).
>
> ○ Push its left child onto the stack (if not None). The left child is
> pushed last so it's processed first (LIFO order).

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def preorder_traversal_iterative(root): result = \[\]

> if not root: return result
>
> stack = \[root\]
>
> while stack:
>
> node = stack.pop() result.append(node.val)
>
> \# Push right child first, then left, so left is processed next if
> node.right:
>
> stack.append(node.right) if node.left:
>
> stack.append(node.left) return result

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is pushed onto and popped from the
stack exactly once.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. In the worst case (skewed tree), the stack might store
all N nodes, making the space complexity O(N). In the best case
(balanced tree), the stack stores log N nodes, making the space
complexity O(log N).

**Compute** **the** **kth** **node** **in** **an** **inorder**
**traversal**

**Problem** **Description:** Given a binary tree and an integer k, find
the value of the k-th node in an inorder traversal (1-indexed).

**Conceptual** **Approach:** We can perform an inorder traversal (either
recursively or iteratively) and keep a counter. When the counter reaches
k, we return the value of the current node. **Python** **Code**
**Solution** **(Iterative** **Inorder):**

\# Assuming TreeNode class from previous problems

def kth_node_inorder(root, k): count = 0

> stack = \[\] current = root
>
> while current or stack: while current:
>
> stack.append(current) current = current.left
>
> current = stack.pop() count += 1
>
> if count == k:
>
> return current.val
>
> current = current.right return None \# k is out of bounds

**Time** **Complexity** **Analysis:** O(k) in the best case (if the k-th
node is near the beginning of the inorder traversal), and O(N) in the
worst case (if k is close to N, or k is out of bounds), where N is the
total number of nodes.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. In the worst case (skewed tree), the stack might store
up to N nodes, making the space complexity O(N). In the best case
(balanced tree), the stack stores log N nodes, making the space
complexity O(log N).

**Compute** **the** **successor**

**Problem** **Description:** Given a node in a binary tree, find its
inorder successor. Assume each node has a parent pointer.

**Conceptual** **Approach:**

> 1\. **If** **the** **node** **has** **a** **right** **child:** The
> successor is the leftmost node in its right subtree. 2. **If** **the**
> **node** **does** **not** **have** **a** **right** **child:** We need
> to go up the parent pointers. The
>
> successor is the first ancestor for which the current node is in its
> left subtree. If no such ancestor exists (i.e., we reach the root and
> the node was in the rightmost path), then there is no successor.

**Python** **Code** **Solution:**

\# Assuming TreeNodeWithParent class from previous problems

def inorder_successor(node): if node.right:

> \# Case 1: Node has a right child current = node.right
>
> while current.left: current = current.left
>
> return current else:
>
> \# Case 2: Node does not have a right child current = node
>
> parent = node.parent
>
> while parent and parent.right == current: current = parent
>
> parent = parent.parent

return parent \# This will be None if current was the rightmost node of
the tree

**Time** **Complexity** **Analysis:** O(H), where H is the height of the
binary tree. In the worst case, we might traverse up to the root or down
to a leaf.

**Space** **Complexity** **Analysis:** O(1), as we only use a few
pointers.

**Implement** **an** **inorder** **traversal** **with** **O(1)**
**space** **(Morris**

**Traversal)**

**Problem** **Description:** Traverse a binary tree in inorder (left,
root, right) using O(1) extra space. This typically involves modifying
the tree structure temporarily.

**Conceptual** **Approach** **(Morris** **Traversal):** The key idea is
to establish temporary links to avoid using a stack.

> 1\. Initialize current to the root. 2. While current is not None:
>
> ○ **If** **current** **has** **no** **left** **child:**
>
> ■ Process current (add to result). ■ Move current to its right child.
>
> ○ **If** **current** **has** **a** **left** **child:**
>
> ■ Find the rightmost node in current's left subtree (let's call it
> predecessor). ■ **If** **predecessor.right** **is** **None**
> **(first** **visit):**
>
> ■ Set predecessor.right = current (create a temporary link). ■ Move
> current to current.left.
>
> ■ **If** **predecessor.right** **is** **current** **(second**
> **visit):**
>
> ■ Set predecessor.right = None (remove the temporary link). ■ Process
> current (add to result).

■ Move current to current.right. **Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def inorder_traversal_morris(root): result = \[\]

> current = root
>
> while current:
>
> if current.left is None: result.append(current.val) current =
> current.right
>
> else:
>
> \# Find the inorder predecessor of current predecessor = current.left

while predecessor.right is not None and predecessor.right != current:

> predecessor = predecessor.right
>
> if predecessor.right is None:

\# First time visiting current's left subtree, establish link

> predecessor.right = current current = current.left
>
> else:

\# Second time visiting current's left subtree (link already exists)

> \# This means we have processed the left subtree
>
> predecessor.right = None \# Remove the temporary link
> result.append(current.val)
>
> current = current.right return result

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each edge is traversed at most twice (once
going down to find the predecessor, once going up). **Space**
**Complexity** **Analysis:** O(1). It uses no extra space apart from a
few pointers.

**Reconstruct** **a** **binary** **tree** **from** **traversal**
**data**

**Problem** **Description:** Given the preorder and inorder traversal
sequences of a binary tree, reconstruct the tree. Assume no duplicate
values exist in the tree.

**Conceptual** **Approach:** The key properties are:

> ● Preorder traversal: \[Root, Left_Subtree_Preorder,
> Right_Subtree_Preorder\] ● Inorder traversal: \[Left_Subtree_Inorder,
> Root, Right_Subtree_Inorder\]

\<!-- end list --\>

> 1\. The first element of the preorder traversal is always the root of
> the current subtree. 2. Find this root in the inorder traversal. This
> splits the inorder array into two parts: left
>
> subtree elements and right subtree elements.
>
> 3\. The number of elements in the left subtree of the inorder
> traversal determines the number of elements in the left subtree of the
> preorder traversal. The same applies to the right subtree.
>
> 4\. Recursively build the left and right subtrees using the
> corresponding portions of the preorder and inorder arrays.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def build_tree_from_traversals(preorder, inorder): if not preorder or
not inorder:

> return None
>
> \# The first element in preorder is the root root_val = preorder\[0\]
>
> root = TreeNode(root_val)

\# Find the root_val in inorder traversal to split left and right
subtrees

> root_idx_in_inorder = inorder.index(root_val)
>
> \# Recursively build left subtree
>
> \# Preorder for left: preorder\[1 : 1 + length of left_inorder\] \#
> Inorder for left: inorder\[0 : root_idx_in_inorder\] root.left =
> build_tree_from_traversals(
>
> preorder\[1 : 1 + root_idx_in_inorder\], inorder\[0 :
> root_idx_in_inorder\]
>
> )
>
> \# Recursively build right subtree
>
> \# Preorder for right: preorder\[1 + length of left_inorder : \] \#
> Inorder for right: inorder\[root_idx_in_inorder + 1 : \] root.right =
> build_tree_from_traversals(
>
> preorder\[1 + root_idx_in_inorder : \], inorder\[root_idx_in_inorder +
> 1 : \]
>
> )
>
> return root

**Time** **Complexity** **Analysis:** O(N^2) in the worst case. The
inorder.index() operation takes O(N) time in the worst case (if the root
is at the end). This operation is performed for each node. If we use a
hash map to store the indices of elements in the inorder traversal, we
can reduce index() lookup to \$O(1)\`, bringing the total time
complexity to O(N).

**Space** **Complexity** **Analysis:** O(N) for storing the sub-arrays
(if slicing is used, which creates copies) or O(H) for the recursion
stack if indices are passed instead of slicing. If a hash map is used
for inorder indices, it would be O(N) for the map.

*Optimized* *with* *Hash* *Map:*

\# Assuming TreeNode class from previous problems

def build_tree_from_traversals_optimized(preorder, inorder): inorder_map
= {val: idx for idx, val in enumerate(inorder)} preorder_idx = 0

> def build_subtree(inorder_start, inorder_end): nonlocal preorder_idx
>
> if inorder_start \> inorder_end: return None
>
> root_val = preorder\[preorder_idx\] root = TreeNode(root_val)
> preorder_idx += 1
>
> root_idx_in_inorder = inorder_map\[root_val\]

root.left = build_subtree(inorder_start, root_idx_in_inorder -1)

root.right = build_subtree(root_idx_in_inorder + 1, inorder_end)

> return root
>
> return build_subtree(0, len(inorder) - 1)

**Time** **Complexity** **Analysis** **(Optimized):** O(N). Building the
hash map takes O(N). Each node is processed once, and lookups in the
hash map are O(1).

**Space** **Complexity** **Analysis** **(Optimized):** O(N) for the hash
map and O(H) for the recursion stack, where H is the height of the tree.
In the worst case, H can be N, so overall O(N).

**Reconstruct** **a** **binary** **tree** **from** **a** **preorder**
**traversal** **with** **markers**

**Problem** **Description:** Given a preorder traversal of a binary tree
where None (or a special marker like \#) indicates a null child,
reconstruct the tree.

**Conceptual** **Approach:** This is straightforward with a recursive
approach. We iterate through the preorder sequence.

> 1\. If the current element is the marker, return None.
>
> 2\. Otherwise, create a node with the current element's value.
>
> 3\. Recursively build its left child using the next element in the
> sequence.

4\. Recursively build its right child using the next element after the
left child's subtree is built. **Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def build_tree_from_preorder_with_markers(preorder_with_markers): \# Use
a mutable object like a list to simulate a global index \# or pass it as
an argument and return (index, node) tuple index = \[0\]

> def build_node():
>
> if index\[0\] \>= len(preorder_with_markers): return None
>
> val = preorder_with_markers\[index\[0\]\] index\[0\] += 1
>
> if val == '#': \# Assuming '#' is the marker for None return None
>
> node = TreeNode(val) node.left = build_node() node.right =
> build_node() return node
>
> return build_node()

**Time** **Complexity** **Analysis:** O(N), where N is the number of
elements in the preorder_with_markers list (including markers). Each
element is visited exactly once.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space

complexity O(N).

**Form** **a** **linked** **list** **from** **the** **leaves** **of**
**a** **binary** **tree.**

**Problem** **Description:** Given a binary tree, collect all leaf nodes
from left to right and form a singly linked list.

**Conceptual** **Approach:** We can perform any traversal (DFS or BFS)
that visits nodes in a left-to-right manner. When a leaf node is
encountered, we append it to our linked list. A DFS (preorder or
inorder) is naturally suited to maintain the left-to-right order of
leaves.

**Python** **Code** **Solution:** class ListNode:

> def \_\_init\_\_(self, val=0, next=None): self.val = val
>
> self.next = next

\# Assuming TreeNode class from previous problems

def form_leaf_linked_list(root): dummy_head = ListNode(0)
current_ll_node = dummy_head

> def dfs(node):
>
> nonlocal current_ll_node if not node:
>
> return
>
> if not node.left and not node.right: \# Leaf node current_ll_node.next
> = ListNode(node.val) current_ll_node = current_ll_node.next return
>
> dfs(node.left) dfs(node.right)
>
> dfs(root)
>
> return dummy_head.next

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited exactly once during the
DFS.

**Space** **Complexity** **Analysis:** O(H) for the recursion stack
(where H is the height of the tree) and O(L) for the linked list where L
is the number of leaf nodes. In the worst case, H can be N, and L can be
N/2 (for a balanced tree, roughly), so O(N) overall.

**Compute** **the** **exterior** **of** **a** **binary** **tree**

**Problem** **Description:** Compute the exterior of a binary tree,
which is defined as the union of

the left boundary, leaves, and right boundary, in counterclockwise
order. Duplicate nodes should be included only once. The left boundary
nodes are all nodes on the path from the root to the leftmost leaf,
excluding the leftmost leaf itself. The right boundary nodes are all
nodes on the path from the root to the rightmost leaf, excluding the
rightmost leaf itself.

**Conceptual** **Approach:** We can break this into three parts:

> 1\. **Left** **Boundary:** Traverse from the root down its left
> children. Add nodes to the result list. Stop if you encounter a node
> that is also a leaf (it will be covered by the leaves part). If a node
> has a left child, always go left. If not, but has a right child, go
> right.
>
> 2\. **Leaves:** Perform an inorder or DFS traversal to collect all
> leaf nodes.
>
> 3\. **Right** **Boundary:** Traverse from the root down its right
> children. Add nodes to a temporary list (or stack) and then reverse it
> before adding to the final result, to maintain counterclockwise order.
> Stop if you encounter a node that is also a leaf. If a node has a
> right child, always go right. If not, but has a left child, go left.

Handle the root carefully: it's part of both boundaries and can be a
leaf. It should only be added once.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def compute_exterior(root): result = \[\]

> if not root: return result
>
> result.append(root.val) \# Add root
>
> \# Add left boundary (excluding root and actual leaf) curr = root.left
>
> while curr:
>
> if curr.left or curr.right: \# Not a leaf result.append(curr.val)
>
> else: \# It's a leaf, will be covered by leaf traversal break
>
> if curr.left:
>
> curr = curr.left else:
>
> curr = curr.right
>
> \# Add leaves (left to right) def add_leaves(node):
>
> if not node: return
>
> if not node.left and not node.right: result.append(node.val)
>
> return add_leaves(node.left) add_leaves(node.right)
>
> add_leaves(root)

\# Add right boundary (excluding root and actual leaf), in reverse order

> right_boundary_nodes = \[\] curr = root.right
>
> while curr:
>
> if curr.left or curr.right: \# Not a leaf
> right_boundary_nodes.append(curr.val)
>
> else: \# It's a leaf break
>
> if curr.right:
>
> curr = curr.right else:
>
> curr = curr.left
>
> for val in reversed(right_boundary_nodes): result.append(val)
>
> \# Special handling if root itself is a leaf (and only node) if not
> root.left and not root.right and len(result) \> 1:

\# If root is a leaf, it's added as part of leaves, remove initial
duplicate

> result = \[root.val\]
>
> return result

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited at most a constant number
of times (once for left boundary, once for leaves, once for right
boundary).

**Space** **Complexity** **Analysis:** O(H) for the recursion stack
during leaf traversal and O(N) in the worst case for storing the result
and right_boundary_nodes list.

**Compute** **the** **right** **sibling** **tree**

**Problem** **Description:** Given a binary tree, populate its right
field (which typically points to the right child) to point to its right
sibling. Nodes are assumed to have an additional next_right pointer.

**Conceptual** **Approach:** This problem is equivalent to performing a
level-order (BFS) traversal. For each level, iterate through the nodes.
For each node, its next_right should point to the next node in the same
level. The last node in a level will have its next_right set to None.

**Python** **Code** **Solution:**

class NodeWithNextRight:

> def \_\_init\_\_(self, val=0, left=None, right=None, next_right=None):
> self.val = val
>
> self.left = left self.right = right
>
> self.next_right = next_right

def connect_right_siblings(root): if not root:

> return root
>
> \# Use a queue for Level Order Traversal (BFS) queue = \[root\]
>
> while queue:
>
> level_size = len(queue) prev_node = None
>
> for i in range(level_size):
>
> current_node = queue.pop(0) \# Dequeue
>
> if prev_node:
>
> prev_node.next_right = current_node prev_node = current_node
>
> if current_node.left: queue.append(current_node.left)
>
> if current_node.right: queue.append(current_node.right)
>
> return root

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is enqueued and dequeued exactly
once.

**Space** **Complexity** **Analysis:** O(W), where W is the maximum
width of the binary tree. In the worst case (a complete binary tree), W
can be N/2, making the space complexity O(N). In the best case (skewed
tree), W is 1, making the space complexity O(1).

**Maximum** **Depth** **of** **Binary** **Tree**

**Problem** **Description:** Given the root of a binary tree, return its
maximum depth. The maximum depth is the number of nodes along the
longest path from the root node down to the farthest leaf node.

**Conceptual** **Approach:** This can be solved recursively using a DFS
approach. The maximum depth of a node is 1 plus the maximum depth of its
left or right subtree. The base case is an empty tree (depth 0).

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def max_depth(root): if not root:

> return 0
>
> left_depth = max_depth(root.left) right_depth = max_depth(root.right)
>
> return 1 + max(left_depth, right_depth)

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited exactly once.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity O(log N).

**Same** **Tree**

**Problem** **Description:** Given the roots of two binary trees, p and
q, return true if they are structurally identical and have the same
values at each node, or false otherwise. **Conceptual** **Approach:**
This is a classic recursive problem.

> 1\. If both p and q are None, they are identical (base case). 2. If
> one is None and the other is not, they are not identical.
>
> 3\. If both are not None, compare their values. If different, return
> false.

4\. Recursively check if their left subtrees are identical AND their
right subtrees are identical. **Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def is_same_tree(p, q):

> \# Both are None, so they are the same if not p and not q:
>
> return True
>
> \# One is None and the other is not, so they are different if not p or
> not q:
>
> return False
>
> \# Values are different if p.val != q.val:
>
> return False
>
> \# Recursively check left and right subtrees return
> is_same_tree(p.left, q.left) and \\
>
> is_same_tree(p.right, q.right)

**Time** **Complexity** **Analysis:** O(min(N\\p, N\\q)), where N\\p and
N\\q are the number of nodes in tree p and tree q respectively. In the
worst case, we might visit all nodes of the smaller tree.

**Space** **Complexity** **Analysis:** O(min(H\\p, H\\q)), where H\\p
and H\\q are the heights of tree p and tree q. This space is used by the
recursion call stack. In the worst case (skewed tree), H can be N,
making the space complexity O(N). In the best case (balanced tree), H is
log N,

making the space complexity O(log N).

**Symmetric** **Tree**

**Problem** **Description:** Given the root of a binary tree, check
whether it is a mirror of itself (i.e., symmetric around its center).

**Conceptual** **Approach:** This is identical to the "Test if a binary
tree is symmetric" problem solved earlier. The approach is to define a
helper function is_mirror(node1, node2) that checks if two subtrees are
mirror images.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def is_symmetric_tree(root): \# Renamed to avoid clash, functionally
same as is_symmetric

> if not root: return True
>
> def is_mirror(node1, node2): if not node1 and not node2:
>
> return True
>
> if not node1 or not node2 or node1.val != node2.val: return False

return is_mirror(node1.left, node2.right) and is_mirror(node1.right,
node2.left)

> return is_mirror(root.left, root.right)

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each pair of nodes that are compared (which
effectively covers all nodes once) contributes a constant amount of
work.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity O(log N).

**Invert/Flip** **Binary** **Tree**

**Problem** **Description:** Given the root of a binary tree, invert the
tree, and return its root. Inverting means swapping the left and right
children of every node.

**Conceptual** **Approach:** This can be done recursively. For a given
node, swap its left and right children. Then, recursively call the
invert function on its new left child (which was the original right
child) and its new right child (which was the original left child).

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def invert_tree(root):

> if not root: return None
>
> \# Swap the left and right children root.left, root.right =
> root.right, root.left
>
> \# Recursively invert the left and right subtrees
> invert_tree(root.left)
>
> invert_tree(root.right)
>
> return root

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited exactly once.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity O(log N).

**Binary** **Tree** **Maximum** **Path** **Sum**

**Problem** **Description:** A path in a binary tree is a sequence of
nodes where each pair of adjacent nodes in the sequence has an edge
connecting them. A node can only appear in the sequence **at** **most**
**once**. The path does not need to pass through the root. The path sum
is the sum of the node's values in the path. Given the root of a binary
tree, return the maximum path sum.

**Conceptual** **Approach:** This is a tricky one. We need a recursive
DFS. For each node, we consider two types of path sums:

> 1\. **Path** **that** **includes** **the** **current** **node**
> **and** **potentially** **extends** **upwards** **(to** **its**
> **parent):** This path must go through either its left child's maximum
> path or its right child's maximum path. The value is node.val + max(0,
> max_path_from_left_child, max_path_from_right_child). We use max(0,
> ...) because if a child's path sum is negative, we'd rather not
> include it.
>
> 2\. **Path** **that** **starts** **and** **ends** **within** **the**
> **subtree** **rooted** **at** **the** **current** **node**
> **(potentially** **a** **"V"** **shape** **or** **just** **a**
> **straight** **line):** This path includes the current node and
> potentially connects its left and right subtrees. The value is
> node.val + max(0, max_path_from_left_child) + max(0,
> max_path_from_right_child). This is the candidate for the *overall*
> *maximum* *path* *sum*.

We'll need a global variable (or passed by reference) to keep track of
the maximum path sum found so far. The recursive function will return
the maximum path sum that *can* *extend* *upwards* from the current
node.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def max_path_sum(root):

> \# Use a list to hold max_so_far as it needs to be mutable across

recursive calls

> max_so_far = \[-float('inf')\]
>
> def dfs(node): if not node:
>
> return 0
>
> \# Recursively get max path sum from left and right children
>
> \# max(0, ...) handles cases where a child path sum is negative
> left_gain = max(0, dfs(node.left))
>
> right_gain = max(0, dfs(node.right))
>
> \# Calculate path sum that goes through the current node

\# This is a potential candidate for the overall maximum path sum

> current_path_sum = node.val + left_gain + right_gain max_so_far\[0\] =
> max(max_so_far\[0\], current_path_sum)

\# Return the maximum gain if we were to extend this path upwards from
current node

> return node.val + max(left_gain, right_gain)
>
> dfs(root)
>
> return max_so_far\[0\]

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited exactly once.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity O(log N).

**Binary** **Tree** **Level** **Order** **Traversal**

**Problem** **Description:** Given the root of a binary tree, return the
level order traversal of its nodes' values. (i.e., from left to right,
level by level).

**Conceptual** **Approach:** This is a classic Breadth-First Search
(BFS) problem. We use a queue to keep track of nodes to visit.

> 1\. Initialize an empty queue and add the root. 2. Initialize an empty
> list to store the results. 3. While the queue is not empty:
>
> ○ Get the current level's size (number of nodes in the queue). ○
> Create a list to store nodes for the current level.
>
> ○ Iterate level_size times: ■ Dequeue a node.
>
> ■ Add its value to the current level's list.
>
> ■ Enqueue its left child (if exists). ■ Enqueue its right child (if
> exists).

○ Add the current level's list to the overall result. **Python**
**Code** **Solution:**

import collections

\# Assuming TreeNode class from previous problems

def level_order(root): result = \[\]

> if not root: return result
>
> queue = collections.deque(\[root\])
>
> while queue:
>
> level_size = len(queue) current_level_nodes = \[\] for \_ in
> range(level_size):
>
> node = queue.popleft() current_level_nodes.append(node.val)
>
> if node.left: queue.append(node.left)
>
> if node.right: queue.append(node.right)
>
> result.append(current_level_nodes) return result

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is enqueued and dequeued exactly
once.

**Space** **Complexity** **Analysis:** O(W), where W is the maximum
width of the binary tree. In the worst case (a complete binary tree), W
can be N/2, making the space complexity O(N). In the best case (skewed
tree), W is 1, making the space complexity O(1).

**Serialize** **and** **Deserialize** **Binary** **Tree**

**Problem** **Description:** Design an algorithm to serialize and
deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to
ensure that a binary tree can be serialized to a string and this string
can be deserialized to the original tree structure.

**Conceptual** **Approach** **(Preorder** **Traversal** **with**
**Markers):** A common way to do this is using a preorder traversal and
marking null nodes with a special character (e.g., \#).

**Serialization:** Perform a preorder DFS. For each node, append its
value to a list (or string). If it's a null node, append the marker.
Join the elements with a delimiter.

**Deserialization:** Split the string by the delimiter to get a list of
values. Use a global index (or

iterator) to keep track of the current position in the list. Recursively
build the tree: 1. Read the next value.

> 2\. If it's the marker, return None.
>
> 3\. Otherwise, create a node with that value. 4. Recursively build its
> left child.

5\. Recursively build its right child. **Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

class Codec:

> def serialize(self, root):
>
> """Encodes a tree to a single string. :type root: TreeNode
>
> :rtype: str """
>
> if not root:
>
> return "#" \# Marker for null

return str(root.val) + "," + self.serialize(root.left) + "," +
self.serialize(root.right)

> def deserialize(self, data):
>
> """Decodes your encoded data to tree. :type data: str
>
> :rtype: TreeNode """
>
> values = data.split(',')

\# Use a list to manage the index as it needs to be modified by
recursive calls

> index = \[0\]
>
> def build_tree():
>
> if index\[0\] \>= len(values): return None
>
> val = values\[index\[0\]\] index\[0\] += 1
>
> if val == '#': return None
>
> node = TreeNode(int(val)) node.left = build_tree() node.right =
> build_tree() return node
>
> return build_tree()

**Time** **Complexity** **Analysis:**

> ● **Serialize:** O(N), where N is the number of nodes in the binary
> tree (including null nodes represented by markers). Each node is
> visited once.
>
> ● **Deserialize:** O(N), where N is the number of elements in the
> serialized string. Each element is processed once.

**Space** **Complexity** **Analysis:**

> ● **Serialize:** O(H) for the recursion stack (where H is the height
> of the tree) and O(N) for the resulting string.
>
> ● **Deserialize:** O(H) for the recursion stack and O(N) for storing
> the values list. In the worst case (skewed tree), H can be N, so O(N)
> overall.

**Subtree** **of** **Another** **Tree**

**Problem** **Description:** Given the roots of two binary trees, root
and subRoot, return true if there is a subtree of root with the same
structure and node values of subRoot and false otherwise. A subtree of a
binary tree tree is tree itself or any subtree of its right or left
child.

**Conceptual** **Approach:** This problem can be broken down into two
parts:

> 1\. A helper function is_same_tree(p, q) (already implemented) to
> check if two trees are identical.
>
> 2\. A main function that traverses root using DFS. At each node in
> root, check if the subtree rooted at that node is identical to subRoot
> using is_same_tree. If not, recursively check the left and right
> subtrees of root.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def is_same_tree(p, q): \# Helper function if not p and not q:

> return True
>
> if not p or not q or p.val != q.val: return False

return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def is_subtree(root, subRoot): if not root:

> return False

if not subRoot: \# An empty tree is considered a subtree of any tree (by
some definitions)

> return True

\# Check if the current subtree rooted at 'root' is identical to
'subRoot'

> if is_same_tree(root, subRoot): return True
>
> \# Otherwise, recursively check left and right subtrees of 'root'

return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)

**Time** **Complexity** **Analysis:** O(N \\cdot M), where N is the
number of nodes in root and M is the number of nodes in subRoot. In the
worst case, is_same_tree is called for every node in root, and each call
might traverse subRoot.

**Space** **Complexity** **Analysis:** O(max(H\\{root}, H\\{subRoot})),
where H\\{root} and H\\{subRoot} are the heights of the respective
trees. This space is used by the recursion call stack.

**Find** **Leaves** **of** **Binary** **Tree**

**Problem** **Description:** Given the root of a binary tree, collect
all nodes that are leaves, and then remove those leaves. Repeat until
the tree is empty. Return a list of lists representing the leaves
collected at each step.

**Conceptual** **Approach:** This problem is best solved by thinking
about the "height" or "depth" of a node *from* *the* *leaf*. A node is a
leaf if its height from the leaf is 0. Its parent will have a height of
1 (after its children are removed), and so on. We can use a recursive
DFS approach. For each node, calculate its "height from the leaf" (0 for
a leaf, 1 + max height of its children otherwise). Store nodes in a list
of lists where the index corresponds to this height.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def find_leaves(root):

result = \[\] \# List of lists, where result\[i\] holds leaves at height
i

> def dfs(node): if not node:

return -1 \# Height of a null node relative to its parent (or a leaf)

> left_height = dfs(node.left) right_height = dfs(node.right)
>
> current_height = 1 + max(left_height, right_height)
>
> \# Ensure result list has enough sublists if len(result) \<=
> current_height:

\# Pad with empty lists if current_height is larger than current length

> while len(result) \<= current_height: result.append(\[\])
>
> result\[current_height\].append(node.val)
>
> return current_height
>
> dfs(root) return result

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited exactly once to compute
its height and add it to the correct list.

**Space** **Complexity** **Analysis:** O(H) for the recursion stack
(where H is the height of the tree) and O(N) for storing the result
lists. In the worst case, H can be N, so O(N) overall.

**Construct** **Binary** **Tree** **from** **Preorder** **and**
**Inorder** **Traversal**

**Problem** **Description:** This is the same problem as "Reconstruct a
binary tree from traversal data" already discussed.

**Conceptual** **Approach** **&** **Python** **Code** **Solution:**
Please refer to the previous section on "Reconstruct a binary tree from
traversal data", which includes both a basic and an optimized solution.

**Validate** **Binary** **Search** **Tree**

**Problem** **Description:** Given the root of a binary tree, determine
if it is a valid Binary Search Tree (BST). A valid BST is defined as
follows:

> ● The left subtree of a node contains only nodes with values **less**
> **than** the node's value. ● The right subtree of a node contains only
> nodes with values **greater** **than** the node's
>
> value.
>
> ● Both the left and right subtrees must also be valid BSTs.

**Conceptual** **Approach:** A common mistake is to only check if
node.left.val \< node.val and node.right.val \> node.val. This is
insufficient. The critical property of a BST is that for any node, *all*
nodes in its left subtree must be less than its value, and *all* nodes
in its right subtree must be greater.

This implies passing down a valid range for each node.

> 1\. Initialize min_val to negative infinity and max_val to positive
> infinity for the root. 2. Recursively check:
>
> ○ For the current node, its value must be within (min_val, max_val).
> If not, return false.
>
> ○ Recursively call for the left child with range (min_val, node.val).

○ Recursively call for the right child with range (node.val, max_val).
**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def is_valid_bst(root):

> \# Helper function to pass min_val and max_val bounds def
> validate(node, min_val, max_val):
>
> if not node:
>
> return True
>
> \# Check if current node's value is within the allowed range if not
> (min_val \< node.val \< max_val):
>
> return False
>
> \# Recursively check left subtree with updated max_val \# Recursively
> check right subtree with updated min_val return validate(node.left,
> min_val, node.val) and \\
>
> validate(node.right, node.val, max_val)
>
> \# Initial call with negative and positive infinity as bounds return
> validate(root, -float('inf'), float('inf'))

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is visited exactly once.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the binary tree. This space is used by the recursion call stack. In the
worst case (skewed tree), H can be N, making the space complexity O(N).
In the best case (balanced tree), H is log N, making the space
complexity O(log N).

**Kth** **Smallest** **Element** **in** **a** **BST**

**Problem** **Description:** Given the root of a Binary Search Tree
(BST) and an integer k, return the k-th smallest value (1-indexed) among
all the values in the tree.

**Conceptual** **Approach:** The inorder traversal of a BST yields its
elements in sorted (ascending) order. Therefore, we can perform an
inorder traversal and keep a counter. When the counter reaches k, we
have found the k-th smallest element.

**Python** **Code** **Solution** **(Iterative** **Inorder):**

\# Assuming TreeNode class from previous problems

def kth_smallest(root, k): stack = \[\]

> current = root count = 0
>
> while current or stack:
>
> \# Traverse to the leftmost node while current:
>
> stack.append(current) current = current.left
>
> \# Pop the smallest element current = stack.pop() count += 1
>
> if count == k:
>
> return current.val
>
> \# Move to the right subtree current = current.right
>
> return -1 \# Should not happen if k is valid

**Time** **Complexity** **Analysis:** O(H + k), where H is the height of
the BST. In the worst case, if k is close to N (number of nodes), it can
be O(N). Specifically, we traverse down to the leftmost node (O(H)) and
then visit k nodes.

**Space** **Complexity** **Analysis:** O(H), where H is the height of
the BST. This space is used by the stack. In the worst case (skewed
tree), H can be N, making the space complexity O(N). In the best case
(balanced tree), H is log N, making the space complexity O(log N).

**Lowest** **Common** **Ancestor** **of** **BST**

**Problem** **Description:** Given a Binary Search Tree (BST), find the
lowest common ancestor (LCA) of two given nodes p and q. The LCA of two
nodes p and q is the lowest node in T that has both p and q as
descendants (where we allow a node to be a descendant of itself).
**Conceptual** **Approach** **(Leveraging** **BST** **property):** The
BST property (left child \< parent \< right child) simplifies LCA
finding significantly compared to a general binary tree.

> 1\. Start from the root.
>
> 2\. If both p.val and q.val are less than root.val, then the LCA must
> be in the left subtree. Move to root.left.
>
> 3\. If both p.val and q.val are greater than root.val, then the LCA
> must be in the right subtree. Move to root.right.
>
> 4\. If neither of the above conditions is met (i.e., p.val is on one
> side and q.val is on the other, or one of them is equal to root.val),
> then the current root is the LCA. This is because this is the first
> node where p and q diverge or one of them is found.

**Python** **Code** **Solution:**

\# Assuming TreeNode class from previous problems

def lowest_common_ancestor_bst(root, p, q): if not root:

> return None
>
> \# If both p and q are in the left subtree if p.val \< root.val and
> q.val \< root.val:
>
> return lowest_common_ancestor_bst(root.left, p, q) \# If both p and q
> are in the right subtree
>
> elif p.val \> root.val and q.val \> root.val:
>
> return lowest_common_ancestor_bst(root.right, p, q)

\# Otherwise, root is the LCA (p and q are on different sides, or one of
them is root)

> else:
>
> return root

**Time** **Complexity** **Analysis:** O(H), where H is the height of the
BST. In the worst case (skewed tree), H can be N, making the space
complexity O(N). In the best case (balanced tree), H is log N, making
the space complexity O(log N). We traverse down a single path from the
root. **Space** **Complexity** **Analysis:** O(H) for the recursion
stack. This can be optimized to O(1) with an iterative approach.

*Iterative* *Solution:*

\# Assuming TreeNode class from previous problems

def lowest_common_ancestor_bst_iterative(root, p, q): current = root

> while current:
>
> if p.val \< current.val and q.val \< current.val: current =
> current.left
>
> elif p.val \> current.val and q.val \> current.val: current =
> current.right

else: \# Found the split point or one of the nodes is the current node

> return current return None

**Time** **Complexity** **Analysis** **(Iterative):** O(H). **Space**
**Complexity** **Analysis** **(Iterative):** O(1).

**Binary** **Tree** **Zigzag** **Level** **Order** **Traversal**

**Problem** **Description:** Given the root of a binary tree, return the
zigzag level order traversal of its nodes' values. (i.e., from left to
right, then right to left for the next level and so on). **Conceptual**
**Approach:** This is a variation of Level Order Traversal (BFS). We'll
still use a queue. The main difference is how we add elements to the
current level's list.

> 1\. Maintain a level counter, starting from 0.
>
> 2\. If level is even, add nodes from left to right to the current
> level's list.
>
> 3\. If level is odd, add nodes from right to left to the current
> level's list. A deque can be useful for efficiently adding to both
> ends, or simply reverse the list after collecting.

**Python** **Code** **Solution** **(Using** **deque** **and**
**reversing):** import collections

\# Assuming TreeNode class from previous problems

def zigzag_level_order(root): result = \[\]

> if not root: return result
>
> queue = collections.deque(\[root\]) level = 0
>
> while queue:
>
> level_size = len(queue) current_level_nodes = \[\] for \_ in
> range(level_size):
>
> node = queue.popleft() current_level_nodes.append(node.val)
>
> if node.left: queue.append(node.left)
>
> if node.right: queue.append(node.right)
>
> if level % 2 == 1: \# Odd level, reverse the list
> current_level_nodes.reverse()
>
> result.append(current_level_nodes) level += 1
>
> return result

**Time** **Complexity** **Analysis:** O(N), where N is the number of
nodes in the binary tree. Each node is enqueued and dequeued exactly
once. The reverse() operation for each level takes time proportional to
the number of nodes at that level, summing up to O(N) overall.

**Space** **Complexity** **Analysis:** O(W), where W is the maximum
width of the binary tree. In the worst case (a complete binary tree), W
can be N/2, making the space complexity O(N). This also includes the
space for storing the current_level_nodes.

**Implement** **Trie** **(Prefix** **Tree)**

**Problem** **Description:** Implement the Trie (Prefix Tree) data
structure. It should support the following operations: insert, search,
and starts_with.

**Conceptual** **Approach:** A Trie is a tree-like data structure used
to store a dynamic set of strings where each node represents a
character. Each path from the root to a node represents a prefix. Each
node typically has:

> ● A dictionary (or array of 26 for English alphabet) to store
> children, mapping a character to its child node.

● A boolean flag is_end_of_word to indicate if the path to this node
forms a complete word. **Python** **Code** **Solution:**

class TrieNode:

> def \_\_init\_\_(self): self.children = {} self.is_end_of_word = False

class Trie:

> def \_\_init\_\_(self): self.root = TrieNode()
>
> def insert(self, word: str) -\> None: """
>
> Inserts a word into the trie. """
>
> node = self.root for char in word:
>
> if char not in node.children: node.children\[char\] = TrieNode()
>
> node = node.children\[char\] node.is_end_of_word = True
>
> def search(self, word: str) -\> bool: """
>
> Returns true if the word is in the trie. """
>
> node = self.root for char in word:
>
> if char not in node.children: return False
>
> node = node.children\[char\] return node.is_end_of_word
>
> def starts_with(self, prefix: str) -\> bool: """

Returns true if there is any word in the trie that starts with the given
prefix.

> """
>
> node = self.root for char in prefix:
>
> if char not in node.children: return False
>
> node = node.children\[char\] return True

**Time** **Complexity** **Analysis:**

> ● **insert(word):** O(L), where L is the length of the word. We
> traverse each character once. ● **search(word):** O(L), where L is the
> length of the word. We traverse each character once. ●
> **starts_with(prefix):** O(P), where P is the length of the prefix. We
> traverse each character
>
> once.

**Space** **Complexity** **Analysis:**

> ● O(TotalChars), where TotalChars is the total number of unique
> characters across all words stored in the Trie. In the worst case, if
> words share no prefixes, it could be O(\\sum L\\i \\cdot A), where
> L\\i is the length of each word and A is the size of the alphabet
> (e.g., 26 for lowercase English letters). Each node itself takes
> constant space (dictionary and boolean).

**Add** **and** **Search** **Word** **(Design** **an** **Add** **and**
**Search** **Words** **Data** **Structure)**

**Problem** **Description:** Design a data structure that supports
adding new words and finding if a string matches any previously added
word. The string can contain regular alphabet characters a-z or a .
(dot) character. A . can represent any single letter.

**Conceptual** **Approach:** This extends the Trie concept. The addWord
operation is identical to Trie.insert. The search operation is where the
. wildcard comes into play. When . is encountered, we need to
recursively check all possible child paths.

**Python** **Code** **Solution:** class TrieNode:

> def \_\_init\_\_(self): self.children = {} self.is_end_of_word = False

class WordDictionary: def \_\_init\_\_(self):

> self.root = TrieNode()
>
> def addWord(self, word: str) -\> None: """
>
> Adds a word into the data structure. """
>
> node = self.root for char in word:
>
> if char not in node.children: node.children\[char\] = TrieNode()
>
> node = node.children\[char\] node.is_end_of_word = True
>
> def search(self, word: str) -\> bool: """

Returns true if the word is in the data structure. A word can contain
the dot character '.' to represent any one letter.

> """
>
> def dfs_search(node, k): \# k is the current index in the word if k ==
> len(word):
>
> return node.is_end_of_word
>
> char = word\[k\]
>
> if char == '.':
>
> \# Try all possible children
>
> for child_char in node.children:
>
> if dfs_search(node.children\[child_char\], k + 1): return True
>
> return False else:
>
> \# Normal character matching if char in node.children:
>
> return dfs_search(node.children\[char\], k + 1) else:
>
> return False
>
> return dfs_search(self.root, 0)

**Time** **Complexity** **Analysis:**

> ● **addWord(word):** O(L), where L is the length of the word.
>
> ● **search(word):** In the worst case, if the word consists entirely
> of . characters, it could be O(A^L), where A is the size of the
> alphabet and L is the length of the word, as it might explore all
> possible paths. However, for a practical dictionary, the average case
> is much better, more akin to O(L) for a fixed alphabet size. The
> complexity depends on the number of branches explored due to .
> characters.

**Space** **Complexity** **Analysis:**

> ● O(TotalChars) for storing the Trie nodes. The search operation uses
> O(L) space for the recursion stack.

**Word** **Search** **II**

**Problem** **Description:** Given an m x n board of characters and a
list of strings words, return all words on the board. Each word must be
constructed from letters of sequentially adjacent cells, where adjacent
cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once in the same word.

**Conceptual** **Approach:** This problem combines Trie with
Backtracking (DFS).

> 1\. **Build** **a** **Trie:** Insert all words from the given list
> into a Trie. This allows efficient prefix checking.
>
> 2\. **DFS** **with** **Backtracking:** Iterate through each cell (r,
> c) on the board. From each cell, start a DFS.
>
> ○ In the DFS, at each step (r, c):
>
> ■ Check if the character board\[r\]\[c\] forms a valid prefix with the
> current path in the Trie.
>
> ■ If it forms a valid prefix, move to the corresponding Trie node.
>
> ■ If the Trie node marks the end of a word, add that word to the
> result set.
>
> ■ Mark the current cell board\[r\]\[c\] as visited (e.g., by
> temporarily changing its character to a marker).
>
> ■ Recursively call DFS for all four adjacent cells.
>
> ■ **Backtrack:** Unmark the current cell (restore its original
> character).
>
> ○ To avoid duplicates and for efficiency, once a word is found, it can
> be removed from the Trie (or just mark it as found and ensure it's not
> added again to the result).

**Python** **Code** **Solution:** class TrieNode:

> def \_\_init\_\_(self):
>
> self.children = {}

self.word = None \# Store the full word here if this node marks end of a
word

class WordDictionaryForWordSearch: \# Renamed to avoid clash def
\_\_init\_\_(self):

> self.root = TrieNode()
>
> def addWord(self, word: str) -\> None: node = self.root
>
> for char in word:
>
> if char not in node.children: node.children\[char\] = TrieNode()
>
> node = node.children\[char\]
>
> node.word = word \# Mark the end of a word

def find_words(board, words):

> trie = WordDictionaryForWordSearch() for word in words:
>
> trie.addWord(word)
>
> rows, cols = len(board), len(board\[0\])
>
> result = set() \# Use a set to handle unique words
>
> def dfs(r, c, current_trie_node): char = board\[r\]\[c\]
>
> if char not in current_trie_node.children: return
>
> next_trie_node = current_trie_node.children\[char\]
>
> \# If a word is found if next_trie_node.word:
>
> result.add(next_trie_node.word)

\# Optimization: Mark the word as found in Trie to avoid duplicates

\# next_trie_node.word = None \# Or remove the word if no other longer
word shares this prefix

> \# Mark as visited by changing the character board\[r\]\[c\] = '#'
>
> \# Explore neighbors

directions = \[(0, 1), (0, -1), (1, 0), (-1, 0)\] \# Right, Left, Down,
Up

> for dr, dc in directions: nr, nc = r + dr, c + dc
>
> if 0 \<= nr \< rows and 0 \<= nc \< cols and board\[nr\]\[nc\] !=

'#':

> dfs(nr, nc, next_trie_node)
>
> \# Backtrack: restore the character board\[r\]\[c\] = char
>
> for r in range(rows): for c in range(cols):
>
> dfs(r, c, trie.root)
>
> return list(result)

**Time** **Complexity** **Analysis:**

> ● **Building** **Trie:** O(\\sum L\\i), where L\\i is the length of
> each word in words.
>
> ● **DFS:** In the worst case, if all characters can form paths and
> many words overlap, the time complexity can be complex. However, it's
> roughly O(M \\cdot N \\cdot (4 \\cdot L\\{max})), where M \\cdot N is
> the board size, and L\\{max} is the maximum word length. Each DFS path
> visits cells, and at each cell, it makes recursive calls to 4
> neighbors. The Trie lookup at each step is O(1) (since character
> access is constant). So, it's approximately O(MN \\cdot 4^L) in the
> extreme worst-case, but the Trie prunes branches significantly. More
> precisely, it's related to the total number of paths in the Trie that
> can be formed on the board.

**Space** **Complexity** **Analysis:**

> ● O(\\sum L\\i \\cdot A) for the Trie, where A is the alphabet size
> (for storing children dictionaries).
>
> ● O(L\\{max}) for the recursion stack during DFS.
>
> ● O(K) for the result set, where K is the number of found words.

I hope this comprehensive breakdown helps! Remember, to get a PDF,
you'll need to copy and paste this into a document editor.
