""" Complete the method which returns the number which is most frequent in the given input array. 
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
"""


def highest_rank(arr):
    ans = {}
    for num in arr:
        if num not in ans:
            ans[num] = 1
        else:
            ans[num] +=1
    biggest_num = []
    for key in ans:
        if ans[key] == max(ans.values()):
            biggest_num.append(key)
    return max(biggest_num)
