"""
You always walk only a single block in a direction and you know it takes 
you one minute to traverse one city block, so create a function that will 
return true if the walk the app gives you will take you exactly ten minutes 
(you don't want to be early or late!) and will, of course, return you to your 
starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment 
of direction letters ('n', 's', 'e', or 'w' only). It will never give you 
an empty array (that's not a walk, that's standing still!).
"""


def isValidWalk(walk):
    if len(walk) != 10:
        return False
    else:
        if walk.count('e') == walk.count('w') and walk.count('n') == walk.count('s'):
            return True
        else:
            return False
    
    #need an even number of n/s e/w back to start
    #takes exactly 10 minutes to walk
    
    # should return false if value does not bring you back to start
    # ['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 'n']
    # ['e', 'e', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']
