# Topological Sort
A topological sort (sometimes also called a linearization) of a directed graph is a list of the  
vertices in such an order that if there is a directed path from vertex v to vertex w,  
then v precedes w in the list. (The graph must be acyclic in order for this to work. Directed  
acyclic graphs are common enough to be referred to by their acronym: DAGs.)
Here is an example of a DAG:
![image](https://github.com/yadavraganu/dsa/assets/77580939/951e250d-84ca-4a26-9185-c1fa34962f27)

In the above DAG, a few of the possible topological sorts could be:
```
1. A B C D E F G H
2. A C B E G D F H
3. B E G A D C F H
```
