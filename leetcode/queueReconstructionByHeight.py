#!/usr/bin/env python3
# https://leetcode.com/problems/queue-reconstruction-by-height/description/


class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key=lambda x:(-x[0],x[1]))
        queue = []
        for height, count in people :
            #print(i)
            queue.insert(count, (height, count))
        return queue

s = Solution()
people= [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(people))

# newPeople = [ (-h, k) for (h,k) in people]

# print(newPeople)
# for [h, f] in people:
#     print (-h, f)
