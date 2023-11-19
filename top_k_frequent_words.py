"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.
"""

from collections import Counter
import heapq 

def solution(words, k):
  counts = Counter(words)
  heap = []
  for word, count in counts.items():
    heapq.heappush(heap, (-count, word))  # invert min heap to max heap by negating priority

  # Slight optimization by creating heap in-place
  # heap = [(-count, word) for word, count in counts.items()]
  # heapq.heapify(heap)
  
  return [heapq.heappop(heap)[1] for i in range(k)]

solution(["i","love","leetcode","i","love","coding"], 2)
solution(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)