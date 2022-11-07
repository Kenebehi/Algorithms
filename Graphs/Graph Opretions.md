## Graph Types
- Directed
- Undirected


### Representation of Graphs
1. Adjacency list on directed Graph
```
Dict[key]: value, key is node and value are the neigbhors.
Dict value is directed neighbors
{
    a: [b, c],
    b: [d],
    c: [e],
    d: [],
    e: [b]
    f: [d]
}

A -----------> C
|             |
|             |
|             |
B             E
|
|
|
|
D-------------> F
```

### Depth First Search
The traversal follows a node depth wise until it cannot go deeper Then goes to neighbor of first node and repeat the steps.
`Explore one direction -> as far as possible before switching directions`

They are implemented using stack dataframe. A stack is LIFO [last in first out] -->  [A, B, C] ---> [A, B]
- Take a starting node of [A] and push to top of stack [last item to go in]     ---> [A] curr = None
- Pop off [A] from stack: [A] is current node                                   ---> []  curr = A
- Push neighbors to the stack                                                   ---> [B, C] curr = A
- end of first iteration
- pop off stack [D]                                                             ---> [C]     curr = B
- look at [B]'s neighbors and push to top of stack [D]                          ---> [C, D]  curr = B
- [D] is top of stack pop [D] and push neighbors to top of stack                ---> [C]     curr = D
- repeat, if no neighbor pop of next item in stack
When stack is empty algorithm is done

- The general idea is for every node in the tree we look at the child of that node


### Breadth First Search
The traversal follows all neighbors of the starting node it is a FIFO [first in first out]
- initialise Queue with [A]                                                             ---> [A] curr = None
- pop [A] and assign as current node and add neighbors to back of Queue                 ---> [] curr = A
- end of first iteration
- pop [B] from Queue and add neighbors to back of Queue #vs stack that goes in front    ---> [A, ] curr = B
- pop [c] from Queue and add neighbors to back of Queue
- pop [d] from Queue and add neighbors to back of Queue
- pop [e] from Queue and has no neighbors 
- pop [f] from Queue and has no neighbors

### Terminologies
- neighbors
