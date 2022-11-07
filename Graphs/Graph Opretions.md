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
The traversal follows a node depth wise cannot go deeper
Then go to neighbor of first node and repeat

"Explore one direction -> as far as possible before switching directions"

They are implement using stack dataframe. A stack is LIFO
- Take a starting node of [a] and push to top of stack
- Pop of a from stack: a is current node
- Push neighbors to the stack [b, c]
- end of first iteration
- pop top of stack [b]
- look at b's neighbors and push to top of stack [d]
- [d] is top of stack pop [d] and push neighbors to top of stack
- repeat, if no neighbor pop of next item in stack
When stack is empty algorithm is done


### Breadth First Search
The traversal follows all neighbors of the starting node
- initialise Queue with [a] 
- pop [a] and assign as current node and add neighbors to back of Queue
- end of first iteration
- pop [b] from Queue and add neighbors to back of Queue #vs stack that goes in front 
- pop [c] from Queue and add neighbors to back of Queue
- pop [d] from Queue and add neighbors to back of Queue
- pop [e] from Queue and has no neighbors 
- pop [f] from Queue and has no neighbors

### Terminologies
- neighbors
