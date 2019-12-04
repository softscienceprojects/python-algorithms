"""takes a string textand returns that string in reverse. For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.

You may get a string containing special characters (for example, !, @, or #).
"""

def reverse(text):
  arr = []
  for letter in text:
    arr[:0] = letter
  return "".join(arr)
  
print reverse("Erin")
print "end test"
