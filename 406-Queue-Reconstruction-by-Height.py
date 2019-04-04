class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people: return []

        peopledct, height, res = {}, [], []
        
        for i in xrange(len(people)):
            if people[i][0] in peopledct:
                peopledct[people[i][0]].append((people[i][1], i))
            else:
                peopledct[people[i][0]] = [(people[i][1], i)]
                height.append(people[i][0])

        height.sort()     

        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res

                
