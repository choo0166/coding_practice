"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""

def solution(iterable):
  n = len(iterable)
  handled = set()
  path, result = [], []

  def dfs(start, visited, path):
    path.append(iterable[start])
    if len(path) == n:
      result.append(path.copy())
    else:
      handled = set()
      for i in range(n):
        if i not in visited and iterable[i] not in handled:
          handled.add(iterable[i])
          visited.add(i)
          dfs(i, visited, path)
    # Backtrack from last visited index
    path.pop()
    visited.remove(start)
    
  for i in range(n):
    # Depth-first search from each element as the root, removing duplicates
    # by ensuring each subsequent element at next level of tree is distinct 
    # from its parent
    if iterable[i] not in handled:
      handled.add(iterable[i])
      visited = set([i])
      dfs(i, visited, path)
  
  return result

solution([1, 2, 1])