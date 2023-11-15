""" 
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def solution(nums, k):
  seen = set()
  for num in nums:
    if abs(k - num) in seen:
      return True
    seen.add(num)
  
  return False

solution([10, 15, 3, 7], 30)