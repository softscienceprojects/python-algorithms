"""
the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the 
seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions I and J.

Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

Given a seat number, your task is to return the seat location in the following format:

'2B' would return 'Front-Left'.

If the number is over 60, or the letter is not valid, return 'No Seat!!'.
"""

import re

def front_or_back(seat):
  if int(seat) <= 20:
    return'Front'
  elif int(seat) > 20 and int(seat) <= 40:
    return 'Middle'
  elif int(seat) > 40 and int(seat) <= 60:
    return 'Back'
  else:
    return 'No'
  
def left_or_right(seat):
  if re.search(r"[ABC]", seat):
    return "-Left"
  elif re.search(r"[DEF]", seat):
    return "-Middle"
  elif re.search(r"[GHK]", seat):
    return "-Right"
  else:
    return " Seat!!"
  

def plane_seat(a):
  seat = []
  cleaned= re.split('(\d+)', a)[1:3]
  for place in cleaned:
    if cleaned.index(place) == 0:
      seat.append( front_or_back(place) )
    else:
      seat.append( left_or_right(place) )
  if seat[0] == "No" or seat[1]== " Seat!!":
    return "No Seat!!"
  else:
    return "".join(seat)
