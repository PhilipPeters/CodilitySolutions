""" Solution to the Germanium 2018 problem, link here: https://app.codility.com/programmers/challenges/germanium2018/
Short version: You have a deck of cards in which each card has two numbers: one on the front and one on the back. Flip some cards over so as to maximize the smallest integer that's not present on any card's front.

This looks like a simple dynamic programming problem with some clear optimal sub-structure-it is not. Maybe there is an a much easier solution, but 
given the principles uncovered in the solution I will deliver, it appears that this is actually the easiest way to go (we are proving definite relations between the problem and an algorithm to solve it).

First, we translate the problem into graph theory. We use an undirected graph, with Our vertex set is the numbers on th ecards, i.e. just positive integers.
We draw an edge between i and j, denoted ij, if there is a card with one side displaying i and one side displaying j. Note if there is a card
which shows the same number on both sides, we have a 'mini loop' from this vertex to itself. If we have 2 identical cards with x on one side, y on the other, 
then we have 2 edges xy.

Now we decompose our graph into its connected components. Then we can now see that we only need to solve the problem for each connected component,
then take the minimum of the answers for each component, and this is our answer.

We only have 2 cases: either we have a cycle in our component, or we don't. If we have a cycle (I am including our 'mini loop' 1 cycles, or a 2-cycle, i.e. 2 of the same edges, as examples of cycles), then every point in the component is representable.
If we do not have a cycle, then our graph is actually a tree (elementary graph theory). Then we know we cannot possibly include every vertex, but we can include all but 1 vertex, and we can choose this vertex.
To see this, imagine choosing a vertex v in our component, and adding the card (v,v). Then our component has a cycle, so every point can be shown. So removing this extra card, we have that every number except v can be shown.
Now we have a list of all numbers, in our vertex set, that cannot be shown (a maximal choice). Then we subtract this from our vetex set, to form a new set, and tatke the smallest positive integer not in this set, and that is our answer.

This is implemented in the code below: """
def solution(A, B):
  vertex_set = set(A) + set(B)

  #First I will write code to determine the connected components of our 'graph'
  from collections import defaultdict
  component_dict = defaultdict
  connected_list = []
  n = len(A)
  
  key_dict = {vertex_set[i]:i for i in range(0, len(vertex_set))}
  reverse_key_dict = {i:vertex_set[i] for i in range(0, len(vertex_set))}
  
  #To effectively implement this decomposition algortihm, we will use pointers (C++ style), so that if we have a and b are in the same component, and c and d are in the same component,
  #if we suddenly discover that a and c are in the same component, we only need 1 operation, using pointers, to make sure that we know a and d and b and c are in the same component.
  #Unfortunately we do not have pointers in Python readily available, but we have lists, so we will use 1 element lists.
  
  pointer_collection = []
  for i in range(0, len(vertex_set)):
    pointer_collection = pointer_collection + [[-1]]
  pointer_collection = [[-1]] * len(vertex_set)
  
  for i in range(0, n):
    if pointer_collection[key_dict[A[i]]][0] == -1 and pointer_collection[key_dict[B[i]]][0] == -1:
      pointer_collection[key_dict[A[i]]][0] = i
      """Note this line below makes sure the lists are 'permanently equal', as their addresses are the same, therefore if we change one list, the other is automatically updated"""
      pointer_collection[key_dict[B[i]]] = pointer_collection[key_dict[A[i]]]

    if pointer_collection[key_dict[A[i]]][0] == -1 and pointer_collection[key_dict[B[i]]][0] != -1:
      pointer_collection[key_dict[A[i]]] = pointer_collection[key_dict[B[i]]]

    if pointer_collection[key_dict[A[i]]][0] != -1 and pointer_collection[key_dict[B[i]]][0] == -1:
      pointer_collection[key_dict[B[i]]] = pointer_collection[key_dict[A[i]]]

    if pointer_collection[key_dict[A[i]]][0] != -1 and pointer_collection[key_dict[B[i]]][0] != -1:
      pointer_collection[key_dict[A[i]]] = pointer_collection[key_dict[B[i]]]
  
  """now we have a list containing different tags for each element in our vertex set. Now we change these tags into consecutive numbers, starting from 0, 
  so we can sort them into a bigger list later."""
  
  index = 0
  
  new_pointer_collection = [0] * len(vertex_set)
  """This defaultdict has default value = -1"""
  tag_map = defaultdict(lambda:-1)
  for i in range(0, len(pointer_collection)):
    if tag_map[pointer_collection[i][0]] == -1:
      tag_map[pointer_collection[i][0]] = index
      index = index + 1
      new_pointer_collection[i] = tag_map[pointer_collection[i][0]]
    else:
      new_pointer_collection[i] = tag_map[pointer_collection[i][0]]
  
  """now we have a list of tags, starting at 0, with consecutive positive integers, so we can just form a new list containing all these sub-collections, with their tags as their position in the outer array"""
  
  m = 0
  for i in range(0, len(new_pointer_collection)):
    m = max(m, new_pointer_collection[i])
  coll_0 = []
  for i in range(0, m):
    coll_0 = coll_0 + [[]]
  for i in range(0, len(new_pointer_collection)):
    coll_0[new_pointer_collection[i]].append(i)
  
  """now we want to take our list of connected components in terms of vertices, and make it into a list in terms of cards"""
  component_map_dict = {}
  for i in range(0, len(coll_0)):
    for j in range(0, len(coll_0[i]):
      component_map_dict[reverse_key_dict[j]] = i
  
  """now to form our collection of cards, as connected components"""
  
  coll_0 = []
  for i in range(0, m):
    coll_0 = coll_0 + [[]]
  for i in range(0, len(A)):
    coll[component_dict[A[i]][0].append(A[i])
    coll[component_dict[B[i]][1].append(B[i])

  #Now we have a list of connected components, each in the form of sub-collections of cards.
  #It is easy to test whether we have a cycle: just test if the number of vertices = number of edges + 1 (basic theory from trees).

  #This list records which points/vertices we cannot show
  not_shown = []

  for i in range(0, len(coll)):
    v = set(coll[i][0]) + set(coll[i][1])
    edge = len(coll[i][0]
    if len(v) = edge + 1:
      not_shown.append(max(v))

  #now we create a new vertex_set without the not_shown list
  shown_list = vertex_set - v
  
  #now to finish up
  if min(shown_list) != 1:
    return 1
  else:
    i = 1
    while i in shown_list:
      i = i + 1
    return i  
    
"""temporal complexity: each stage is O(N) (the most complicated part is the decomposition into connected components, but this is O(N)).
Spatial complexity: each auxilliary data structure is again O(N), with the possible exception of coll, the list sub-collections of cards. Depending on the language,
this could have size O(N), or O(N^2). We can get around this and ensure it is O(N) by modifying it. Instead of making it a list of lists, make it as full list of cards, 
sorted by their connected components, and between each different components, add a 'filler card', so in the for loop where we cycle through each component, just cycle through each card, and
make sure to temporarily pause when we hit this filler card."""
