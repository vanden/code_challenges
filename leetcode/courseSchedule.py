#https://leetcode.com/problems/course-schedule/description/



class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2:
            return True
        if not prerequisites:
            return True
        courses = set(range(numCourses))
        intro_courses = set(courses)
        graph = {}
        for course in courses:
            graph[course] = set()

        for course, prereq in prerequisites:
            intro_courses.discard(course)
            graph[prereq].add(course)

        reachable = set().union(intro_courses)

        changed = True
        while changed:
            changed = False
            not_reached = courses.difference(reachable)
            
            for course in not_reached:
                if graph[course].issubset(reachable):
                    changed = True
                    reachable.add(course)
        return reachable == courses


s = Solution()

test = [[0,1]] # should be False

print(s.canFinish(2, test))

