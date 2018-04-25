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
        courses = list(range(numCourses))
        intro_courses = set(courses)
        graph = {}
        for course in courses:
            graph[course] = []

        for course, prereq in prerequisites:
            intro_courses.discard(course)
            graph[prereq].append(course)

        print(graph, "Graph")

        # Intro courses have no prereqs
        to_explore = intro_courses

        print(courses)
        print(to_explore, "To Explore")

        reachable = []
        explored = set()

        while to_explore:
            current_course = to_explore.pop()
            print(current_course)
            if current_course in explored:
                print('NO')
                continue
            reachable.append(current_course)
            explored.add(current_course)
            for course in graph[current_course]:
                to_explore.add(course)
            print(reachable)
            print(to_explore)
        return set(reachable) == set(courses)


s = Solution()

test = [[0,1]] # should be False

print(s.canFinish(2, test))

