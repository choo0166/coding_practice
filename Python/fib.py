"""
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
"""

class RecurseException(Exception):
  """
  The exception thrown when the function is recursed
  """
  def __init__(self, *args, **kwargs):
    self.args = args 
    self.kwargs = kwargs

def tail_recurse(f):
  """
  Decorator to make tail call optimization
  """
  def wrapper(*args, **kwargs):
    while True:
      try:
        return f(*args, **kwargs)
      except RecurseException as e:
        args = e.args 
        kwargs = e.kwargs 
  
  return wrapper

def solution_tail_recursive(n):
  # Tail recursive version of fib(n) that makes
  # call stack O(1) instead of O(n)
  def recurse(*args, **kwargs):
    raise RecurseException(*args, **kwargs)
  
  @tail_recurse
  def helper(n, prev1, prev2):
    if n == 0:
      return prev2
    elif n == 1:
      return prev1 
    else:
      # recursive call to helper with new set of arguments
      return recurse(n-1, prev1 + prev2, prev1) 
  
  return helper(n, 1, 0)


def solution_iterative(n):
  prev1, prev2 = 1, 0
  while n >= 0:
    if n == 0:
      return prev2
    elif n == 1:
      return prev1
    else:
      prev1_tmp = prev1
      prev1 += prev2
      prev2 = prev1_tmp
    n -= 1

solution_tail_recursive(100)