# Top 50 Data Structure Knowledge Interview Questions

[Original source link](https://career.guru99.com/top-50-data-structure-interview-questions/)

## 1. What is data structure

A data structure is a means to organize and manipulate data quickly and efficiently.

---

## 2. Differentiate between file and structure storage structures

File structure will save data into memory that is not within the system. Storage structure is memory within the system.

---

## 3. When is a binary search best applied

A binary search is best applied to a collection of already sorted data. Since the data is sorted, the search will take O(log n) time to find what is needed. __*Binary search can only be executed on a sorted collection.*__

---

## 4. What is a linked list

A linked list is data structure created with *Nodes*. A Node contains the data that it is storing and reference to the next Node in the list. Think of a linked list as a single-filed line, where you only know about the person who is infront of you. The structure just described is a single-linked list. A *Linked List* will always contain a *Head* reference which keeps track of the current Node that is being looked at and is used to traverse the list. The Head can be thought of as a person going through the line and picking individual people out.

---

## 5. How do you reference all the elements in a one-dimension array

Use a for loop and traverse from index 0 to len(list)-1 and perform operation(s) on each item in the array.

---

## 6. In what areas are data structures are applied

Anything that involves an algorithm, or when you need to organize data.

---

## 7. What is LIFO

Last-In-First-Out. A Stack data structure utilizes a LIFO approach, where the last item inserted into the Stack is the first item to be taken out. A LIFO structure is analogous to a stack of dishes. If you have a stack of dishes and need to take one off, you will take a dish off the top. If you need to add a dish to the stack of dishes, you will add it to the top.

---

## 8. What is queue

A queue is a data structure that deals with elements in a FIFO manner. First-In-First-Out. The first item to come into the queue is the first item to leave the queue, similar to how you might wait in a line. A queue has 2 main operations

1. Dequeue(), *removes* an item from the front of the queue and returns it
2. Enqueue(), *adds* an item to the end of a queue 

Worst-case Runtimes:

- Search, O(n)
- Enqueue, O(1)
- Dequeue, O(n)

---

## 9. What are binary trees

A Binary Tree is a tree where every node in the tree has at most 2 children.

Worst-case Runtimes:

- Search, O(n)
- Insert, O(n)
- Delete, O(n)

Best-case Runtimes (when the tree is balanced):

- Search, O(log n)
- Insert, O(log n)
- Delete, O(log n)

---

## 10. Which data structures are applied when dealing with a recursive function

A stack is used in memory when recursion is used. It will store the return address of the function that called it, so
when it computes the value it can return it to the parent call.

---

## 11. What is a stack

A Stack is a data structure that stores items in a Last-In-First-Out approach (i.e. the last item to be added in is the 
first item to be removed).

Worst-case Runtimes:

- Search, O(n)
- Insert/Push, O(1) (when removing a node from the top of the stack)
- Delete/Pop, O(1) (when removing a node from the top of the stack)

---

__12. Explain Binary Search Tree.__

__13. What are multidimensional arrays?__

__14. Are linked lists considered linear or non-linear data structures?__

__15. How does dynamic memory allocation help in managing data?__

__16. What is FIFO?__

__17. What is an ordered list?__

__18. What is merge sort?__

__19. Differentiate NULL and VOID.__

__20. What is the primary advantage of a linked list?__

__21. What is the difference between a PUSH and a POP?__

__22. What is a linear search?__

__23. How does variable declaration affect memory allocation?__

__24. What is the advantage of the heap over a stack?__

__25. What is a postfix expression?__

__26. What is Data abstraction?__

__27. How do you insert a new item in a binary search tree?__

__28. How does a selection sort work for an array?__

__29. How do signed and unsigned numbers affect memory?__

__30. What is the minimum number of nodes that a binary tree can have?__

__31. What are dynamic data structures?__

__32. In what data structures are pointers applied?__

__33. Do all declaration statements result in a fixed reservation in.__

__34. What are ARRAYs?__

__35. What is the minimum number of queues needed when implementing a priority queue.__

__36. Which sorting algorithm is considered the fastest?__

__37. Differentiate STACK from ARRAY.__

__38. Give a basic algorithm for searching a binary search tree.__

__39. What is a dequeue?__

__40. What is a bubble sort and how do you perform it?__

__41. What are the parts of a linked list?__

__42. How does selection sort work?__

__43. What is a graph?__

__44. Differentiate linear from a nonlinear data structure.__

__45. What is an AVL tree?__

__46. What are doubly linked lists?__

__47. What is Huffman's algorithm?__

__48. What is Fibonacci search?__

__49. Briefly explain recursive algorithm.__

__50. How do you search for a target key in a linked list?__
