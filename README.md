# Text to Non-BinaryTree

### Non Binary Tree Class
The Node class represents a node in a tree structure. 
* item: Represents the item value of the node. It can hold any value associated with the node.  
* type: Represents the type of the node. It can be used to denote the role or distinction of a particular node.  
* children: Stores references to the child nodes of the current node in a list.
```python
class Node:
    def __init__(self, item,type_):
        self.item = item
        self.type = type_
        self.children = []
```

The NBT class represents a Node-Based Tree.
* root: Represents the root node of the tree, indicating the starting   point of the tree.

```python
class NBT:
    def __init__(self, r):
        self.root = r
```
---

### Input
#### Input Rule
1. Only use keyword node and leaf 
2. Use colon to assign value 
3. Child node must be parenthesized
4. Leaf can't have child node
```python
input = '''
    node:"food"{
        leaf:"I love food",
        leaf:"my favorite food is mola😁",
        node:"korean food"{
            leaf:"kimchi",
            node:"tang"{
                leaf:"budaejjigae",
                leaf:"kimchijjigae",
                node:"seafoodtang"{
                    leaf:"haemuljjambbongtang",
                },
                node:"sogogitang"{
                    leaf:"galbijjim",
                }
            },
        },
        node:"chinese food"{
            leaf:"tanghulu",
            leaf:"tangsuyuk",
            leaf:"jjambbong",
        }
    }

    node:"programming"{
        leaf:"not coding",
        node:"c++"{
            leaf:"adlfkjlsfkgj"
        }
        node:"java"{
            leaf:"akfjgslfjg"
        }
        node:"python"{
            leaf:"aldkfjs;lkfgj;sklf",
            leaf:"askfdjg;slkfj;"
        }
    }
'''
```

---
### Output Visualization

REF : https://copyprogramming.com/howto/how-to-print-a-tree-in-python

```
     ┌I love food
     ├my favorite food is mola😁
     │            ┌tanghulu
     ├chinese food┤
     │            ├jjambbong
     │            └tangsuyuk
 food┤
     │           ┌kimchi
     └korean food┤
                 │    ┌budaejjigae
                 │    ├kimchijjigae
                 └tang┤
                      ├sogogitang┐
                      │          └galbijjim
                      └seafoodtang┐
                                  └haemuljjambbongtang
            ┌not coding
            ├c++┐
            │   └adlfkjlsfkgj
 programming┤
            │      ┌aldkfjs;lkfgj;sklf
            ├python┤
            │      └askfdjg;slkfj;
            └java┐
                 └akfjgslfjg
```