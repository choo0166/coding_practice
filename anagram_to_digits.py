"""
You are given a string formed by concatenating several words corresponding to the integers zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'. Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above, this would be 357.
"""

from collections import Counter

# Map of integer letters
INTEGERS = {
  0: Counter("zero"),
  1: Counter("one"),
  2: Counter("two"),
  3: Counter("three"),
  4: Counter("four"),
  5: Counter("five"),
  6: Counter("six"),
  7: Counter("seven"),
  8: Counter("eight"),
  9: Counter("nine")
}

def solution(string):
  length = len(string)
  letter_counter = Counter(string)
  possibles, sol = {}, []
  # Look through integer map and do a first pass of 
  # all distinct integers that appear in the anagram
  for integer, integer_counter in INTEGERS.items():
    int_length = sum(integer_counter.values())
    if integer_counter.keys() <= letter_counter.keys() and int_length <= length:
      possibles[integer] = integer_counter
      sol.append(integer)
      length -= int_length

  # Now get duplicates of previously seen integers
  while length > 0:
    for integer, integer_counter in possibles.items():
      int_length = sum(integer_counter.values())
      if integer_counter.keys() <= letter_counter.keys() and int_length <= length:
        sol.append(integer)
        length -= int_length
  
  assert length == 0, "Not all integers matched in input string!"
  sol.sort()

  return ''.join([str(x) for x in sol])


solution("niesevehrtfeev")
solution("niesveeviehertifennevf")