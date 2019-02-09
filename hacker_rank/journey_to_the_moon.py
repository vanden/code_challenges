# HTTP://www.hackerrank.com/challenges/journey-to-the-moon/problem

import time
from collections import defaultdict
from functools import wraps

def timing(func):
    @wraps(func)
    def wrap(*args):
        start = time.perf_counter()
#        start = time.time()
        result = func(*args)
        end = time.perf_counter()
#        end = time.time()
        print(end - start, func.__name__)
        return result
    return wrap



def journeyToMoonSlow(n, astronauts):
    # Times out on case 11
    #
    # 3-4 times as long is spent in getCountryCounts as spent in
    # countPairs. Which is a relief, as I can see a number of ways to chop
    # time from getCountryCounts, but don't have any good ideas right now for
    # countPairs.
    counts = getCountryCounts(n, astronauts)
    pairCount = countPairs(counts)
    return pairCount

@timing
def countPairs(countryCounts):
    pairCount = 0
    for i, v in enumerate(countryCounts):
        for _, u in enumerate(countryCounts[i+1:]):
            pairCount += v * u
    return pairCount


@timing
def getCountryCounts(n, astronauts):
    nodes = []
    classes = defaultdict(set)
    for i in range(n):
        nodes.append(Node(i))

    for first, second in astronauts:
        nodes[first].addEdge(second)
        nodes[second].addEdge(first)

    queue = []
    for i in range(n):
        if not nodes[i].explored:
            classes[i].add(i)
            queue.append(nodes[i])
            nodes[i].explored = True
            while queue:
                current = queue.pop()
                current.explored = True
                for edge in current.edges:
                    if not nodes[edge].explored:
                        queue.append(nodes[edge])
                        classes[i].add(edge)
    counts = [len(s) for s in classes.values()]

    return counts

class Node():
    def __init__(self, index):
        self.index = index
        self.edges = []
        self.explored = False
    def addEdge(self, toIndex):
        self.edges.append(toIndex)
    def __repr__(self):
        return "Node(%s) with edges: %s and Explored: %s" %(
            self.index, self.edges, self.explored)

################################################################

def journeyToMoonThird(n, astronauts):
    # Still times out on case 11, but about a 100% speed up on getCountryCounts.

    # However, profiling shows it is now countPairs that is taking all the
    # time. And, the shape of the case shows why: pointless iteration over
    # endless tokens of 1. That should be an easy fix.

    # Except for the fact that nChooseTwo isn't feasible when n is 99996!
    counts = getCountryCountsTry3(n, astronauts)
    pairCount = countPairsTry3(counts)
    return pairCount

@timing
def countPairsTry3(countryCounts):
    pairCount = 0
    origLen = len(countryCounts)
    countryCounts = [n for n in countryCounts if n != 1]
    onesCount = origLen - len(countryCounts)
    for i, v in enumerate(countryCounts):
        for _, u in enumerate(countryCounts[i+1:]):
            pairCount += v * u
        pairCount += v * onesCount

    pairCount += nChooseTwo(onesCount)
    return pairCount

def factorial(n):
    print(n)
    if n < 2:
        return 1
    return n * factorial(n-1)


def nChooseTwo(n):
    return factorial(n) / (2 * factorial(n-2))

@timing
def getCountryCountsTry3(n, astronauts):
    explored = set()
    edges = defaultdict(list)
    queue = []
    classes = defaultdict(set)

    for toNode, fromNode in astronauts:
        edges[fromNode].append(toNode)
        edges[toNode].append(fromNode)
#    print(sum(len(edges[e]) for e in edges))

    for i in range(n):
        if i in explored:
            continue
        classes[i].add(i)
        queue.append(i)
        explored.add(i)

        while queue:
            current = queue.pop()
            explored.add(current)
            for toNode in edges[current]:
                if toNode not in explored:
                    queue.append(toNode)
                    classes[i].add(toNode)

    counts = [len(s) for s in classes.values()]
    return counts



