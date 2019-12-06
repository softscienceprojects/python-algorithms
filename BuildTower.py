"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

for example, a tower of 3 floors looks like below
[
  '  *  ', 
  ' *** ', 
  '*****'
]

"""



def tower_builder(n_floors):
    tower = []
    for floor in range(n_floors):
        tower.append( (" " * (n_floors-(floor+1)) ) + ("*" * (floor+(floor+1))) + (" " * (n_floors-(floor+1)) ) )   
    return tower