# case2 = [
#     (0, 11), (2, 4), (2, 95), (3, 48), (4, 85), (4, 95), (5, 67), (5, 83),
#     (5, 42), (6, 76), (9, 31), (9, 22), (9, 55), (10, 61), (10, 38),
#     (11, 96), (11, 41), (12, 60), (12, 69), (14, 80), (14, 99), (14, 46),
#     (15, 42), (15, 75), (16, 87), (16, 71), (18, 99), (18, 44), (19, 26),
#     (19, 59), (19, 60), (20, 89), (21, 69), (22, 96), (22, 60), (23, 88),
#     (24, 73), (27, 29), (30, 32), (31, 62), (32, 71), (33, 43), (33, 47),
#     (35, 51), (35, 75), (37, 89), (37, 95), (38, 83), (39, 53), (41, 84),
#     (42, 76), (44, 85), (45, 47), (46, 65), (47, 49), (47, 94), (50, 55),
#     (51, 99), (53, 99), (56, 78), (66, 99), (71, 78), (73, 98), (76, 88),
#     (78, 97), (80, 90), (83, 95), (85, 92), (88, 99), (88, 94)]



# # 500
case3 = [
    (1, 426), (1, 117), (2, 261), (3, 493), (4, 282), (4, 164), (4, 455),
    (5, 116), (6, 139), (7, 288), (7, 428), (8, 71), (10, 357), (10, 55),
    (11, 456), (12, 71), (13, 27), (13, 324), (14, 258), (14, 15),
    (15, 243), (15, 173), (16, 193), (16, 258), (16, 74), (16, 433),
    (16, 350), (16, 61), (16, 62), (17, 104), (18, 418), (18, 268),
    (18, 50), (19, 471), (19, 189), (19, 335), (20, 25), (20, 435),
    (21, 160), (21, 233), (21, 197), (22, 177), (22, 114), (22, 260),
    (23, 59), (23, 78), (25, 113), (25, 260), (26, 217), (27, 118),
    (28, 136), (28, 324), (28, 365), (28, 87), (30, 224), (31, 51),
    (32, 433), (32, 407), (33, 133), (34, 298), (34, 226), (34, 95),
    (35, 129), (35, 289), (37, 335), (38, 107), (38, 203), (38, 365),
    (38, 55), (39, 333), (39, 127), (40, 104), (40, 347), (41, 329),
    (41, 378), (41, 363), (41, 87), (44, 190), (44, 351), (45, 216),
    (46, 52), (47, 148), (47, 277), (48, 444), (48, 323), (48, 356),
    (49, 362), (49, 350), (50, 115), (51, 153), (51, 201), (52, 389),
    (53, 293), (53, 174), (54, 160), (55, 417), (56, 431), (58, 418),
    (58, 391), (59, 71), (60, 121), (60, 262), (61, 404), (61, 101),
    (61, 78), (62, 481), (62, 211), (62, 94), (62, 479), (63, 357),
    (64, 268), (65, 363), (65, 101), (65, 117), (65, 293), (67, 462),
    (67, 335), (68, 136), (68, 464), (69, 259), (69, 403), (69, 415),
    (70, 304), (70, 137), (72, 176), (72, 123), (72, 395), (73, 386),
    (73, 307), (74, 400), (74, 136), (75, 360), (76, 249), (76, 252),
    (77, 464), (77, 203), (77, 197), (77, 383), (78, 243), (78, 444),
    (79, 242), (80, 472), (81, 160), (81, 153), (81, 451), (81, 254),
    (83, 227), (83, 350), (84, 346), (84, 237), (84, 342), (85, 337),
    (86, 109), (87, 355), (88, 300), (88, 325), (88, 327), (89, 354),
    (89, 272), (89, 370), (89, 220), (89, 93), (89, 158), (90, 454),
    (91, 297), (92, 486), (92, 175), (93, 394), (93, 409), (95, 448),
    (95, 294), (95, 366), (95, 309), (95, 442), (96, 264), (96, 464),
    (96, 269), (96, 263), (98, 248), (98, 354), (98, 444), (98, 342),
    (101, 305), (101, 277), (102, 217), (103, 471), (104, 162), (105, 153),
    (105, 124), (106, 482), (107, 152), (107, 421), (107, 158), (107, 437),
    (109, 321), (109, 447), (110, 424), (110, 276), (110, 372), (110, 333),
    (111, 281), (111, 331), (113, 184), (113, 244), (115, 404), (117, 393),
    (117, 430), (117, 379), (117, 189), (117, 158), (118, 458), (118, 213),
    (118, 478), (119, 345), (119, 338), (120, 153), (121, 201), (121, 177),
    (123, 388), (123, 304), (123, 406), (123, 280), (123, 347), (124, 262),
    (124, 397), (124, 147), (124, 213), (124, 283), (125, 378), (125, 460),
    (126, 263), (127, 312), (128, 251), (128, 357), (131, 358), (132, 496),
    (132, 409), (132, 498), (133, 432), (134, 334), (134, 455), (135, 282),
    (135, 435), (136, 369), (137, 176), (138, 390), (138, 142), (139, 336),
    (139, 154), (139, 199), (140, 418), (141, 469), (145, 242), (146, 438),
    (147, 252), (147, 238), (149, 436), (149, 231), (150, 476), (151, 395),
    (151, 340), (152, 476), (152, 491), (152, 431), (153, 452), (153, 484),
    (154, 418), (154, 252), (156, 297), (158, 208), (158, 316), (161, 499),
    (161, 484), (161, 471), (162, 366), (163, 345), (164, 379), (165, 242),
    (165, 421), (167, 389), (167, 286), (168, 320), (168, 361), (168, 466),
    (168, 432), (169, 389), (170, 273), (172, 472), (172, 409), (173, 242),
    (175, 411), (175, 310), (176, 224), (176, 297), (176, 202), (176, 465),
    (176, 373), (178, 459), (178, 229), (178, 181), (179, 332), (180, 358),
    (182, 473), (182, 211), (182, 455), (183, 384), (183, 424), (183, 419),
    (184, 296), (184, 378), (184, 264), (185, 324), (187, 473), (187, 230),
    (188, 264), (188, 242), (188, 414), (191, 344), (191, 264), (191, 276),
    (192, 364), (192, 436), (193, 194), (193, 301), (194, 339), (195, 327),
    (196, 480), (196, 265), (196, 466), (196, 240), (198, 403), (199, 248),
    (199, 492), (200, 207), (201, 459), (202, 404), (202, 429), (203, 273),
    (204, 343), (205, 361), (205, 419), (206, 443), (206, 334), (209, 365),
    (210, 223), (211, 223), (212, 298), (214, 254), (215, 288), (215, 486),
    (217, 331), (217, 366), (219, 408), (219, 445), (219, 237), (221, 397),
    (223, 423), (224, 343), (225, 418), (226, 389), (226, 295), (227, 341),
    (229, 459), (230, 497), (230, 450), (230, 348), (231, 391), (233, 310),
    (234, 281), (234, 361), (238, 473), (239, 429), (239, 461), (240, 274),
    (242, 379), (243, 425), (243, 357), (244, 448), (244, 437), (247, 489),
    (248, 405), (249, 440), (250, 456), (250, 314), (250, 383), (251, 468),
    (253, 360), (253, 463), (255, 499), (257, 290), (257, 307), (258, 480),
    (258, 449), (259, 481), (260, 481), (260, 455), (261, 439), (264, 485),
    (266, 401), (268, 409), (268, 340), (273, 362), (275, 420), (276, 279),
    (277, 467), (277, 316), (280, 386), (281, 305), (283, 399), (288, 365),
    (289, 490), (290, 458), (291, 458), (291, 339), (294, 345), (294, 316),
    (295, 379), (296, 308), (298, 305), (299, 353), (299, 420), (300, 352),
    (300, 340), (303, 306), (306, 456), (306, 417), (306, 356), (308, 459),
    (310, 392), (310, 316), (311, 337), (311, 390), (313, 495), (314, 356),
    (314, 402), (316, 444), (317, 444), (320, 407), (321, 444), (324, 465),
    (326, 410), (326, 494), (327, 392), (329, 386), (329, 485), (332, 398),
    (333, 360), (335, 346), (337, 416), (338, 380), (339, 398), (339, 407),
    (340, 388), (345, 497), (345, 481), (348, 374), (351, 359), (353, 429),
    (354, 406), (356, 371), (357, 438), (357, 378), (363, 394), (364, 472),
    (364, 451), (369, 453), (370, 429), (371, 436), (371, 462), (373, 482),
    (378, 448), (379, 450), (382, 416), (382, 427), (382, 468), (386, 457),
    (386, 435), (388, 452), (395, 490), (396, 492), (399, 487), (400, 416),
    (400, 462), (408, 480), (411, 438), (412, 437), (414, 426), (414, 423),
    (416, 436), (416, 431), (417, 488), (417, 483), (419, 477), (436, 497),
    (438, 453), (445, 491), (456, 465), (456, 476), (458, 470), (466, 488)
]

# Needs  100000
case11 = [(1, 2), (3, 4)]

def report(i, s):
    if i == 42:
        print(i, s)

print(journeyToMoonSlow(500, case3))
print(journeyToMoonThird(500, case3))

#print(journeyToMoonSlow(100000, case11))
print(journeyToMoonThird(100000, case11))
